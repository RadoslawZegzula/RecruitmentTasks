import pytest
import datetime

from mainclass import *

import sys

def test_countDaysToBirthday():
    dp = DataPopulator()
    assert dp.countDaysToBirthday("1966-08-05T11:50:25.558Z", "1997-08-05") == 0
    assert dp.countDaysToBirthday("1997-07-26", "1997-08-05") == 355
    assert dp.countDaysToBirthday("1997-08-06", "1997-08-05") == 1
    assert dp.countDaysToBirthday("1997-01-13", "1997-08-05") == 161
    assert dp.countDaysToBirthday("1952-02-29", "1997-08-05") == 208

def test_returnNumbersFromPhoneNumber():
    dp = DataPopulator()
    assert dp.returnNumbersFromPhoneNumber("(440)-648-8986") == "4406488986"
    assert dp.returnNumbersFromPhoneNumber("1787-787-99") == "178778799"
    assert dp.returnNumbersFromPhoneNumber("1997-08-06") == "19970806"
    assert dp.returnNumbersFromPhoneNumber("(629)-891-2853") == "6298912853"