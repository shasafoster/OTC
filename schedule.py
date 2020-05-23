"""
Creates a payment schedule

@author: ShasaFoster
"""

import numpy as np
from numpy import busday_offset, nan, busdaycalendar
from pandas import DateOffset, DatetimeIndex
import pandas as pd
import os, sys
from datetime import datetime
import time

sys.path.insert(0, '/calendars')
sys.path.insert(0, '/isda_daycounters')

from calendars.calendar import get_calendar
from isda_daycounters import actual360, actualactual, actual365, thirty360, thirtyE360, thirtyE360ISDA


def year_fraction(start_date,end_date,day_count_basis):
    """Return the year fraction between the start_date and end_date per the day_count_basis."""
    if day_count_basis == 'ACT/ACT': 
        return actualactual.year_fraction(start_date,end_date)
    elif day_count_basis == 'ACT/360': 
        return actual360.year_fraction(start_date,end_date)
    elif day_count_basis == 'ACT/365': 
        return actual365.year_fraction(start_date,end_date)
    elif day_count_basis == '30/360': 
        return thirty360.year_fraction(start_date,end_date)
    elif day_count_basis == '30E/360': 
        return thirtyE360.year_fraction(start_date,end_date)
    elif day_count_basis == '30E/360 ISDA': 
        return thirtyE360ISDA.year_fraction(start_date,end_date)
    else: raise ValueError('Day count basis value "' + str(day_count_basis) + '" is invalid')
    
    
def day_count(start_date,end_date,day_count_basis):
    """Return the number of days between the start_date and end_date per the day_count_basis."""
    if day_count_basis == 'ACT/ACT': 
        return actualactual.day_count(start_date,end_date)
    elif day_count_basis == 'ACT/360': 
        return actual360.day_count(start_date,end_date)
    elif day_count_basis == 'ACT/365': 
        return actual365.day_count(start_date,end_date)
    elif day_count_basis == '30/360': 
        return thirty360.day_count(start_date,end_date)
    elif day_count_basis == '30E/360': 
        return thirtyE360.day_count(start_date,end_date)
    elif day_count_basis == '30E/360 ISDA': 
        return thirtyE360ISDA.day_count(start_date,end_date)
    else: raise ValueError('Day count basis value "' + str(day_count_basis) + '" is invalid')


def roll_dates(dates, day_roll):
    """Roll the days of the dates to the provided day_roll."""
    print('Heloeasuhtoes',day_roll)
    if str(day_roll).lower() == 'eom' or day_roll == 31:
        return dates + pd.offsets.MonthEnd(0)
    elif day_roll < 29:
        return DatetimeIndex([datetime(d.year,d.month,int(day_roll)) for d in dates])
    else:
        rolled = []
        for d in dates:
            try:
                rolled.append(datetime(d.year,d.month,int(day_roll)))
            except ValueError:
                rolled.append(d + pd.offsets.MonthEnd(0))
        return DatetimeIndex(rolled)     


def nb_months_per_period(freq):
    """Return the number of month in a given yearly frequency."""
    if freq == 'M': return 1
    elif freq == 'Q': return 3
    elif freq == 'S': return 6
    elif freq == 'A': return 12
    else: raise ValueError('Frequency value "' + str(freq) + '" is invalid')
                         

