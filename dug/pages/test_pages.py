import glob
import os
from os import path

import pytest


def list_pages() -> list[str]:
    dire = path.dirname(path.relpath(__file__, start=os.getcwd()))
    for f in glob.glob(path.join(dire, "*.py")):
        if "test_" in f:
            continue
        yield f.split(".")[0].replace(os.sep, ".")


@pytest.mark.parametrize("page", list_pages())
def test_pages(page: str):
    __import__(page)
