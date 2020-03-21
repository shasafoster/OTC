import pandas as pd
import numpy as np
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime

def isWeekday(dates):
    return ~dates.weekday_name.isin(['Saturday', 'Sunday'])


def inNextMonth(dates1, dates2):
    return np.any([dates1.month == dates2.month - 1,dates1.month - 11 == dates2.month],axis=0) 


def rollFollowing(dates, cal):
    # If date falls on non-business day, roll to the next business day
    return dates.where(isWeekday(dates), dates + cal)


def rollModifiedFollowing(dates, cal):
    # If the next business day not in the next calendar month, roll to the next business day, 
    # Else, roll to the previous business day
    fwd = dates + cal
    adj = fwd.where(~inNextMonth(dates, fwd), dates - cal)
    return dates.where(isWeekday(dates), adj)
         
           
def rollPreceding(dates, cal):
    # If date falls on non-business day, roll to the previous business day
    return dates.where(isWeekday(dates), dates - cal)


def rollModifiedPreceding(dates, cal):
    # If the previous business day not in the previous calendar month, roll to the previous business day, 
    # Else, roll to the next business day
    bwd = dates - cal
    adj = bwd.where(~inNextMonth(bwd, dates), dates + cal)
    return dates.where(isWeekday(dates), adj)


def rollDates(dates, roll_convention='Actual', cal=CustomBusinessDay()):
    """
    Rolls dates if date falls on a non-business day
        
    Parameters
    ----------
    dates : DatetimeIndex
        Dates to roll
    roll_convention : String
        Specifies the date roll convention
    cal : CustomBusinessDay
        Business day calendar to observe
        
    Returns
    -------
    dates : DatetimeIndex
        The `dates` rolled according to the date roll rule and business calendar
    """
    
    if roll_convention == 'Actual': 
        return dates
    elif roll_convention == 'Modified_Following': 
        return rollModifiedFollowing(dates, cal)
    elif roll_convention == 'Following': 
        return rollFollowing(dates, cal)
    elif roll_convention == 'Modified_Preceding': 
        return rollModifiedPreceding(dates, cal)
    elif roll_convention == 'Preceding': 
        return rollPreceding(dates, cal)
    else:
        raise ValueError('"' + roll_convention + '" is an invalid roll_convention value.\
                         Valid roll_convention values include:\
                         Actual, Modified_Following, Following, Modified_Preceding, Preceding')


#%% Tests with Saturday 29 Februay 2020
        
# Fri 28-Feb-2020
# Sat 29-Feb-2020                         
# Sun  1-Mar-2020
# Mon  2-Mar-2020                        
        
date = pd.date_range('02/29/2020', '02/29/2020')
assert rollDates(date,'Actual').to_pydatetime()[0] == datetime(2020, 2, 29) # Day should stay the same 
assert rollDates(date,'Modified_Following').to_pydatetime()[0] == datetime(2020, 2, 28) # Roll to Fri 28-Feb-2020
assert rollDates(date,'Following').to_pydatetime()[0] == datetime(2020, 3, 2) # Roll to Mon 2-Mar-2020
assert rollDates(date,'Modified_Preceding').to_pydatetime()[0] == datetime(2020, 2, 28) # Roll to Fri 28-Feb-2020
assert rollDates(date,'Preceding').to_pydatetime()[0] == datetime(2020, 2, 28) # Roll to Fri 28-Feb-2020


#%% Tests with Sunday 1 March 2020

# Fri 28-Feb-2020
# Sat 29-Feb-2020                         
# Sun  1-Mar-2020
# Mon  2-Mar-2020        
    
date = pd.date_range('03/01/2020', '03/01/2020')
assert rollDates(date,'Actual').to_pydatetime()[0] == datetime(2020, 3, 1) # Day should stay the same 
assert rollDates(date,'Modified_Following').to_pydatetime()[0] == datetime(2020, 3, 2) # Roll to Mon 2-Mar-2020 
assert rollDates(date,'Following').to_pydatetime()[0] == datetime(2020, 3, 2) # Roll to Mon 2-Mar-2020 
assert rollDates(date,'Modified_Preceding').to_pydatetime()[0] == datetime(2020, 3, 2) # Roll to Mon 2-Mar-2020 
assert rollDates(date,'Preceding').to_pydatetime()[0] == datetime(2020, 2, 28) # Roll to Fri-28-Feb-2020

#%% Tests with Saturday 1 August 2020

# Fri 31-Jul-2020
# Sat  1-Aug-2020                    
# Sun  2-Aug-2020
# Mon  3-Aug-2020        
    
date = pd.date_range('08/01/2020', '08/01/2020')
assert rollDates(date,'Actual').to_pydatetime()[0] == datetime(2020, 8, 1) # Day should stay the same 
assert rollDates(date,'Modified_Following').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Following').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Modified_Preceding').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Preceding').to_pydatetime()[0] == datetime(2020, 7, 31) # Roll to Fri 31-Jul-2020


#%% Tests with August 2 August 2020

# Fri 31-Jul-2020
# Sat  1-Aug-2020                    
# Sun  2-Aug-2020
# Mon  3-Aug-2020        
    
date = pd.date_range('08/02/2020', '08/02/2020')
assert rollDates(date,'Actual').to_pydatetime()[0] == datetime(2020, 8, 2) # Day should stay the same 
assert rollDates(date,'Modified_Following').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Following').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Modified_Preceding').to_pydatetime()[0] == datetime(2020, 8, 3) # Roll to Mon 3-Aug-2020 
assert rollDates(date,'Preceding').to_pydatetime()[0] == datetime(2020, 7, 31) # Roll to Fri 31-Jul-2020












