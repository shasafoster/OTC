"""
Creates object for defining a yield curve
Functions for valuing an Interest Rate Swap off an excel template

@author: ShasaFoster
"""

import os, sys

sys.path.insert(0, '/calendars')
sys.path.insert(0, '/isda_daycounters')

from calendars.calendar import get_calendar
import schedule as sch
import pandas as pd
from pandas import DatetimeIndex
import numpy as np
from scipy.interpolate import CubicSpline


class yield_curve(object):
    def __init__(self, name, curve_date, discount_data, day_count_basis, historical_fixings=None):
        
        def calc_discount_factors(self,t,discount_factors,date_range, bps_shift):
            # Construct the log-discount curve using cubic spline interpolation
            log_discount = CubicSpline(t,-np.log(list(discount_factors)) + bps_shift*t) # basis point shift to the zero curve
            return np.exp(-log_discount(pd.Series(sch.year_fraction(self.curve_date,date_range,self.day_count_basis)))) 
        
        # Store the defining terms of the curve
        self.name = name
        self.curve_date = curve_date
        self.discount_data = discount_data
        self.day_count_basis = day_count_basis
        
        # Calculate the time in years from the curve_date to the relevant dates of discount factors
        d = DatetimeIndex(discount_data.keys())
        t = np.array(sch.year_fraction(DatetimeIndex([curve_date for _ in range(len(d))]),d,day_count_basis))
        # Dates to precalc discount factors for
        date_range = pd.date_range(self.curve_date,pd.Timestamp('2059-12-31'),freq='d')
        
        discount_factors = calc_discount_factors(self,
                                                 t=t,
                                                 discount_factors=discount_data.values(),
                                                 date_range=date_range,
                                                 bps_shift=0)
        self.discount_factors_base = pd.DataFrame({'Dates': date_range, 'DiscountFactors': discount_factors})
        
        discount_factors = calc_discount_factors(self,
                                                 t=t,
                                                 discount_factors=discount_data.values(),
                                                 date_range=date_range,
                                                 bps_shift=1/100/100)
        self.discount_factors_upshift = pd.DataFrame({'Dates': date_range, 'DiscountFactors': discount_factors})
        
        discount_factors = calc_discount_factors(self,
                                                 t=t,
                                                 discount_factors=discount_data.values(),
                                                 date_range=date_range,
                                                 bps_shift=-1/100/100)
        self.discount_factors_downshift = pd.DataFrame({'Dates': date_range, 'DiscountFactors': discount_factors})
        
        self.discount_factors = self.discount_factors_base

        if historical_fixings is not None:
            self.historical_fixings = historical_fixings

    def upshift(self):
        self.discount_factors = self.discount_factors_upshift

    def downshift(self):
        self.discount_factors = self.discount_factors_downshift
        
    def reset(self):
        self.discount_factors = self.discount_factors_base
        
    def get_dcf(self, dates):
        return pd.Series(list(self.discount_factors.loc[self.discount_factors['Dates'].isin(dates),'DiscountFactors']))
        
    
def isin(tmp, nb, k):
    col_name = 'LEG' + str(nb) + k
    if col_name in tmp.index:
        return tmp[col_name]
    else:
        return np.nan


def fixed_leg(df, payer_receiver, notional, fixed_rate, dsc_curve, day_count_basis, dirty_flag=True): 
    
    # Dirty valuation, include interest accrued before valuation date
    if dirty_flag:
        d1 = pd.DatetimeIndex(df['Start Date'])
        d2 = pd.DatetimeIndex(df['End Date'])
        df['Days'] = sch.day_count(d1, d2, day_count_basis)
        df['Year Fraction'] = sch.year_fraction(d1, d2, day_count_basis)
    # Clean valuation, exclude interest accrued before valuation date
    else: 
        tmp = df['Start Date'].copy()
        tmp[tmp<dsc_curve.curve_date] = dsc_curve.curve_date
        d1 = pd.DatetimeIndex(tmp)
        d2 = pd.DatetimeIndex(df['End Date'])
        df['Days'] = sch.day_count(d1, d2, day_count_basis)
        df['Year Fraction'] = sch.year_fraction(d1, d2, day_count_basis)
        
    df['Fixed Rate'] = fixed_rate / 100.0
    df['Notional'] = notional
    df['Cash Flow'] = df['Notional'] * df['Fixed Rate'] * df['Year Fraction'] * payer_receiver
    df['Discount Factor'] = dsc_curve.get_dcf(DatetimeIndex(df['Payment Date']))
    df.loc[df['Payment Date'] == dsc_curve.curve_date,'Discount Factor'] = 0.0
    df['Cash Flow PV'] = df['Cash Flow'] * df['Discount Factor']
    return df