def payment_schedule(start_date,
                     end_date,
                     payment_freq,
                     roll_convention='modifiedfollowing',
                     day_roll=nan,
                     stub='first short',
                     last_stub=nan,
                     first_cpn_end_date=nan,
                     last_cpn_start_date=nan,
                     payment_type='in arrears', 
                     payment_delay=0,
                     ccys=nan,
                     holidays=nan,
                     cal=nan):
    """
    Create a payment schedule.

    Parameters
    ----------
    start_date : pandas.Timestamp
        Specifies the effective date of the schedule
    end_date : pandas.Timestamp
        Specifies the expiration date of the schedule
    payment_freq : {'M', 'Q', 'S', 'A'}
        Specify the payment frequency
    day_count_basis : {'ACT/ACT','ACT/360','ACT/365', '30/360', '30E/360', '30E/350 ISDA'}
    roll_convention : {'actual','following','preceding','modifiedfollowing','modifiedpreceding'},
        How to treat dates that do not fall on a valid day. The default is ‘raise’.
            'following' means to take the first valid day later in time.
            'preceding' means to take the first valid day earlier in time.
            'modifiedfollowing' means to take the first valid day later in time unless it is across a Month boundary, in which case to take the first valid day earlier in time.
            'modifiedpreceding' means to take the first valid day earlier in time unless it is across a Month boundary, in which case to take the first valid day later in time.
    stub : {'first short','first long','last short','last long'}
        Specify the type and location of stub period
    last_stub : {short, long}
        Specifies the type of the last stub
    payment_type : {'in arrears','in advance'}
        Specifies when payments are made
    payment_delay : int
        Specifies how many days after period end the payment is made
    day_roll : {1,2,3,...,30,31,'EoM'}
        Specifies the day periods should start/end on, EoM = roll to the end of month
    ccy : array of strings of three letter currency codes
    holidays : array of strings {'Amsterdam','AMS',
                                 'Copenhagen','COP','DKK',
                                 'Helsinki','HEL',
                                 'Istanbul','IST','TRY',
                                 'Johannesburg','JOH','ZAR',
                                 'Lima','LIM','PEN',
                                 'Lisbon','LIS',
                                 'London','LON','GBP',
                                 'Madrid','MAD',
                                 'Moscow','MOS','RUB',
                                 'New York','NY','USD',
                                 'Oslo','OSL','NOK',
                                 'Prague','PRA','CZK',
                                 'San Paulo','SAN','BRL',
                                 'Stockholm','STO','SEK',
                                 'Sydney','SYD','AUD',
                                 'Tokyo','TKY','JPY',
                                 'Toronto','TOR','CAD',
                                 'Vienna','VIE',
                                 'Wellington','WEL','NZD',
                                 'Zurich','ZUR','CHF'}
        Specifies the holidays of the countrys and financial centres to be observed
    cal : numpy.busdaycalendar 
        Specifies the holiday calendar to observe. If this parameter is provided, neither ccy or holidays may be provided
        
    Returns
    -------
    schedule : pandas.DataFrame
        Columns
            start_date - start dates of the periods
            end_date - end dates of the periods
            year_fraction - year fraction between period start and end days per the day_count_basis
    """
    
    print_ = False
    def printt(v):
        if print_:
            print(v)

    
    if pd.isnull(roll_convention): roll_convention = 'modifiedfollowing'
    if pd.isnull(payment_type): payment_type = 'in arrears'
    if pd.isnull(payment_delay): payment_delay = 0
    
    payment_freq = payment_freq.upper()
    #day_count_basis = day_count_basis.upper()
    roll_convention = roll_convention.lower()
    payment_type = payment_type.lower()
    
    assert payment_freq in {'M','Q','S','A'}, payment_freq
    assert roll_convention in {'actual','following','preceding','modifiedfollowing','modifiedpreceding'}, roll_convention
    if not pd.isnull(stub): 
        stub = stub.lower()
        assert stub in {'first short','first long','last short','last long'}, stub
    if not pd.isnull(last_stub): 
        last_stub = last_stub.lower()
        assert last_stub in {'short','long'}, last_stub
    assert payment_type in {'in arrears','in advance'}, payment_type

    nb_months  = nb_months_per_period(payment_freq)
    
    if pd.isnull(cal):
        cal = get_calendar(ccys, holidays) 
    
    first_cpn_end_date_isnull = pd.isnull(first_cpn_end_date)
    last_cpn_start_date_isnull = pd.isnull(last_cpn_start_date)
    
    if not first_cpn_end_date_isnull:
        # The expected first coupon end date if no stub
        expected_first_cpn_end_date = pd.Timestamp(busday_offset(dates=DatetimeIndex([start_date - date_offset(nb_months)]).astype(str), offsets=0, roll=roll_convention, busdaycal=cal)[0])
    if not last_cpn_start_date_isnull:
        # The expected last coupon start date if no stub
        expected_last_cpn_start_date = pd.Timestamp(busday_offset(dates=DatetimeIndex([end_date - date_offset(nb_months)]).astype(str), offsets=0, roll=roll_convention, busdaycal=cal)[0])

    # If the schedule terms specifiy 1 period
    if (not first_cpn_end_date_isnull and first_cpn_end_date == end_date) or (not last_cpn_start_date_isnull and last_cpn_start_date == start_date):
        d1 = [start_date]
        d2 = [end_date]
        
    # If the schedule terms specifiy 2 periods
    elif not first_cpn_end_date_isnull and not last_cpn_start_date_isnull and (first_cpn_end_date == last_cpn_start_date):
        d1 = [start_date, first_cpn_end_date]
        d2 = [last_cpn_start_date, end_date]
        
    # Otherwise, calculate the schedule dates
    else:
        # If the trade has a maximum of one stub or if the first_cpn_end_date or first_cpn_end_date is specified, 
        # the date is where we expect it to be without a stub
        if (first_cpn_end_date_isnull and last_cpn_start_date_isnull) \
            or (not first_cpn_end_date_isnull and first_cpn_end_date == expected_first_cpn_end_date) \
            or (not last_cpn_start_date_isnull and last_cpn_start_date == expected_last_cpn_start_date):
            printt('0')
                
            # Use a first short stub if:
            # 1) specified
            # 2) no stub parameters (stub, last_stub, first_cpn_end_date, last_cpn_start_date) where provided
            # 3) the last_cpn_start_date is in the expected position if there is no last stub
            if stub == 'first short' or (pd.isnull(stub) and pd.isnull(last_stub)) \
                or (not last_cpn_start_date_isnull and last_cpn_start_date == expected_last_cpn_start_date):
                d1,d2 = backward_date_generation(start_date, end_date, nb_months)       
                printt('1')                                            
        
            # Use a last short stub if:
            # 1) specified
            # 2) the first_cpn_end_date is in the expected position if there is no first stub
            elif stub =='last short' or last_stub == 'short' \
                or (not first_cpn_end_date_isnull and first_cpn_end_date == expected_first_cpn_end_date):
                d1,d2 = forward_date_generation(start_date, end_date, nb_months) 
                printt('2')
            
            # Use a first long stub only when specified
            elif stub == 'first long':
                d1,d2 = backward_date_generation(start_date, end_date, nb_months) 
                d1 = [d1[0]] + d1[2:]
                d2 = d2[1:]
                printt('3')
            
            # Use a last long stub only when specified
            elif stub == 'last long' or last_stub == 'long':
                d1,d2 = forward_date_generation(start_date, end_date, nb_months) 
                d1 = d1[:-1]  
                d2 = d2[:-2] + [d2[-1]]
                printt('4')
            
            else: 
                raise ValueError('stub value"' + str(stub) + '" is invalid')    
          
        # If there is a stub at both the start and end
        elif not first_cpn_end_date_isnull and not last_cpn_start_date_isnull:
            d1,d2 = forward_date_generation(first_cpn_end_date, last_cpn_start_date, nb_months) 
            d1 = [start_date] + d1 + [last_cpn_start_date]
            d2 = [first_cpn_end_date] + d2 + [end_date]
            printt('5')
            
        # dates will need to be rolled to the start date day
        elif first_cpn_end_date_isnull and not last_cpn_start_date_isnull:
            d1,d2 = backward_date_generation(start_date, last_cpn_start_date, nb_months) 
            d1 = d1 + [last_cpn_start_date]
            d2 = d2 + [end_date]
            printt('6')
            
        # dates will need to be rolled to the end date day
        elif not first_cpn_end_date_isnull and last_cpn_start_date_isnull:
            d1,d2 = forward_date_generation(first_cpn_end_date, end_date, nb_months) 
            d1 = [start_date] + d1
            d2 = [first_cpn_end_date] + d2
            print('7')
              
        d1 = DatetimeIndex(d1)
        d2 = DatetimeIndex(d2)
              
        if not pd.isnull(day_roll):
            print(day_roll)
            d1 = roll_dates(d1, day_roll)
            d2 = roll_dates(d2, day_roll)
        
        if roll_convention != 'actual':
            # Roll the days of the schedule per the roll convention and business day holiday calendar
            d1 = DatetimeIndex(busday_offset(dates=d1.astype(str), offsets=0, roll=roll_convention, busdaycal=cal))
            d2 = DatetimeIndex(busday_offset(dates=d2.astype(str), offsets=0, roll=roll_convention, busdaycal=cal))

        # Use the dates specified in the function call (start_date, end_date, first_cpn_end_date, last_cpn_end_date) 
        # in the schedule, regardless if they fall on a non-business day. 
        d1 = d1.to_list()
        d2 = d2.to_list()
        if not first_cpn_end_date_isnull and not last_cpn_start_date_isnull:
            d1 = [start_date] + [first_cpn_end_date] + d1[2:-1] + [last_cpn_start_date]
            d2 = [first_cpn_end_date] + d2[1:-2] + [last_cpn_start_date] + [end_date]
        elif first_cpn_end_date_isnull and not last_cpn_start_date_isnull:
            d1 = [start_date] + d1[1:-1] + [last_cpn_start_date]
            d2 = d2[:-2] + [last_cpn_start_date] + [end_date]        
        elif not first_cpn_end_date_isnull and last_cpn_start_date_isnull:
            d1 = [start_date] + [first_cpn_end_date] + d1[2:]
            d2 = [first_cpn_end_date] + d2[1:-1] + [end_date]
        else: 
            d1 = [start_date] + d1[1:]
            d2 = d2[:-1] + [end_date]
                
    df = pd.DataFrame({'Start Date': d1, 'End Date': d2})
    df = df[df['Start Date'] != df['End Date']]
    df.reset_index(drop=True,inplace=True)

    # Add the payment date
    if payment_type == 'in arrears':
        if payment_delay == 0:
            df['Payment Date'] = df['End Date']
        else:
            df['Payment Date'] = busday_offset(DatetimeIndex(df['End Date']+DateOffset(days=payment_delay)).astype(str), offsets=0, roll='following', busdaycal=cal)
    elif payment_type == 'in advance':
        if payment_delay == 0:
            df['Payment Date'] = df['Start Date'] 
        else:
            df['Payment Date'] = busday_offset(DatetimeIndex(df['Start Date']+DateOffset(days=payment_delay)).astype(str), offsets=0, roll='following', busdaycal=cal)
    else:
        raise ValueError('payment_type value"' + str(payment_type) + '" is invalid')   

    return df


