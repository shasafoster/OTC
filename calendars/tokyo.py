from datetime import time
from itertools import chain
import pandas as pd
from pytz import timezone
from pytz import UTC

from xtks_holidays import (
    NewYearsHolidayDec31,
    NewYearsHolidayJan1,
    NewYearsHolidayJan2,
    NewYearsHolidayJan3,
    ComingOfAgeDay,
    NationalFoundationDay,
    VernalEquinoxes,
    GreeneryDayThrough2006,
    ShowaDay,
    ConstitutionMemorialDay,
    GreeneryDay2007Onwards,
    CitizensHolidayGoldenWeek,
    ChildrensDay,
    MarineDayThrough2002,
    MarineDay2003Onwards,
    MountainDay,
    AutumnalEquinoxes,
    CitizensHolidaySilverWeek,
    RespectForTheAgedDayThrough2002,
    RespectForTheAgedDay2003Onwards,
    HealthAndSportsDay,
    CultureDay,
    LaborThanksgivingDay,
    EmperorAkihitoBirthday,
    EmperorNaruhitoBirthday,
    Misc2019Holidays
)


XTKS_START_DEFAULT = pd.Timestamp('2000-01-01', tz=UTC)



def TKY_holidays():
    return [
        NewYearsHolidayDec31,
        NewYearsHolidayJan1,
        NewYearsHolidayJan2,
        NewYearsHolidayJan3,
        ComingOfAgeDay,
        NationalFoundationDay,
        GreeneryDayThrough2006,
        ShowaDay,
        ConstitutionMemorialDay,
        GreeneryDay2007Onwards,
        CitizensHolidayGoldenWeek,
        ChildrensDay,
        MarineDayThrough2002,
        MarineDay2003Onwards,
        MountainDay,
        RespectForTheAgedDayThrough2002,
        RespectForTheAgedDay2003Onwards,
        HealthAndSportsDay,
        CultureDay,
        LaborThanksgivingDay,
        EmperorAkihitoBirthday,
        EmperorNaruhitoBirthday,
    ]


