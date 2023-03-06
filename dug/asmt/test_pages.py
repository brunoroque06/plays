import os
from collections.abc import Iterable
from pathlib import Path

import pytest


def list_pages() -> Iterable[str]:
    for f in Path("pages").glob("*.py"):
        if "test_" in str(f):
            continue
        yield str(f).split(".", maxsplit=1)[0].replace(os.sep, ".")


@pytest.mark.parametrize("page", list_pages())
def test_pages(page: str):
    __import__(page)
