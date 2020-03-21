# New York Stock Exchange Holidays

from dateutil.relativedelta import (MO, TH, TU)
from pandas import (DateOffset, Timestamp, date_range)
from pandas.tseries.holiday import (Holiday, nearest_workday, sunday_to_monday)
from pandas.tseries.offsets import Day
from pandas.tseries.holiday import GoodFriday, USLaborDay
from common_holidays import (FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY)


# These have the same definition, but are used in different places because the
# NYSE closed at 2:00 PM on Christmas Eve until 1993.


def july_5th_holiday_observance(datetime_index):
    return datetime_index[datetime_index.year < 2013]


def following_tuesday_every_four_years_observance(dt):
    return dt + DateOffset(years=(4 - (dt.year % 4)) % 4, weekday=TU(1))


ChristmasEveBefore1993 = Holiday(
    'Christmas Eve',
    month=12,
    day=24,
    end_date=Timestamp('1993-01-01'),
    # When Christmas is a Saturday, the 24th is a full holiday.
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY),
)
ChristmasEveInOrAfter1993 = Holiday(
    'Christmas Eve',
    month=12,
    day=24,
    start_date=Timestamp('1993-01-01'),
    # When Christmas is a Saturday, the 24th is a full holiday.
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY),
)
USNewYearsDay = Holiday(
    'New Years Day',
    month=1,
    day=1,
    # When Jan 1 is a Sunday, US markets observe the subsequent Monday.
    # When Jan 1 is a Saturday (as in 2005 and 2011), no holiday is observed.
    observance=sunday_to_monday
)
USMartinLutherKingJrAfter1998 = Holiday(
    'Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    # The US markets didn't observe MLK day as a holiday until 1998.
    start_date=Timestamp('1998-01-01'),
    offset=DateOffset(weekday=MO(3)),
)
USLincolnsBirthDayBefore1954 = Holiday(
    'Lincoln''s Birthday',
    month=2,
    day=12,
    start_date=Timestamp('1874-01-01'),
    end_date=Timestamp('1953-12-31'),
    observance=sunday_to_monday,
)
USWashingtonsBirthDayBefore1964 = Holiday(
    'Washington''s Birthday',
    month=2,
    day=22,
    start_date=Timestamp('1880-01-01'),
    end_date=Timestamp('1963-12-31'),
    observance=sunday_to_monday,
)
USWashingtonsBirthDay1964to1970 = Holiday(
    'Washington''s Birthday',
    month=2,
    day=22,
    start_date=Timestamp('1964-01-01'),
    end_date=Timestamp('1970-12-31'),
    observance=nearest_workday,
)
USPresidentsDay = Holiday('President''s Day',
                          start_date=Timestamp('1971-01-01'),
                          month=2, day=1,
                          offset=DateOffset(weekday=MO(3)))
# http://www.tradingtheodds.com/nyse-full-day-closings/
USThanksgivingDayBefore1939 = Holiday('Thanksgiving Before 1939',
                                      start_date=Timestamp('1864-01-01'),
                                      end_date=Timestamp('1938-12-31'),
                                      month=11, day=30,
                                      offset=DateOffset(weekday=TH(-1)))
# http://www.tradingtheodds.com/nyse-full-day-closings/
USThanksgivingDay1939to1941 = Holiday('Thanksgiving 1939 to 1941',
                                      start_date=Timestamp('1939-01-01'),
                                      end_date=Timestamp('1941-12-31'),
                                      month=11, day=30,
                                      offset=DateOffset(weekday=TH(-2)))
USThanksgivingDay = Holiday('Thanksgiving',
                            start_date=Timestamp('1942-01-01'),
                            month=11, day=1,
                            offset=DateOffset(weekday=TH(4)))
# http://www.tradingtheodds.com/nyse-full-day-closings/
USMemorialDayBefore1964 = Holiday(
    'Memorial Day',
    month=5,
    day=30,
    end_date=Timestamp('1963-12-31'),
    observance=sunday_to_monday,
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USMemorialDay1964to1969 = Holiday(
    'Memorial Day',
    month=5,
    day=30,
    start_date=Timestamp('1964-01-01'),
    end_date=Timestamp('1969-12-31'),
    observance=nearest_workday,
)
USMemorialDay = Holiday(
    # NOTE: The definition for Memorial Day is incorrect as of pandas 0.16.0.
    # See https://github.com/pydata/pandas/issues/9760.
    'Memorial Day',
    month=5,
    day=25,
    start_date=Timestamp('1971-01-01'),
    offset=DateOffset(weekday=MO(1)),
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USIndependenceDayBefore1954 = Holiday(
    'July 4th',
    month=7,
    day=4,
    end_date=Timestamp('1953-12-31'),
    observance=sunday_to_monday,
)
USIndependenceDay = Holiday(
    'July 4th',
    month=7,
    day=4,
    start_date=Timestamp('1954-01-01'),
    observance=nearest_workday,
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USElectionDay1848to1967 = Holiday(
    'Election Day',
    month=11,
    day=2,
    start_date=Timestamp('1848-1-1'),
    end_date=Timestamp('1967-12-31'),
    offset=DateOffset(weekday=TU(1)),
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USElectionDay1968to1980 = Holiday(
    'Election Day',
    month=11,
    day=2,
    start_date=Timestamp('1968-01-01'),
    end_date=Timestamp('1980-12-31'),
    observance=following_tuesday_every_four_years_observance
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USVeteransDay1934to1953 = Holiday(
    'Veteran Day',
    month=11,
    day=11,
    start_date=Timestamp('1934-1-1'),
    end_date=Timestamp('1953-12-31'),
    observance=sunday_to_monday,
)
# http://www.tradingtheodds.com/nyse-full-day-closings/
USColumbusDayBefore1954 = Holiday(
    'Columbus Day',
    month=10,
    day=12,
    end_date=Timestamp('1953-12-31'),
    observance=sunday_to_monday,
)
ChristmasBefore1954 = Holiday(
    'Christmas',
    month=12,
    day=25,
    end_date=Timestamp('1953-12-31'),
    observance=sunday_to_monday,
)
Christmas = Holiday(
    'Christmas',
    month=12,
    day=25,
    start_date=Timestamp('1954-01-01'),
    observance=nearest_workday,
)


def NY_holidays():
    return [USNewYearsDay,
            USMartinLutherKingJrAfter1998,
            USLincolnsBirthDayBefore1954,
            USWashingtonsBirthDayBefore1964,
            USWashingtonsBirthDay1964to1970,
            USPresidentsDay,
            GoodFriday,
            USMemorialDayBefore1964,
            USMemorialDay1964to1969,
            USMemorialDay,
            USIndependenceDayBefore1954,
            USIndependenceDay,
            USLaborDay,
            USThanksgivingDayBefore1939,
            USThanksgivingDay1939to1941,
            USThanksgivingDay,
            USElectionDay1848to1967,
            USElectionDay1968to1980,
            USVeteransDay1934to1953,
            USColumbusDayBefore1954,
            ChristmasBefore1954,
            Christmas]

