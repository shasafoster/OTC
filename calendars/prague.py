#
# Copyright 2019 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
import pandas as pd
from pandas.tseries.holiday import (
    Easter,
    EasterMonday,
    Holiday,
)
from pandas.tseries.offsets import Day
from pytz import UTC, timezone

from calendars.common_holidays import (
    new_years_day,
    new_years_eve,
    european_labour_day,
    christmas,
    christmas_eve,
)


NewYearsDay = new_years_day()

# Need custom start year so can't use pandas GoodFriday
GoodFriday = Holiday(
    "Good Friday",
    month=1,
    day=1,
    offset=[Easter(), Day(-2)],
    start_date='2013'
)

LabourDay = european_labour_day()

LiberationDay = Holiday(
    'Liberation Day',
    month=5,
    day=8,
)

SaintsCyrilAndMethodiusDay = Holiday(
    'Saints Cyril and Methodius Day',
    month=7,
    day=5,
)

JanHusDay = Holiday(
    'Jan Hus Day',
    month=7,
    day=6,
)

CzechStatehoodDay = Holiday(
    'Czech Statehood Day',
    month=9,
    day=28,
)

IndependenceDay = Holiday(
    'Independence Day',
    month=10,
    day=28,
)

StruggleForFreedomAndDemocracyDay = Holiday(
    'Struggle for Freedom and Democracy Day',
    month=11,
    day=17,
)

ChristmasEve = christmas_eve()

ChristmasDay = christmas()

SecondDayOfChristmas = Holiday(
    'Second Day of Christmas',
    month=12,
    day=26,
)

ExchangeHoliday = new_years_eve()



def holidays():

    return [
        NewYearsDay,
        GoodFriday,
        EasterMonday,
        LabourDay,
        LiberationDay,
        SaintsCyrilAndMethodiusDay,
        JanHusDay,
        CzechStatehoodDay,
        IndependenceDay,
        StruggleForFreedomAndDemocracyDay,
        ChristmasEve,
        ChristmasDay,
        SecondDayOfChristmas,
        ExchangeHoliday,
    ]
