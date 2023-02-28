import pytest
from dateutil.relativedelta import relativedelta

from asmt import time


@pytest.mark.parametrize(
    "year,month,inc,res",
    [
        (4, 2, False, 4.02),
        (4, 10, False, 4.1),
        (4, 12, False, 5),
        (4, 11, True, 5),
        (4, 13, False, 5.01),
    ],
)
def test_delta_idx(year: int, month: int, inc: bool, res: float):
    assert time.delta_idx(relativedelta(years=year, months=month), inc=inc) == res
