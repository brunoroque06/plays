import typing
from dataclasses import dataclass
from datetime import timedelta


@dataclass
class Section:
    id: str
    values: typing.List[str]


def get_sections(age: timedelta) -> typing.List[Section]:
    hand = Section(id="Handgeschicklichkeit", values=["hg11", 'hg12', 'hg2', 'hg3'])
    ball = Section(id="Ballfertigkeiten", values=['bf1', 'bf2'])
    balance = Section(id="Balance", values=["bl11", "bl12", "bl2"])
    if timedelta(days=365) * 6 < age:
        balance.values.append("bl3")
    else:
        balance.values.extend(["bl31", "bl32"])
    return [hand, ball, balance]
