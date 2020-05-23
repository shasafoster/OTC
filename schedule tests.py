# -*- coding: utf-8 -*-
"""
Testing the correctness of the schedule function

@author: ShasaFoster
"""

import schedule as sch
from pandas import Timestamp
from numpy import nan
import numpy as np
import pandas as pd

#%% General tests

payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('15-Apr-2020'),
                          payment_freq='Q', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('15-Apr-2020'),Timestamp('15-Apr-2020')]])
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('15-Jul-2020'),
                          payment_freq='Q', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('15-Apr-2020'),Timestamp('15-Apr-2020')],
                [Timestamp('15-Apr-2020'),Timestamp('15-Jul-2020'),Timestamp('15-Jul-2020')]])
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('15-Jan-2021'),
                          payment_freq='Q', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('15-Apr-2020'),Timestamp('15-Apr-2020')],
                [Timestamp('15-Apr-2020'),Timestamp('15-Jul-2020'),Timestamp('15-Jul-2020')],
                [Timestamp('15-Jul-2020'),Timestamp('15-Oct-2020'),Timestamp('15-Oct-2020')],
                [Timestamp('15-Oct-2020'),Timestamp('15-Jan-2021'),Timestamp('15-Jan-2021')]])
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('15-Jan-2021'),
                          payment_freq='A', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('15-Jan-2021'),Timestamp('15-Jan-2021')]])
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('15-May-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('17-Feb-2020'),Timestamp('17-Feb-2020')], # 15-Feb-2020 falls on Saturday, roll to 17th
                [Timestamp('17-Feb-2020'),Timestamp('16-Mar-2020'),Timestamp('16-Mar-2020')], # 15-Mar-2020 falls on Sunday, roll to 16th
                [Timestamp('16-Mar-2020'),Timestamp('15-Apr-2020'),Timestamp('15-Apr-2020')], 
                [Timestamp('15-Apr-2020'),Timestamp('15-May-2020'),Timestamp('15-May-2020')]])
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('30-Sep-2020'), 
                          end_date=Timestamp('31-Oct-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('30-Sep-2020'),Timestamp('31-Oct-2020'),Timestamp('31-Oct-2020')]]) # 31-Aug-2020 is Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('30-Sep-2020'), 
                          end_date=Timestamp('31-Oct-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('30-Sep-2020'),Timestamp('31-Oct-2020'),Timestamp('31-Oct-2020')]]) # 31-Aug-2020 is Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('31-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='following', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('31-Jan-2020'),Timestamp('2-Mar-2020'),Timestamp('2-Mar-2020')], # 29-Feb-2020 falls on Saturday, roll to 2-March-2020
                [Timestamp('2-Mar-2020'),Timestamp('31-Mar-2020'),Timestamp('31-Mar-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('30-Apr-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('31-May-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()


#%% Test the payment delay 

payment_schedule = sch.payment_schedule(start_date=Timestamp('31-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='following', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=1,
                          cal=nan)
arr = np.array([[Timestamp('31-Jan-2020'),Timestamp('2-Mar-2020'),Timestamp('3-Mar-2020')], # 29-Feb-2020 falls on Saturday, roll to 2-March-2020
                [Timestamp('2-Mar-2020'),Timestamp('31-Mar-2020'),Timestamp('1-Apr-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('1-May-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('1-June-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

payment_schedule = sch.payment_schedule(start_date=Timestamp('31-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='following', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in advance', 
                          payment_delay=1,
                          cal=nan)
arr = np.array([[Timestamp('31-Jan-2020'),Timestamp('2-Mar-2020'),Timestamp('3-Feb-2020')], # 29-Feb-2020 falls on Saturday, roll to 2-March-2020
                [Timestamp('2-Mar-2020'),Timestamp('31-Mar-2020'),Timestamp('3-Mar-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('1-Apr-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('1-May-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

#%% Test Stubs

# The default stub setting is a 'first short' stub
payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub=nan,
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('31-Jan-2020'),Timestamp('31-Jan-2020')], 
                [Timestamp('31-Jan-2020'),Timestamp('28-Feb-2020'),Timestamp('28-Feb-2020')], # 29-Feb-2020 falls on Saturday, roll to 28-Feb-2020
                [Timestamp('28-Feb-2020'),Timestamp('31-Mar-2020'),Timestamp('31-Mar-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('30-Apr-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('31-May-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

# The default stub setting is a 'first short' stub (same result as above)
payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub='first short',
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('31-Jan-2020'),Timestamp('31-Jan-2020')],
                [Timestamp('31-Jan-2020'),Timestamp('28-Feb-2020'),Timestamp('28-Feb-2020')], # 29-Feb-2020 falls on Saturday, roll to 28-Feb-2020
                [Timestamp('28-Feb-2020'),Timestamp('31-Mar-2020'),Timestamp('31-Mar-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('30-Apr-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('31-May-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()

# 
payment_schedule = sch.payment_schedule(start_date=Timestamp('15-Jan-2020'), 
                          end_date=Timestamp('31-May-2020'),
                          payment_freq='M', 
                          roll_convention='modifiedfollowing', 
                          day_roll=nan,
                          stub='first long',
                          last_stub=nan,
                          first_cpn_end_date=nan,
                          last_cpn_start_date=nan,
                          payment_type='in arrears', 
                          payment_delay=0,
                          cal=nan)
arr = np.array([[Timestamp('15-Jan-2020'),Timestamp('28-Jan-2020'),Timestamp('28-Feb-2020')], # 29-Feb-2020 falls on Saturday, roll to 28-Feb-2020
                [Timestamp('28-Feb-2020'),Timestamp('31-Mar-2020'),Timestamp('31-Mar-2020')], 
                [Timestamp('31-Mar-2020'),Timestamp('30-Apr-2020'),Timestamp('30-Apr-2020')], 
                [Timestamp('30-Apr-2020'),Timestamp('31-May-2020'),Timestamp('31-May-2020')]]) # 31-May-2020 falls on a Saturday, don't roll as input dates are not rolled
assert (payment_schedule == pd.DataFrame(arr,columns=['Start Date','End Date','Payment Date'])).all().all()










