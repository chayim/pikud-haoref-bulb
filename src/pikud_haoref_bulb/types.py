from dataclasses import dataclass
from datetime import date, datetime, time
from enum import Enum
from typing import Any


class PikudState(Enum):
    LEAVE_THE_MAMAD = 13
    EARLY_WARNING = 14
    ROCKETS = 1

    # when things are bad
    NO_INTERNET = -1


@dataclass
class PikudEntry:
    data: str
    date: date
    time: time
    alert_date: datetime
    category: int
    category_desc: str
    matrix_id: int
    rid: int
    name_he: str
    name_en: str
    name_ar: str
    name_ru: str

    @classmethod
    def no_internet(cls) -> "PikudEntry":
        now = datetime.now()
        return cls(
            data="",
            date=now.date(),
            time=now.time(),
            alert_date=now,
            category=PikudState.NO_INTERNET.value,
            category_desc="No internet connection",
            matrix_id=0,
            rid=0,
            name_he="",
            name_en="",
            name_ar="",
            name_ru="",
        )

    @classmethod
    def no_alerts(cls) -> "PikudEntry":
        now = datetime.now()
        return cls(
            data="",
            date=now.date(),
            time=now.time(),
            alert_date=now,
            category=PikudState.LEAVE_THE_MAMAD.value,
            category_desc="No active alerts",
            matrix_id=0,
            rid=-1,
            name_he="",
            name_en="",
            name_ar="",
            name_ru="",
        )

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "PikudEntry":
        return cls(
            data=raw["data"],
            date=datetime.strptime(raw["date"], "%d.%m.%Y").date(),
            time=datetime.strptime(raw["time"], "%H:%M:%S").time(),
            alert_date=datetime.fromisoformat(raw["alertDate"]),
            category=int(raw["category"]),
            category_desc=raw["category_desc"],
            matrix_id=int(raw["matrix_id"]),
            rid=int(raw["rid"]),
            name_he=raw["NAME_HE"],
            name_en=raw["NAME_EN"],
            name_ar=raw["NAME_AR"],
            name_ru=raw["NAME_RU"],
        )
