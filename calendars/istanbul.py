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

from datetime import time, timedelta
from itertools import chain
import pandas as pd
from pandas.tseries.holiday import Holiday
from pytz import timezone, UTC

from calendars.common_holidays import (
    european_labour_day,
    new_years_day,
    WEEKDAYS,
    WEEKENDS
)

NewYearsDay = new_years_day()

NationalSovereigntyAndChildrensDay = Holiday(
    "National Sovereignty and Children's Day",
    month=4,
    day=23,
)

LabourDay = european_labour_day(start_date='2009')

CommemorationOfAttaturkYouthAndSportsDay = Holiday(
    'Commemoration of Attaturk, Youth and Sports Day',
    month=5,
    day=19,
)



DemocracyAndNationalUnityDay = Holiday(
    'Democracy and National Unity Day',
    month=7,
    day=15,
    start_date='2017'
)



VictoryDay = Holiday(
    'Victory Day',
    month=8,
    day=30,
)

RepublicDay = Holiday(
    'Republic Day',
    month=10,
    day=29,
)



def holidays():
    return [
        NewYearsDay,
        NationalSovereigntyAndChildrensDay,
        LabourDay,
        CommemorationOfAttaturkYouthAndSportsDay,
        DemocracyAndNationalUnityDay,
        VictoryDay,
        RepublicDay,
    ]

