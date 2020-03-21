# Sydney holidays


from datetime import time

from dateutil.relativedelta import MO
from pandas import DateOffset, Timestamp
from pandas.tseries.holiday import (
    Holiday,
    GoodFriday,
    EasterMonday,
    previous_friday,
    sunday_to_monday,
    weekend_to_monday,
)
from pytz import timezone
from pytz import UTC

from common_holidays import (
    new_years_day,
    anzac_day,
    christmas,
    weekend_christmas,
    boxing_day,
    weekend_boxing_day,
)

NewYearsDay = new_years_day(observance=weekend_to_monday)

AustraliaDay = Holiday(
    'Australia Day',
    month=1,
    day=26,
    observance=weekend_to_monday,
)

# Anzac Day was observed on Monday when it fell on a Sunday in
# 2010 but that does not appear to have been the case previously.
# We'll assume that this will be the behavior from now on.
AnzacDayNonMondayized = anzac_day(end_date='2010')
AnzacDay = anzac_day(observance=sunday_to_monday, start_date='2010')

# When Easter Monday and Anzac Day coincided in 2011, Easter Tuesday was
# also observed as a public holiday. Note that this isn't defined as a
# rule, because it will happen next in 2095 (and then in  2163), and
# there isn't a great way to tell how this will be handled at that point.
EasterTuesday2011AdHoc = Timestamp('2011-04-26', tz=UTC)

QueensBirthday = Holiday(
    "Queen's Birthday",
    month=6,
    day=1,
    offset=[DateOffset(weekday=MO(2))],
)

Christmas = christmas()
WeekendChristmas = weekend_christmas()
BoxingDay = boxing_day()
WeekendBoxingDay = weekend_boxing_day()

def SYD_holidays():
    return [NewYearsDay,
            AustraliaDay,
            GoodFriday,
            EasterMonday,
            AnzacDayNonMondayized,
            AnzacDay,
            QueensBirthday,
            Christmas,
            WeekendChristmas,
            BoxingDay,
            WeekendBoxingDay]




