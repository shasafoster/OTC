"""
ISDA 30/360 day count convention.
=====

Implemented according to 2006 ISDA definition:
http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
"""

import pandas as pd
import numpy as np

name = 'thirty/360'


def day_count(start_date, end_date):
    """Return number of days between start_date and end_date, using Thirty/360 convention."""
    d1 = np.minimum(30, pd.Series(start_date.day))
    d2 = [min(v1, v2) if v1 == 30 else v2 for v1,v2 in zip(d1,pd.Series(end_date.day))]

    return 360*(pd.Series(end_date.year) - pd.Series(start_date.year)) \
           + 30*(pd.Series(end_date.month) - pd.Series(start_date.month)) \
           + d2 - d1  


def year_fraction(start_date, end_date):
    """Return fraction in years between start_date and end_date, using Thirty/360 convention."""
    return day_count(start_date, end_date) / 360.0
