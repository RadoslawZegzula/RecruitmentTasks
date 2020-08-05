import pytest
import datetime

from programlogic.mainclass import countDaysToBirthday, returnNumbersFromPhoneNumber

def test_countDaysToBirthday():
    assert countDaysToBirthday("1966-08-05T11:50:25.558Z", "1997-08-05") == 0
    assert countDaysToBirthday("1997-07-26", "1997-08-05") == 355
    assert countDaysToBirthday("1997-08-06", "1997-08-05") == 1
    assert countDaysToBirthday("1997-01-13", "1997-08-05") == 161

def test_returnNumbersFromPhoneNumber():
    assert returnNumbersFromPhoneNumber("(440)-648-8986") == "4406488986"
    assert returnNumbersFromPhoneNumber("1787-787-99") == "178778799"
    assert returnNumbersFromPhoneNumber("1997-08-06") == "19970806"
    assert returnNumbersFromPhoneNumber("(629)-891-2853") == "6298912853"