from calendars.calendar import getCalendar
from calendars.calendar import getWeekMask
import pandas as pd
import numpy as np

holidays = getCalendar(['NZD'])
holidays2=pd.Series(holidays.format())

cal = np.busdaycalendar(holidays=pd.Series(holidays.format()))
np.busday_offset('2017-04-17',offsets=0,roll='following',busdaycal=cal)

#%%

x = np.array(cal.to_pydatetime(), dtype=np.datetime64)

cal2 = cal.values.strftime('d-mmm-yyy')

np.datetime64(cal2)



date = pd.date_range('6-Feb-2020', '6-Feb-2020')
date + cal

cal.holidays()

d1 = datetime.strptime('6Feb2020', '%d%b%Y')
d1.date()

from datetime import datetime
d = np.array([np.datetime64(datetime.strptime('6Feb2020', '%d%b%Y')),np.datetime64(datetime.strptime('7Feb2020', '%d%b%Y'))])

np.busday_offset(dates=datetime.strptime('6Feb2020', '%d%b%Y').date(),offsets=0,roll='backward',busdaycal=bdd)

bdd = np.busdaycalendar(holidays=['2020-02-06', '2019-12-31'])


cal = AbstractHolidayCalendar()
cal3 = HolidayCalendarFactory('Cal', cal, holidays)
cal33 = cal3()

cal33.holidays(datetime(2010, 1, 1), datetime(2100, 12, 31))


print(cal.rules)

https://stackoverflow.com/questions/33094297/create-trading-holiday-calendar-with-pandas


