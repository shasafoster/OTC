import pandas as pd
import numpy as np
from pandas.tseries.offsets import CustomBusinessDay   
from pandas.tseries.holiday import AbstractHolidayCalendar, HolidayCalendarFactory
import os
import sys


os.chdir('G:/My Drive/OTC/calendars/')
from amsterdam import AMS_holidays
from copenhagen import COP_holidays
from helsinki import HEL_holidays
from johannesburg import JOH_holidays
from london import LON_holidays
from new_york  import NY_holidays
from oslo import OSL_holidays
from stockholm import STO_holidays
from sydney import SYD_holidays
from tokyo import TKY_holidays
from wellington import WEL_holidays
from zurich import ZUR_holidays

#%%

AMS_rules = AMS_holidays()
COP_rules = COP_holidays()
HEL_rules = HEL_holidays()
JOH_rules = JOH_holidays()
LON_rules = LON_holidays()
NY_rules  = NY_holidays()
OSL_rules = OSL_holidays()
STO_rules = STO_holidays()
SYD_rules = SYD_holidays()
TKY_rules = TKY_holidays()
WEL_rules = WEL_holidays()
ZUR_rules = ZUR_holidays()

#%%

        


















