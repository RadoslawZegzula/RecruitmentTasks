
from peewee import *
from login import Login
from location import Location
db = SqliteDatabase('personDatabase.db')

class Person(Model):
        gender = CharField(max_length=70, null=True)    
        nameTitle = CharField(max_length=70, null=True) 
        nameFirst = CharField(max_length=70, null=True)
        nameLast = CharField(max_length=70, null=True)
        email = CharField(max_length=70, null=True) 
        personDate = DateTimeField(null=True) 
        personAge = IntegerField(null=True)
        daysToBirthday = IntegerField(null=True) 
        registeredDate = DateTimeField(null=True) 
        registeredAge = IntegerField(null=True)
        phone = IntegerField(null=True) 
        cell = CharField(max_length=70, null=True) 
        nameId = CharField(max_length=70, null=True)
        valueId = CharField(max_length=70, null=True)
        nationality = CharField(max_length=70, null=True)

        location = ForeignKeyField(Location, null = True)
        login = ForeignKeyField(Login, null = True)           

        class Meta:
                database=db