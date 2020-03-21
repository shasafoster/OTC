from datetime import time
from pandas.tseries.holiday import (
    EasterMonday,
    GoodFriday,
    Holiday,
)
from pytz import timezone

from common_holidays import (
    new_years_day,
    european_labour_day,
    ascension_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)

# Regular Holidays
# ----------------
NewYearsDay = new_years_day()

BerchtoldsDay = Holiday(
    "Berchtold's Day",
    month=1,
    day=2,
)

EuropeanLabourDay = european_labour_day()

AscensionDay = ascension_day()

WhitMonday = whit_monday()

SwissNationalDay = Holiday(
    "Swiss National Day",
    month=8,
    day=1
)

ChristmasEve = christmas_eve()

Christmas = christmas()

BoxingDay = boxing_day()

NewYearsEve = new_years_eve()



def ZUR_holidays():
    return [
        NewYearsDay,
        BerchtoldsDay,
        EasterMonday,
        GoodFriday,
        EuropeanLabourDay,
        AscensionDay,
        WhitMonday,
        SwissNationalDay,
        ChristmasEve,
        Christmas,
        BoxingDay,
        NewYearsEve,
    ]