def get_fwd_rates(d1, d2, fwd_curve, cal, roll_conv):

    # Get historical fixings
    historical_dates = d1[d1 <= fwd_curve.curve_date]
    historical_fixings = []
    historical_fixing_dates = []
    for i,d in enumerate(historical_dates):
        if d in fwd_curve.historical_fixings.keys():
            historical_fixings.append(fwd_curve.historical_fixings[d]/100.0)
            historical_fixing_dates.append(d)
        else:
            j = 1 
            while j < 10:
                d = DatetimeIndex([d])
                d = pd.Timestamp(np.busday_offset(dates=d.astype(str), offsets=j, roll=roll_conv, busdaycal=cal)[0])
                if d in fwd_curve.historical_fixings.keys():
                    historical_fixings.append(fwd_curve.historical_fixings[d]/100.0)
                    historical_fixing_dates.append(d)
                    break
                j += 1
                
    # Calculate future fixings
    d2 = d2[d1 > fwd_curve.curve_date]
    d1 = d1[d1 > fwd_curve.curve_date]
    t = pd.Series(sch.year_fraction(d1,d2,fwd_curve.day_count_basis))
    future_fixings = list((1 / t) * (fwd_curve.get_dcf(d1) / fwd_curve.get_dcf(d2) - 1))

    return pd.Series(historical_fixing_dates + d1.to_list()), pd.Series(historical_fixings + future_fixings)
	
            
def float_leg(df, payer_receiver, notional, spread, dsc_curve, fwd_curve, cal, day_count_basis, dirty_flag=True, roll_conv='modifiedfollowing'):
    
    # Dirty valuation, include interest accrued before valuation date
    if dirty_flag:
        d1 = pd.DatetimeIndex(df['Start Date'])
        d2 = pd.DatetimeIndex(df['End Date'])
        df['Days'] = sch.day_count(d1, d2, day_count_basis)
        df['Year Fraction'] = sch.year_fraction(d1, d2, day_count_basis)
    # Clean valuation, exclude interest accrued before valuation date
    else: 
        tmp = df['Start Date'].copy()
        tmp[tmp<dsc_curve.curve_date] = dsc_curve.curve_date
        d1 = pd.DatetimeIndex(tmp)
        d2 = pd.DatetimeIndex(df['End Date'])
        df['Days'] = sch.day_count(d1, d2, day_count_basis)
        df['Year Fraction'] = sch.year_fraction(d1, d2, day_count_basis)
        
    df['Notional'] = notional
    fixing_dates, fixings = get_fwd_rates(DatetimeIndex(df['Start Date']),DatetimeIndex(df['End Date']),fwd_curve,cal,roll_conv)
     
    df['Fixing Date'] = fixing_dates
    df['Index Rate'] = fixings
    df['Spread'] = spread / 10000.0
    df['Floating Rate'] = df['Index Rate'] + df.Spread
    df['Cash Flow'] = notional * df['Floating Rate'] * df['Year Fraction'] * payer_receiver
    df['Discount Factor'] = dsc_curve.get_dcf(DatetimeIndex(df['Payment Date']))
    df.loc[df['Payment Date'] == dsc_curve.curve_date,'Discount Factor'] = 0.0
    df['Cash Flow PV'] = df['Cash Flow'] * df['Discount Factor']	
    
    return df


