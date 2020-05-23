#
# Copyright 2018 Quantopian, Inc.
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

from pandas.tseries.holiday import Holiday, GoodFriday, EasterMonday
from pytz import timezone

from calendars.common_holidays import (
    new_years_day,
    ascension_day,
    whit_monday,
    european_labour_day,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
    WEEKDAYS
)

NewYearsDay = new_years_day()

AscensionDay = ascension_day(end_date='2001')
WhitMonday = whit_monday(end_date='2002')

QueensDay = Holiday(
    "Queen's Day",
    month=4,
    day=30,
    end_date='2002',
)

LabourDay = european_labour_day()

ChristmasEve = christmas_eve(days_of_week=WEEKDAYS)
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEveBefore2002 = new_years_eve(end_date='2002')
NewYearsEveInOrAfter2002 = new_years_eve(
    start_date='2002',
    days_of_week=WEEKDAYS,
)



def holidays():
    return [
        NewYearsDay,
        GoodFriday,
        EasterMonday,
        AscensionDay,
        WhitMonday,
        QueensDay,
        LabourDay,
        Christmas,
        BoxingDay,
        NewYearsEveBefore2002,
    ]


