"""
ISDA Actual/Actual day count convention.
=====

Implemented according to 2006 ISDA definition:
http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
"""

import calendar
from datetime import datetime
import pandas as pd

name = 'actual/actual'


def day_count(start_date, end_date):
    """Returns number of days between start_date and end_date, using Actual/Actual convention"""
    return (end_date - start_date).days


def year_fraction(start_date, end_date):
    """Returns fraction in years between start_date and end_date, using Actual/Actual convention"""

    start_year = pd.Series(start_date.year)
    end_year = pd.Series(end_date.year)
    year_1_diff = 365 + start_year.map(calendar.isleap)
    year_2_diff = 365 + end_year.map(calendar.isleap) 
    
    total_sum = end_year - start_year - 1
    diff_first = pd.Series([datetime(v + 1, 1, 1) for v in start_year]) - start_date
    total_sum += diff_first.dt.days / year_1_diff
    diff_second = end_date - pd.Series([datetime(v, 1, 1) for v in end_year]) 
    total_sum += diff_second.dt.days / year_2_diff

    return total_sum