def forward_date_generation(start_date, end_date, nb_periods, period_type='months'):
    """
    Generates a schedule working forwards from start date to the end date

    Parameters
    ----------
    start_date : pd.Timestamp
        start date of the schedule
    end_date : pd.Timestamp
        end date of the schedule
    nb_periods : Integer
        Specifies the number of periods of length 'period_type' per time increment
    period_type : {'months','years','weeks','days'}, optional
        Specifies the length of a period. The default is 'months'.

    Returns
    -------
    tuble of lists
        start dates, end dates
    """

    d1_arr = []
    d2_arr = []
    d1 = start_date
    d2 = start_date + date_offset(nb_periods,period_type)
    i = 1

    while end_date > d2 :   
        d1_arr.append(d1)
        d2_arr.append(d2)
        d1 = start_date + date_offset(nb_periods*i,period_type) 
        d2 = start_date + date_offset(nb_periods*(i+1),period_type) 
        i = i + 1
    d1_arr.append(d1)
    d2_arr.append(end_date)

    return d1_arr,d2_arr


def backward_date_generation(start_date, end_date, nb_periods, period_type='months'):
    """
    Generates a schedule working backwards from the end date to the start date

    Parameters
    ----------
    start_date : pd.Timestamp
        start date of the schedule
    end_date : pd.Timestamp
        end date of the schedule
    nb_periods : Integer
        Specifies the number of periods of length 'period_type' per time decrement
    period_type : {'months','years','weeks','days'}, optional
        Specifies the length of a period. The default is 'months'.

    Returns
    -------
    tuble of lists
        start dates, end dates
    """
    
    d1_arr = []
    d2_arr = []
    d1 = end_date - date_offset(nb_periods,period_type)
    d2 = end_date
    i = 1
    while start_date < d1:   
        d1_arr.append(d1)
        d2_arr.append(d2)
        d1 = end_date - date_offset(nb_periods*(i+1),period_type) 
        d2 = end_date - date_offset(nb_periods*i,period_type) 
        i = i + 1
    d1_arr.append(start_date)
    d2_arr.append(d2)

    return list(reversed(d1_arr)),list(reversed(d2_arr))


def date_offset(nb_periods, period_type='months'):
    if period_type == 'months':
        return DateOffset(months=nb_periods)
    elif period_type == 'years':
        return DateOffset(years=nb_periods)
    elif period_type == 'weeks': 
        return DateOffset(weeks=nb_periods)
    elif period_type == 'days':
        return DateOffset(days=nb_periods)


