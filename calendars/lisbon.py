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

from pandas.tseries.holiday import Holiday, GoodFriday, Easter, EasterMonday
from pandas.tseries.offsets import Day
from pytz import timezone

from .common_holidays import (
    new_years_day,
    corpus_christi,
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

Carnival = Holiday(
    'Carnival',
    month=1,
    day=1,
    offset=[Easter(), Day(-47)],
    end_date='2003',
)
CorpusChristi = corpus_christi(end_date='2003')

LibertyDay = Holiday(
    'Liberty Day',
    month=4,
    day=25,
    end_date='2003',
)

LabourDay = european_labour_day()

PortugalDay = Holiday(
    'Portugal Day',
    month=6,
    day=10,
    end_date='2003',
)

SaintAnthonysDay = Holiday(
    "Saint Anthony's Day",
    month=6,
    day=13,
    end_date='2002',
)

AssumptionDay = assumption_day(end_date='2003')

RepublicDay = Holiday(
    'Republic Day',
    month=10,
    day=5,
    end_date='2003',
)

AllSaintsDay = all_saints_day(end_date='2003')

IndependenceDay = Holiday(
    'Independence Day',
    month=12,
    day=1,
    end_date='2003',
)

ImmaculateConception = immaculate_conception(end_date='2003')

ChristmasEveBefore2003 = christmas_eve(end_date='2003')
ChristmasEve = christmas_eve(start_date='2003', days_of_week=WEEKDAYS)
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve(days_of_week=WEEKDAYS)


def holidays():
    return [
        NewYearsDay,
        Carnival,
        GoodFriday,
        EasterMonday,
        CorpusChristi,
        LibertyDay,
        LabourDay,
        PortugalDay,
        SaintAnthonysDay,
        AssumptionDay,
        RepublicDay,
        AllSaintsDay,
        IndependenceDay,
        ImmaculateConception,
        ChristmasEveBefore2003,
        Christmas,
        BoxingDay,
    ]

