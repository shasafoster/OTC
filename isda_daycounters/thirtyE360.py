"""
ISDA 30E/360 (Eurobond basis) day count convention.
=====

Implemented according to 2008 ISDA definition:
https://www.isda.org/2008/12/22/30-360-day-count-conventions/
"""

import pandas as pd
import numpy as np

name = 'thirtyE/360'


def day_count(start_date, end_date):
    """Return number of days between start_date and end_date, using ThirtyE/360 convention."""
    d1 = np.minimum(30, pd.Series(start_date.day))
    d2 = np.minimum(30, pd.Series(end_date.day))

    return 360 * (pd.Series(end_date.year) - pd.Series(start_date.year)) \
           + 30 * (pd.Series(end_date.month) - pd.Series(start_date.month)) \
           + d2 - d1


def year_fraction(start_date, end_date):
    """Return fraction in years between start_date and end_date, using ThirtyE/360 convention."""
    return day_count(start_date, end_date) / 360.0
