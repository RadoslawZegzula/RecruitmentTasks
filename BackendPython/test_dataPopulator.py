import pytest
import datetime
from dataPopulator import *

def test_countDaysToBirthday_blankBirthDate():
    dp = DataPopulator()
    assert dp.countDaysToBirthday(birthdayDate = "") == 0
    assert dp.countDaysToBirthday(birthdayDate = "", todayDateFromUser = "2020-08-05") == 0
    assert dp.countDaysToBirthday(birthdayDate = "", todayDateFromUser = "1997-08-06") == 0

def test_countDaysToBirthday_beforeTodayMonthOrDay():
    dp = DataPopulator()
    assert dp.countDaysToBirthday(birthdayDate = "1997-07-26", todayDateFromUser = "2020-08-05") == 355
    assert dp.countDaysToBirthday(birthdayDate = "1997-01-13", todayDateFromUser = "2020-08-05") == 161
    assert dp.countDaysToBirthday(birthdayDate = "1997-08-04", todayDateFromUser = "2020-08-05") == 364

def test_countDaysToBirthday_afterTodayMonthOrDay():
    dp = DataPopulator()
    assert dp.countDaysToBirthday(birthdayDate = "1966-08-05T11:50:25.558Z", todayDateFromUser = "2020-08-05") == 0
    assert dp.countDaysToBirthday(birthdayDate = "1997-08-06", todayDateFromUser = "2020-08-05") == 1
    assert dp.countDaysToBirthday(birthdayDate = "1997-08-09", todayDateFromUser = "2020-08-08") == 1
    assert dp.countDaysToBirthday(birthdayDate = "1997-09-16", todayDateFromUser = "2020-08-08") == 39

def test_countDaysToBirthday_shouldWorkWithFebruary29():
    dp = DataPopulator()
    assert dp.countDaysToBirthday(birthdayDate = "1952-02-29", todayDateFromUser = "2020-08-05") == 208
    assert dp.countDaysToBirthday(birthdayDate = "2001-02-29", todayDateFromUser = "2020-07-08") == 236

def test_countDaysToBirthday_shouldWorkWithLongerFormat():
    dp = DataPopulator()
    assert dp.countDaysToBirthday(birthdayDate = "1966-01-05T11:50:25.558Z", todayDateFromUser = "2020-08-05") == 153
    assert dp.countDaysToBirthday(birthdayDate = "1966-04-06T11:50:25.558Z", todayDateFromUser = "2020-08-05") == 244
    assert dp.countDaysToBirthday(birthdayDate = "1966-09-06T11:50:25.558Z", todayDateFromUser = "2020-08-05") == 32



def test_returnNumbersFromPhoneNumber_worksWithNumbers():
    dp = DataPopulator()
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "1787-787-99") == "178778799"
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "1997-08-06") == "19970806"
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "19970806") == "19970806"

def test_returnNumbersFromPhoneNumber_worksWithEmptyString():
    dp = DataPopulator()
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "") == ""

def test_returnNumbersFromPhoneNumber_worksWithSpecialChars():
    dp = DataPopulator()
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "Abfgdr!@#$%^&**()") == ""
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") == ""
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "!\"#$%&'()87*+,-./:;<=>?@[\\]^_`{|}~86") == "8786"
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "(629)-891-2853") == "6298912853"
    assert dp.returnNumbersFromPhoneNumber(phoneNr = "(440)-648-8986") == "4406488986"