def get_dsc_curve(curves, curve_terms, row):  
    if row['InstrumentType'] in ['Vanilla Swap','OIS','ZeroCoupon']:
        curve_type = row['Collateralization/DiscountingMethod'].upper()
        
        if curve_type == 'OIS': 
            CCY = row['CollateralizationCurrency']
            tmp = curve_terms.loc[np.logical_and(curve_terms['Currency']==CCY, curve_terms['CurveType']==curve_type)]
            index = tmp['Index'].iloc[0]
            return curves[CCY + ' ' + index]
        elif curve_type == 'LIBOR' or curve_type == '':
            assert row['InstrumentType'] != 'OIS'
            CCY = row['Currency']
            tmp = curve_terms.loc[np.logical_and(curve_terms['Currency']==CCY, curve_terms['CurveType']==curve_type)]
            index = tmp['Index'].iloc[0]
            print(CCY + ' ' + index + ' ' + tmp['Base Tenor'].iloc[0])
            return curves[CCY + ' ' + index + ' ' + tmp['Base Tenor'].iloc[0]]
        else: 
            raise ValueError("curve_type: ", curve_type)


def get_fwd_curve(curves, curve_terms, row, i):
    CCY = row['Currency']
    tmp = curve_terms.loc[np.logical_and(curve_terms['Currency']==CCY, curve_terms['CurveType']=='LIBOR')]
    index = tmp['Index'].iloc[0]
    tenor = freq2tenor[row['LEG' + str(i) + 'FixingFrequency']]
    return curves[CCY + ' ' + index + ' ' + tenor]


def FixedLeg(tmp, nb, curves, curve_terms, cal=np.nan):
    
    ccy              = tmp['Currency']
    payer_receiver   = isin(tmp,nb,'PayerReceiver')
    start_date       = isin(tmp,nb,'StartDate')
    end_date         = isin(tmp,nb,'EndDate')
    notional         = isin(tmp,nb,'Notional')
    fixed_rate       = isin(tmp,nb,'FixedRate')
    day_count_basis  = isin(tmp,nb,'DayCountBasis')
    payment_freq     = isin(tmp,nb,'PaymentFrequency')
    day_roll         = isin(tmp,nb,'DayRoll')
    roll_convention  = isin(tmp,nb,'RollConv')
    payment_type     = isin(tmp,nb,'PaymentType')
    payment_delay    = isin(tmp,nb,'PaymentDelay')
    holidays         = isin(tmp,nb,'Holidays')
    stub             = isin(tmp,nb,'Stub')
    last_stub        = isin(tmp,nb,'LastStub')
    first_cpn_end_date  = isin(tmp,nb,'FirstCpnEndDate')
    last_cpn_start_date = isin(tmp,nb,'LastCpnStartDate')
    
    if payer_receiver.upper() == 'P':
        payer_receiver = -1 
    elif payer_receiver.upper() == 'R':
        payer_receiver = 1
    else: 
        raise ValueError
    
    dsc_curve = get_dsc_curve(curves, curve_terms, tmp)
        
    if cal is np.nan:
        cal = get_calendar([ccy], holidays) 
        
    payment_schedule = sch.payment_schedule(start_date=start_date, 
                              end_date=end_date,
                              payment_freq=payment_freq, 
                              roll_convention=roll_convention, 
                              day_roll=day_roll,
                              stub=stub,
                              last_stub=last_stub,
                              first_cpn_end_date=first_cpn_end_date,
                              last_cpn_start_date=last_cpn_start_date,
                              payment_type=payment_type, 
                              payment_delay=payment_delay,
                              cal=cal)
    
    payment_schedule = payment_schedule[payment_schedule['End Date']  >= dsc_curve.curve_date]
    payment_schedule.reset_index(drop=True, inplace=True)

    cashflow_schedule = fixed_leg(payment_schedule.copy(), payer_receiver, notional, fixed_rate, dsc_curve, day_count_basis).copy()  
    #legPV_clean = fixed_leg(payment_schedule, payer_receiver, notional, fixed_rate, dsc_curve, day_count_basis, dirty_flag=True).copy()  
    
    dsc_curve.upshift()
    legPV_upshift = fixed_leg(payment_schedule, payer_receiver, notional, fixed_rate, dsc_curve, day_count_basis)['Cash Flow PV'].sum()
    dsc_curve.downshift() 
    legPV_downshift = fixed_leg(payment_schedule, payer_receiver, notional, fixed_rate, dsc_curve, day_count_basis)['Cash Flow PV'].sum()
    dsc_curve.reset()
    leg_DV01 = (legPV_upshift - legPV_downshift) / 20.0
    
    return cashflow_schedule , leg_DV01, payment_schedule


