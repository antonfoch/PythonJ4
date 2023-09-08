from mongoengine import *

connect('Database', host='mongodb://127.0.0.1:27017/Database')

class student(Document):
    name = StringField(max_length=50)
    age = IntField()
    address = StringField(max_length=50)

class message(Document):
    name = StringField(max_length=50)
    message = StringField(max_length=50)

class channel(Document):
    name = StringField(max_length=50)
    channel = StringField(max_length=50)

class chat(Document):
    name = StringField(max_length=50)
    chat = StringField(max_length=50)


me = student(name='Anton', age=20, address='Vincennes').save()
me = message(name='Anton', message='Hello').save()
me = channel(name='Anton', channel='General').save()
me = chat(name='Anton', chat='Hello').save()
