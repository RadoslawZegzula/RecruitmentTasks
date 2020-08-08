import datetime
from location import Location
from login import Login
from person import Person
from peewee import *
from playhouse.shortcuts import model_to_dict

class SearcherByUserCommand:      
    def displayDataByUserCommand(self, args):
        if(args.category =="persons-percents"):           
            self.printPersonPercentes()
            return
        if(args.category =="avg" 
        and (args.firstOptional == 'male' or args.firstOptional == 'female' or args.firstOptional == 'all')):           
            self.printWantedAvgAge(args.firstOptional)
            return
        if(args.category =="pop-cities" 
        and args.firstOptional is not None 
        and args.firstOptional != "" 
        and args.firstOptional.isdigit() == True):
            self.printNMostPopularCities(int(args.firstOptional))
            return
        if(args.category =="pop-pass" 
        and args.firstOptional is not None 
        and args.firstOptional != "" 
        and args.firstOptional.isdigit() == True):
            self.printNMostPopularPassword(int(args.firstOptional))   
            return  
        if(args.category =="safest-pass"):           
            self.printSafestPassword()
            return
        if(args.category =="persons-birth"):
            self.printUsersFromBirthDateRange(args.firstOptional, args.secondOptional)  
            return
    
    def printPersonPercentes(self):
        malesCount = 0
        femalesCount = 0
        twoGendersCount= 0
        for user in Person.select():
            if(user.gender=='male'):
                malesCount += 1
            if(user.gender=='female'):
                femalesCount += 1
        twoGendersCount = malesCount + femalesCount

        malePercentage = "{:.0%}".format(malesCount / twoGendersCount)
        femalePercentage = "{:.0%}".format(femalesCount / twoGendersCount)
        print("males:" + malePercentage + " females:" + femalePercentage)
        return malePercentage, femalePercentage
  
    def printWantedAvgAge(self, firstOptional):
        malesCount = 0
        femalesCount = 0
        twoGendersCount= 0
        malesAgeCount = 0
        femalesAgeCount = 0
        twoGendersAgeCount = 0

        for user in Person.select():
            if(user.gender=='male'):
                malesCount += 1
                malesAgeCount += user.personAge
            if(user.gender=='female'):
                femalesCount += 1
                femalesAgeCount += user.personAge

        twoGendersCount = malesCount + femalesCount
        twoGendersAgeCount = malesAgeCount + femalesAgeCount

        maleAvgAge = malesAgeCount / malesCount
        femaleAvgAge = femalesAgeCount / femalesCount
        personsAvgAge = twoGendersAgeCount / twoGendersCount

        if(firstOptional == 'male'):
            print(" Males avg age:" + str(maleAvgAge))
            return maleAvgAge
        
        if(firstOptional == "female"):
            print(" Females avg age:" + str(femaleAvgAge))
            return femaleAvgAge
        
        if(firstOptional == 'all'):
            print(" Persons avg age:" + str(personsAvgAge))
            return personsAvgAge

    def printNMostPopularCities(self, n):
        dict = {} 
        count, itm = 0, '' 
        for item in Location.select(): 
            dict[item.city] = dict.get(item.city, 0) + 1

        if(n > len(dict)):
            print("You should specify number that is less that " + str(len(dict)))
            return
        
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(0, n):
            print(dict[i])
            result.append(dict[i])
        return result
        
    def printNMostPopularPassword(self, n):
        dict = {} 
        count, itm = 0, '' 
        for item in Login.select(): 
            dict[item.password] = dict.get(item.password, 0) + 1
        
        if(n > len(dict)):
            print("You should specify number that is less that " + str(len(dict)))
            return
        
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(0, n):
            print(dict[i])
            result.append(dict[i])
        return result

    def printSafestPassword(self):    
        safestPassword = ""
        mostPoints = 0

        smallLetterOrNumberPoint = 1
        bigLetterPoint = 2
        minEightCharsPoint = 5
        specialDigitPoint = 3

        passwordSpecialDigits = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-"
        , ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|" , "}", "~"]
        
        for item in Login.select():
            if(item.password == ""):
                continue
            
            pointsCount = 0
            
            if(any(x.islower() for x in item.password) or any(x.isdigit() for x in item.password)):
                pointsCount += smallLetterOrNumberPoint

            if(any(x.isupper() for x in item.password)) :
                pointsCount += bigLetterPoint

            if(any(e in item.password for e in passwordSpecialDigits)):
                pointsCount += specialDigitPoint       
    
            if(len(item.password) > 7):
                pointsCount += minEightCharsPoint
    
            if(pointsCount > mostPoints):
                mostPoints = pointsCount
                safestPassword = item.password        
            
        print("Safest Password: " + safestPassword + "  Points: " + str(mostPoints))
        return safestPassword

    def printUsersFromBirthDateRange(self, LeftDate, rightDate):
        
        date_left = ""
        date_right = ""
        try:
            date_left = datetime.datetime.strptime(LeftDate, "%Y-%m-%d").date()
            date_right = datetime.datetime.strptime(rightDate, "%Y-%m-%d").date()
        except ValueError:
            print("Given date is in bad format, try YYYY-MM-DD")
            return
        
        if(date_left > date_right):
            print("Left date should be earlier that right date")
            return

        result = []
        for person in Person.select():
            personDate = datetime.datetime.strptime(person.personDate[0:10], "%Y-%m-%d").date()
            if(personDate >= date_left and personDate <= date_right):
                result.append(model_to_dict(person))
        
        print(result)
        return result