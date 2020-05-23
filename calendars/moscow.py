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
from itertools import chain

import pandas as pd
from pandas.tseries.holiday import Holiday, weekend_to_monday
from pytz import timezone, UTC

from calendars.common_holidays import new_years_day, new_years_eve, european_labour_day, WEEKDAYS


def new_years_eve_observance(holidays):
    # For some reason New Year's Eve was not a holiday these years.
    holidays = holidays[
        (holidays.year != 2008) &
        (holidays.year != 2009)
    ]

    return pd.to_datetime([weekend_to_monday(day) for day in holidays])


def new_years_holiday_observance(holidays):
    # New Year's Holiday did not follow the next-non-holiday rule in 2016.
    holidays = holidays[(holidays.year != 2016)]

    return pd.to_datetime([weekend_to_monday(day) for day in holidays])


def orthodox_christmas_observance(holidays):
    # Orthodox Christmas did not follow the next-non-holiday rule these years.
    holidays = holidays[
        (holidays.year != 2012) &
        (holidays.year != 2017)
    ]

    return pd.to_datetime([weekend_to_monday(day) for day in holidays])


def defender_of_fatherland_observance(holidays):
    # Defender of the Fatherland Day did not follow the next-non-holiday rule
    # these years.
    holidays = holidays[
        (holidays.year != 2013) &
        (holidays.year != 2014) &
        (holidays.year != 2019)
    ]

    return pd.to_datetime([weekend_to_monday(day) for day in holidays])


NewYearsDay = new_years_day(observance=weekend_to_monday)
NewYearsHoliday = Holiday(
    "New Year's Holiday",
    month=1,
    day=2,
    observance=new_years_holiday_observance,
)
NewYearsHoliday2 = Holiday(
    "New Year's Holiday",
    month=1,
    day=3,
    start_date='2005',
    end_date='2012',
)
NewYearsHoliday3 = Holiday(
    "New Year's Holiday",
    month=1,
    day=4,
    start_date='2005',
    end_date='2012',
)
NewYearsHoliday4 = Holiday(
    "New Year's Holiday",
    month=1,
    day=5,
    start_date='2005',
    end_date='2012',
)
NewYearsHoliday5 = Holiday(
    "New Year's Holiday",
    month=1,
    day=6,
    start_date='2005',
    end_date='2012',
)

OrthodoxChristmas = Holiday(
    'Orthodox Christmas',
    month=1,
    day=7,
    observance=orthodox_christmas_observance,
)

DefenderOfTheFatherlandDay = Holiday(
    'Defender of the Fatherland Day',
    month=2,
    day=23,
    observance=defender_of_fatherland_observance,
)

WomensDay = Holiday(
    "Women's Day",
    month=3,
    day=8,
    observance=weekend_to_monday,
)

LabourDay = european_labour_day(observance=weekend_to_monday)

VictoryDay = Holiday(
    'Victory Day',
    month=5,
    day=9,
    observance=weekend_to_monday,
)

DayOfRussia = Holiday(
    'Day of Russia',
    month=6,
    day=12,
    observance=weekend_to_monday,
)

UnityDay = Holiday(
    'Unity Day',
    month=11,
    day=4,
    observance=weekend_to_monday,
    start_date='2005',
)

NewYearsEve = new_years_eve(
    observance=new_years_eve_observance,
    days_of_week=WEEKDAYS,
)


def holidays():
    return [
        NewYearsDay,
        NewYearsHoliday,
        NewYearsHoliday2,
        NewYearsHoliday3,
        NewYearsHoliday4,
        NewYearsHoliday5,
        OrthodoxChristmas,
        DefenderOfTheFatherlandDay,
        WomensDay,
        LabourDay,
        VictoryDay,
        DayOfRussia,
        UnityDay,
        NewYearsEve,
    ]


