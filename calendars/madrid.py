from datetime import time

from pandas.tseries.holiday import (
    Holiday,
    GoodFriday,
    EasterMonday,
    weekend_to_monday,
)
from pytz import timezone

from .common_holidays import (
    new_years_day,
    epiphany,
    european_labour_day,
    assumption_day,
    all_saints_day,
    immaculate_conception,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
    WEEKDAYS
)

NewYearsDay = new_years_day()

Epiphany = epiphany(end_date='2007')

LabourDay = european_labour_day()

AssumptionDay = assumption_day(end_date='2005', observance=weekend_to_monday)

NationalDay = Holiday(
    'National Day',
    month=10,
    day=12,
    end_date='2005',
)

AllSaintsDay = all_saints_day(end_date='2005')

ConstitutionDay = Holiday(
    'Constitution Day',
    month=12,
    day=6,
    end_date='2005',
)

ImmaculateConception = immaculate_conception(end_date='2005')

ChristmasEveThrough2010 = christmas_eve(end_date='2011')
ChristmasEveEarlyClose2012Onwards = christmas_eve(
    start_date='2012',
    days_of_week=(WEEKDAYS),
)
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEveThrough2010 = new_years_eve(end_date='2011')
NewYearsEveEarlyClose2012Onwards = new_years_eve(
    start_date='2012',
    days_of_week=(WEEKDAYS),
)


def holidays():
    return [
        NewYearsDay,
        Epiphany,
        GoodFriday,
        EasterMonday,
        LabourDay,
        AssumptionDay,
        NationalDay,
        AllSaintsDay,
        ConstitutionDay,
        ImmaculateConception,
        ChristmasEveThrough2010,
        Christmas,
        BoxingDay,
        NewYearsEveThrough2010,
    ]


