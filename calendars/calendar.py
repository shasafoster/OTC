from numpy import busdaycalendar, nan
from pandas.tseries.holiday import HolidayCalendarFactory, AbstractHolidayCalendar, Series
from datetime import datetime
import pandas as pd

from calendars import amsterdam,copenhagen,helsinki, istanbul,johannesburg,lima,lisbon,london,madrid,moscow,new_york,oslo,prague,san_paulo,stockholm,sydney,tokyo,toronto,vienna,wellington,zurich

map_citycode_to_holidays = {
    'amsterdam'    : amsterdam.holidays(),
    'ams'          : amsterdam.holidays(),
    'copenhagen'   : copenhagen.holidays(),
    'cop'          : copenhagen.holidays(),
    'helsinki'     : helsinki.holidays(),
    'hel'          : helsinki.holidays(),
    'istanbul'     : istanbul.holidays(),
    'ist'          : istanbul.holidays(),
    'johannesburg' : johannesburg.holidays(),
    'joh'          : johannesburg.holidays(),
    'lima'         : lima.holidays(),
    'lim'          : lima.holidays(),
    'lisbon'       : lisbon.holidays(),
    'lis'          : lisbon.holidays(),
    'london'       : london.holidays(),
    'lon'          : london.holidays(),
    'Madrid'       : madrid.holidays(),
    'mad'          : madrid.holidays(),
    'Moscow'       : moscow.holidays(),
    'mos'          : moscow.holidays(),
    'new york'     : new_york.holidays(),
    'ny'           : new_york.holidays(),
    'oslo'         : oslo.holidays(),
    'osl'          : oslo.holidays(),
    'prague'       : prague.holidays(),
    'pra'          : prague.holidays(),
    'san paulo'    : san_paulo.holidays(),
    'san'          : san_paulo.holidays(),
    'stockholm'    : stockholm.holidays(),
    'sto'          : stockholm.holidays(),
    'sydney'       : sydney.holidays(),
    'syd'          : sydney.holidays(),
    'Tokyo'        : tokyo.holidays(),
    'tky'          : tokyo.holidays(),
    'toronto'      : toronto.holidays(),
    'tor'          : toronto.holidays(),
    'vienna'       : vienna.holidays(),
    'vie'          : vienna.holidays(),
    'wellington'   : wellington.holidays(),
    'wel'          : wellington.holidays(),
    'zurich'       : zurich.holidays(),
    'zur'          : zurich.holidays(),
    }

map_ccy_to_holidays = {
    'DKK'          : copenhagen.holidays(),
    'TRY'          : istanbul.holidays(),
    'ZAR'          : johannesburg.holidays(),
    'PEN'          : lima.holidays(),
    'GBP'          : london.holidays(),
    'RUB'          : moscow.holidays(),
    'USD'          : new_york.holidays(),
    'NOK'          : oslo.holidays(),
    'CZK'          : prague.holidays(),
    'BRL'          : san_paulo.holidays(),
    'SEK'          : stockholm.holidays(),
    'AUD'          : sydney.holidays(),
    'JPY'          : tokyo.holidays(),
    'CAD'          : toronto.holidays(),
    'NZD'          : wellington.holidays(),
    'CHF'          : zurich.holidays()
    }


def get_calendar(ccys, cities=nan):
    """
    Create a calendar which has the holidays and business of the curriences and city inputs.

    Parameters
    ----------
    cities : array of strings, optional
        DESCRIPTION. Array of three letter (financial) city codes, The default is None.

    Returns
    -------
    CustomBusinessDay() object, observing the holiday of the cities
    
    """
    
    if pd.isnull(ccys) and pd.isnull(cities):
        return busdaycalendar()
    
    # Muslim/Jewish states have Friday & Sunday as the weekend
    weekmask = getWeekMask(ccys)

    holidays = []
    if cities is not nan:
        holidays += [map_citycode_to_holidays[c] for c in cities if c in map_citycode_to_holidays.keys()]
    holidays += [map_ccy_to_holidays[c] for c in ccys if c in map_ccy_to_holidays.keys()]
    # Flattan the list of lists
    holidays = [h for city_holidays in holidays for h in city_holidays]    
    if holidays == []:
        return busdaycalendar(weekmask=weekmask)
    else:
        cal = HolidayCalendarFactory('Cal', AbstractHolidayCalendar(), holidays)
        cal_instance = cal()
        holidays = cal_instance.holidays(datetime(2000, 1, 1), datetime(2100, 1, 1))
        return busdaycalendar(holidays=Series(holidays.format()))
        
    
def getWeekMask(ccys):
    """
    Return the business days of the countries associated with the provided currencies.
    
    Muslim/Jewish states have have Friday & Sunday as the weekend.
    Specifically, Israel, United Arab Emrites, Egypt, Saudi Arabia, Qatar, Iraq, Iran have Friday & Sunday as the weekend
    
    Parameters
    ----------
    ccys : numpy array of strings
        array of three letter currency codes 
        
    Returns
    -------
    The business days consistent across all currencies 
    
    """
    fri_sat_weekend = set(['ILS', # Israeli
                           'AED', # UAE
                           'EGP', # Egpyt
                           'SAR', # Saudi Arabia
                           'QAR', # Qatar
                           'IQD', # Iraq
                           'IRR' # Iran
                           ])

    bool_arr = [ccy in fri_sat_weekend for ccy in ccys]
    
    if True in bool_arr and False in bool_arr:
        return 'Mon Tue Wed Thu'
    elif False in bool_arr:
        return 'Mon Tue Wed Thu Fri'
    else:
        return 'Sun Mon Tue Wed Thu'





