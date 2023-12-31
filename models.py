from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv('.env')
connect(host=os.getenv('MONGO_URI'))

class Account(EmbeddedDocument):
    name = StringField(required=True)
    category = StringField(required=True)
    password = StringField(required=True)
    account_notes = StringField()

class Note(EmbeddedDocument):
    title = StringField(required=True)
    category = StringField(required=True)
    note = StringField(required=True)

class Users(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    accounts = ListField(EmbeddedDocumentField(Account))
    notes = ListField(EmbeddedDocumentField(Note))