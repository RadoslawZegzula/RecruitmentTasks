from peewee import *
db = SqliteDatabase('personDatabase.db')

class Location(Model):
        streetNumber = IntegerField(null=True)
        streetName = CharField(max_length=70, null=True)
        city = CharField(max_length=70, null=True)
        state = CharField(max_length=70, null=True)
        country = CharField(max_length=70, null=True)
        postcode = IntegerField(null=True)
        latiduteCordinates = CharField(max_length=70, null=True)
        longitudeCordinates = CharField(max_length=70, null=True)
        offsetTimezone = CharField(max_length=70, null=True)
        descriptionTimezone = CharField(max_length=70, null=True)
      
        class Meta:
                database=db