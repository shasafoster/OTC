from datetime import time
from pandas.tseries.offsets import Day
from pandas import Timestamp
from pandas.tseries.holiday import (
    Easter,
    GoodFriday,
    Holiday,
    sunday_to_monday,
)
from pytz import timezone, UTC

from calendars.common_holidays import new_years_day


def holidays():
    return [
        new_years_day(
            observance=sunday_to_monday,
        ),
        Holiday(
            "Human Rights Day",
            month=3,
            day=21,
            observance=sunday_to_monday,
        ),
        GoodFriday,
        Holiday(
            "Family Day",
            month=1,
            day=1,
            offset=[Easter(), Day(1)],
        ),
        Holiday(
            "Freedom Day",
            month=4,
            day=27,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Workers' Day",
            month=5,
            day=1,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Youth Day",
            month=6,
            day=16,
            observance=sunday_to_monday,
        ),
        Holiday(
            "National Women's Day",
            month=8,
            day=9,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Heritage Day",
            month=9,
            day=24,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Day of Reconciliation",
            month=12,
            day=16,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Christmas",
            month=12,
            day=25,
            observance=sunday_to_monday,
        ),
        Holiday(
            "Day of Goodwill",
            month=12,
            day=26,
            observance=sunday_to_monday,
        ),
    ]

