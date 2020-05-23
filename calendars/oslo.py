from datetime import time

from pandas.tseries.holiday import AbstractHolidayCalendar, EasterMonday, GoodFriday, Holiday
from pandas.tseries.offsets import Day, Easter
from pytz import timezone


OSENewYearsDay = Holiday(
    "New Year's Day",
    month=1,
    day=1
)

OSEWednesdayBeforeEaster = Holiday(
    "Wednesday before Easter",
    month=1,
    day=1,
    offset=[Easter(), Day(-4)]

)

OSEMaundyThursday = Holiday(
    "Maundy Thursday",
    month=1,
    day=1,
    offset=[Easter(), Day(-3)]
)

OSEGoodFriday = GoodFriday

OSEEasterMonday = EasterMonday

OSELabourDay = Holiday(
    "Labour Day",
    month=5,
    day=1
)

OSEConstitutionDay = Holiday(
    "Constitution Day",
    month=5,
    day=17
)

OSEWhitMonday = Holiday(
    "Whit Monday",
    month=1,
    day=1,
    offset=[Easter(), Day(50)]
)

OSEAscensionDay = Holiday(
    "Ascension Day",
    month=1,
    day=1,
    offset=[Easter(), Day(39)]
)

OSEChristmasEve = Holiday(
    "Christmas Eve",
    month=12,
    day=24,
)

OSEChristmasDay = Holiday(
    "Christmas Day",
    month=12,
    day=25
)

OSEBoxingDay = Holiday(
    "Boxing Day",
    month=12,
    day=26
)

OSENewYearsEve = Holiday(
    "New Year's Eve",
    month=12,
    day=31
)


def holidays():
    return [OSENewYearsDay,
        OSEMaundyThursday,
        OSEGoodFriday,
        OSEEasterMonday,
        OSELabourDay,
        OSEConstitutionDay,
        OSEWhitMonday,
        OSEAscensionDay,
        OSEChristmasEve,
        OSEChristmasDay,
        OSEBoxingDay,
        OSENewYearsEve]

