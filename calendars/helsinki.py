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
    epiphany,
    european_labour_day,
    ascension_day,
    midsummer_eve,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)

NewYearsDay = new_years_day()

Epiphany = epiphany()

LabourDay = european_labour_day()

AscensionDay = ascension_day()

MidsummerEve = midsummer_eve()

IndependenceDay = Holiday('Finland Independence Day', month=12, day=6)

ChristmasEve = christmas_eve()
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve()


def holidays():
    return [
        NewYearsDay,
        Epiphany,
        GoodFriday,
        EasterMonday,
        LabourDay,
        AscensionDay,
        MidsummerEve,
        IndependenceDay,
        ChristmasEve,
        Christmas,
        BoxingDay,
        NewYearsEve,
    ]
