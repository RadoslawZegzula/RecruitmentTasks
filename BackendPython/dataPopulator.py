import datetime
import urllib.request, json 

from peewee import *
from location import Location
from login import Login
from person import Person
db = SqliteDatabase('personDatabase.db')

class DataPopulator:
    def countDaysToBirthday(self, date, todayDateFromUser = ""):
        if date ==  "":
          return 0
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        addOneIfSpecialFebruary = 0

        if month == 2 and day == 29:
            day = day - 1
            addOneIfSpecialFebruary = 1

        todayDate = datetime.datetime.now()

        if todayDateFromUser != "":
            y = int(todayDateFromUser[0:4])
            m = int(todayDateFromUser[5:7])
            d = int(todayDateFromUser[8:10])
            todayDate = datetime.datetime(y, m, d) 

        birthdayDate = datetime.datetime(todayDate.year, month, day) 

        if (birthdayDate.month == todayDate.month) and (birthdayDate.day == todayDate.day):
            return 0
        if todayDate >= birthdayDate:
            birthdayDate = datetime.datetime(todayDate.year + 1, birthdayDate.month, birthdayDate.day)

        days = (birthdayDate - todayDate).days + addOneIfSpecialFebruary
        return days

    def returnNumbersFromPhoneNumber(self, phoneNr):
        numbers = ""
        for c in phoneNr:
            if c.isdigit():
                numbers = numbers + c
        return numbers
 
    def populateDataFromApi(self):
        with urllib.request.urlopen("https://randomuser.me/api/?results=2000") as url:
            data = json.loads(url.read().decode())
            for p in data['results']:
                createdLocation = Location.create(
                                streetNumber = p['location']['street']['number'],
                                streetName = p['location']['street']['name'],
                                city = p['location']['city'],
                                state= p['location']['state'],
                                country = p['location']['country'],
                                postcode = p['location']['postcode'],
                                latiduteCordinates = p['location']['coordinates']['latitude'],
                                longitudeCordinates = p['location']['coordinates']['longitude'],
                                offsetTimezone = p['location']['timezone']['offset'],
                                descriptionTimezone = p['location']['timezone']['description']
                        )
                        
                createdLogin = Login.create(
                                uuid = p['login']['uuid'],
                                username = p['login']['username'],
                                password = p['login']['password'],
                                salt = p['login']['salt'],
                                md5 = p['login']['md5'],
                                sha1 = p['login']['sha1'],
                                sha256 = p['login']['sha256']
                        )
   
                daysToBirth = self.countDaysToBirthday(p['dob']['date']);        
                phoneNr = self.returnNumbersFromPhoneNumber(p['phone'])   

                createdPerson = Person.create(
                                gender = p['gender'],
                                nameTitle = p['name']['title'],
                                nameFirst = p['name']['first'],
                                nameLast = p['name']['last'],
                                email = p['email'],
                                personDate = p['dob']['date'],
                                personAge = p['dob']['age'],
                                daysToBirthday = daysToBirth,
                                registeredDate = p['registered']['date'],
                                registeredAge = p['registered']['age'],
                                phone = phoneNr,
                                cell = p['cell'],
                                nameId = p['id']['name'],
                                valueId = p['id']['value'],
                                nationality = p['nat'],
                                location = createdLocation, 
                                login = createdLogin)
                createdLocation.save()        
                createdLogin.save()        
                createdPerson.save()


