import glob
import os
from os import path
from typing import Iterable

import pytest


def list_pages() -> Iterable[str]:
    for f in glob.glob(path.join("pages", "*.py")):
        if "test_" in f:
            continue
        yield f.split(".")[0].replace(os.sep, ".")


@pytest.mark.parametrize("page", list_pages())
def test_pages(page: str):
    __import__(page)
