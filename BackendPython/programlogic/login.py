from peewee import *
db = SqliteDatabase('programlogic/personDatabase.db')

class Login(Model):
        uuid = CharField(max_length=70, null=True)
        username = CharField(max_length=70, null=True)
        password = CharField(max_length=70, null=True)
        salt = CharField(max_length=70, null=True)
        md5 = CharField(max_length=70, null=True)
        sha1 = CharField(max_length=70, null=True)
        sha256 = CharField(max_length=70, null=True)

        class Meta:
                database=db             