def FloatLeg(tmp, nb, curves, curve_terms, cal=np.nan):

    ccy              = tmp['Currency']
    payer_receiver   = isin(tmp,nb,'PayerReceiver')
    start_date       = isin(tmp,nb,'StartDate')
    end_date         = isin(tmp,nb,'EndDate')
    notional         = isin(tmp,nb,'Notional')
    spread           = isin(tmp,nb,'Spread')
    day_count_basis  = isin(tmp,nb,'DayCountBasis')
    payment_freq     = isin(tmp,nb,'PaymentFrequency')
    day_roll         = isin(tmp,nb,'DayRoll')
    roll_convention  = isin(tmp,nb,'RollConv')
    payment_type     = isin(tmp,nb,'PaymentType')
    payment_delay    = isin(tmp,nb,'PaymentDelay')
    holidays         = isin(tmp,nb,'Holidays')
    stub             = isin(tmp,nb,'Stub')
    last_stub        = isin(tmp,nb,'LastStub')
    first_cpn_end_date  = isin(tmp,nb,'FirstCpnEndDate')
    last_cpn_start_date = isin(tmp,nb,'LastCpnStartDate')

    if payer_receiver.upper() == 'P':
        payer_receiver = -1 
    elif payer_receiver.upper() == 'R':
        payer_receiver = 1
    else: 
        raise ValueError(payer_receiver)

    fwd_curve = get_fwd_curve(curves, curve_terms, tmp, nb)
    dsc_curve = get_dsc_curve(curves, curve_terms, tmp)

    if cal is np.nan:
        cal = get_calendar([ccy], holidays) 

    payment_schedule = sch.payment_schedule(start_date=start_date, 
                              end_date=end_date,
                              payment_freq=payment_freq, 
                              roll_convention=roll_convention, 
                              day_roll=day_roll,
                              stub=stub,
                              last_stub=last_stub,
                              first_cpn_end_date=first_cpn_end_date,
                              last_cpn_start_date=last_cpn_start_date,
                              payment_type=payment_type, 
                              payment_delay=payment_delay,
                              cal=cal)

    # Only get future dates
    payment_schedule = payment_schedule[payment_schedule['End Date']  >= dsc_curve.curve_date]
    payment_schedule.reset_index(drop=True, inplace=True)

    cashflow_schedule = float_leg(payment_schedule, payer_receiver, notional, spread, dsc_curve, fwd_curve, cal, day_count_basis).copy()
    #legPV_clean = float_leg(payment_schedule.copy(), payer_receiver, notional, spread, dsc_curve, fwd_curve, cal, day_count_basis, dirty_flag=True)['Cash Flow PV'].copy()
    dsc_curve.upshift()
    fwd_curve.upshift()
    
    legPV_upshift = float_leg(payment_schedule, payer_receiver, notional, spread, dsc_curve, fwd_curve, cal, day_count_basis)['Cash Flow PV'].sum()
    dsc_curve.downshift()
    fwd_curve.downshift() 
    
    legPV_downshift = float_leg(payment_schedule, payer_receiver, notional, spread, dsc_curve, fwd_curve, cal, day_count_basis)['Cash Flow PV'].sum()
    fwd_curve.reset()
    dsc_curve.reset()
    leg_DV01 = (legPV_upshift - legPV_downshift) / 2.0
    return cashflow_schedule , leg_DV01, payment_schedule

freq2tenor = {'M':'1M','Q':'3M','S':'6M','A':'12M'}