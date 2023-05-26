import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

import pytest
from playwright.sync_api import Page

port = 8501
host = f"http://localhost:{port}"


def list_pages() -> Iterable[str]:
    for f in Path("pages").glob("*.py"):
        yield f.name.split(".", maxsplit=1)[0]


@pytest.fixture(autouse=True, scope="module")
def start_app():
    with subprocess.Popen(
        [
            "streamlit",
            "run",
            "Home.py",
            "--browser.serverPort",
            str(port),
            "--server.headless",
            "true",
        ]
    ) as app:
        while True:
            try:
                with urllib.request.urlopen(host) as r:
                    if r.code == 200:
                        break
            except urllib.error.URLError:
                pass
            time.sleep(1)
        yield
        app.terminate()


@pytest.mark.parametrize("url", list_pages())
def test_pages(page: Page, url: str):
    page.goto(f"{host}/{url}")
    page.wait_for_selector(".stApp", timeout=5000)
    page.wait_for_timeout(2000)  # what to wait for exactly?
    assert page.locator(".stException").count() == 0
