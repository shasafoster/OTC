# Wellington holidays

# Useful source for the history of New Zealand public holidays:
# Nancy Swarbrick, 'Public holidays', Te Ara - the Encyclopedia of New Zealand
# http://www.TeAra.govt.nz/en/public-holidays/print (accessed 22 December 2019)

from datetime import time
from pytz import UTC
from pandas import Timestamp

from pandas.tseries.holiday import (
    DateOffset,
    EasterMonday,
    GoodFriday,
    Holiday,
    MO,
    next_monday,
    next_monday_or_tuesday,
    previous_workday,
    weekend_to_monday,
)
from pytz import timezone

from calendars.common_holidays import (
    new_years_day,
    anzac_day,
    christmas,
    boxing_day,
)


# Prior to 2015, Waitangi Day and Anzac Day are not "Mondayized",
# that is, if they occur on the weekend, there is no make-up.
MONDAYIZATION_START_DATE = "2015-01-01"

# Regular Holidays
# ----------------
NewYearsDay = new_years_day(observance=next_monday)

DayAfterNewYearsDay = Holiday(
    "Day after New Year's Day",
    month=1,
    day=2,
    observance=next_monday_or_tuesday,
)

WaitangiDayNonMondayized = Holiday(
    "Waitangi Day",
    month=2,
    day=6,
    end_date=MONDAYIZATION_START_DATE,
)

WaitangiDay = Holiday(
    "Waitangi Day",
    month=2,
    day=6,
    observance=weekend_to_monday,
    start_date=MONDAYIZATION_START_DATE,
)

AnzacDayNonMondayized = anzac_day(end_date=MONDAYIZATION_START_DATE)

AnzacDay = anzac_day(
    observance=weekend_to_monday,
    start_date=MONDAYIZATION_START_DATE,
)

QueensBirthday = Holiday(
    "Queen's Birthday",
    month=6,
    day=1,
    offset=DateOffset(weekday=MO(1)),
)

LabourDay = Holiday(
    "Labour Day",
    month=10,
    day=1,
    offset=DateOffset(weekday=MO(4)),
)

Christmas = christmas(observance=next_monday)

BoxingDay = boxing_day(observance=next_monday_or_tuesday)

def holidays():
    return [
        NewYearsDay,
        DayAfterNewYearsDay,
        WaitangiDayNonMondayized,
        WaitangiDay,
        GoodFriday,
        EasterMonday,
        AnzacDayNonMondayized,
        AnzacDay,
        QueensBirthday,
        LabourDay,
        Christmas,
        BoxingDay,
    ]



