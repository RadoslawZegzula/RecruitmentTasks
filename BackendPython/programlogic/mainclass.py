import datetime

def countDaysToBirthday(date, todayDateFromUser = ""):

    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    todayDate = datetime.datetime.now()

    if(todayDateFromUser != False):
        y = int(todayDateFromUser[0:4])
        m = int(todayDateFromUser[5:7])
        d = int(todayDateFromUser[8:10])
        todayDate = datetime.datetime(y, m, d) 

    birthdayDate = datetime.datetime(todayDate.year, month, day) 

    if (birthdayDate.month == todayDate.month) and (birthdayDate.day == todayDate.day):
        return 0
    if todayDate >= birthdayDate:
        birthdayDate = datetime.datetime(todayDate.year + 1, birthdayDate.month, birthdayDate.day)

    days = (birthdayDate - todayDate).days
    return days

def returnNumbersFromPhoneNumber(phoneNr):
    numbers = ""
    for c in phoneNr:
        if c.isdigit():
            numbers = numbers + c
    return numbers
