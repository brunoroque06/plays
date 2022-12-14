from dateutil.relativedelta import relativedelta


# Required because pd.Interval does not support relativedelta
def delta_idx(r: relativedelta, inc: bool = False) -> float:
    d = 1 if inc else 0
    r = (r + relativedelta(months=d)).normalized()
    return float(f"{r.years}.{r.months:02}")
