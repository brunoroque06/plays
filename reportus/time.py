from datetime import date


def format_date(d: date, inc_day: bool = True) -> str:
    if inc_day:
        return d.strftime("%d.%m.%Y")
    return d.strftime("%m.%Y")
