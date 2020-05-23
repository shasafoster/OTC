from datetime import time

from pandas.tseries.holiday import (
    Holiday,
    GoodFriday,
    EasterMonday,
    previous_friday,
)
from pytz import timezone

from calendars.common_holidays import (
    new_years_day,
    epiphany,
    ascension_day,
    whit_monday,
    corpus_christi,
    european_labour_day,
    assumption_day,
    all_saints_day,
    immaculate_conception,
    christmas_eve,
    christmas,
    new_years_eve,
)


NewYearsDay = new_years_day()

Epiphany = epiphany(end_date='2019')

AscensionDay = ascension_day(end_date='2019')
WhitMonday = whit_monday()
CorpusChristi = corpus_christi(end_date='2019')

LabourDay = european_labour_day()

AssumptionDay = assumption_day(end_date='2019')

NationalHoliday = Holiday('National Holiday', month=10, day=26)

AllSaintsDay = all_saints_day(end_date='2019')

ImmaculateConception = immaculate_conception(end_date='2019')

ChristmasEve = christmas_eve()
Christmas = christmas()

SaintStephensDay = Holiday("Saint Stephen's Day", month=12, day=26)

# Prior to 2016, when New Year's Eve fell on the weekend, it was observed
# on the preceding Friday. In 2016 and after, it is not made up.
NewYearsEveThrough2015 = new_years_eve(
    observance=previous_friday,
    end_date='2016',
)
NewYearsEve2016Onwards = new_years_eve(start_date='2016')


def holidays():
    return [
        NewYearsDay,
        Epiphany,
        GoodFriday,
        EasterMonday,
        AscensionDay,
        WhitMonday,
        CorpusChristi,
        LabourDay,
        AssumptionDay,
        NationalHoliday,
        AllSaintsDay,
        ImmaculateConception,
        ChristmasEve,
        Christmas,
        SaintStephensDay,
        NewYearsEveThrough2015,
        NewYearsEve2016Onwards,
    ]
