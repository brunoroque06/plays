from datetime import date

from dateutil.relativedelta import relativedelta


# Required because pd.Interval does not support `relativedelta`, due to not being hashable
def delta_idx(r: relativedelta, inc: bool = False) -> float:
    d = 1 if inc else 0
    r = (r + relativedelta(months=d)).normalized()
    return float(f"{r.years}.{r.months:02}")


def format_date(d: date, inc_day: bool = True) -> str:
    if inc_day:
        return d.strftime("%d.%m.%Y")
    return d.strftime("%m.%Y")
