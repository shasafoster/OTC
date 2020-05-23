from datetime import time
from itertools import chain

import pandas as pd
from pandas.tseries.holiday import GoodFriday, Holiday
from pytz import timezone, UTC

from calendars.common_holidays import (
    new_years_day,
    maundy_thursday,
    european_labour_day,
    saint_peter_and_saint_paul_day,
    all_saints_day,
    immaculate_conception,
    christmas,
    new_years_eve,
)

####################
# Regular Holidays #
####################
NewYearsDay = new_years_day()

MaundyThursday = maundy_thursday()

LabourDay = european_labour_day()

SaintPeterAndSaintPaulDay = saint_peter_and_saint_paul_day()

IndependenceDay1 = Holiday('Independence Day', month=7, day=28)
IndependenceDay2 = Holiday('Independence Day', month=7, day=29)

SantaRosa = Holiday('Santa Rosa', month=8, day=30)

BattleOfAngamos = Holiday('Battle of Angamos', month=10, day=8)

AllSaintsDay = all_saints_day()

ImmaculateConception = immaculate_conception()

Christmas = christmas()

NewYearsEve = new_years_eve(end_date='2008')


def holidays():
    return [
        NewYearsDay,
        MaundyThursday,
        GoodFriday,
        LabourDay,
        SaintPeterAndSaintPaulDay,
        IndependenceDay1,
        IndependenceDay2,
        SantaRosa,
        BattleOfAngamos,
        AllSaintsDay,
        ImmaculateConception,
        Christmas,
        NewYearsEve,
    ]


