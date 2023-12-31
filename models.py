from mongoengine import *
from dotenv import load_dotenv
from enum import Enum
import os
import string
import secrets

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

class CharacterOptions(Enum):
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    ALPHANUMERIC = string.ascii_letters + string.digits
    MIXED = f'{string.ascii_letters + string.digits}{"$_@!^&%*)(-?"}'

class PasswordStrength(Enum):
    VERY_STRONG_LENGTH  = 16
    STRONG_LENGTH = 10

class Utilities:
    def upcase_option(character_option: str) -> str:
       ''' Make all characters uppercase to compare to Enum member name '''
       return character_option.upper()
    

class PasswordGenerator:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters

    def generate_password(self) -> str:
        ''' 
             Iterate over the Enum, if the member name is the same as the value passed into 
             the constructor for the character property, get that enum members value and pass
             the sequence to secrets.choice(). Using the length property to give the desired
             number of random characters to be returned. 
        '''
        character_result = Utilities.upcase_option(self.characters)
        for character in (CharacterOptions):
            if character.name == character_result:
                return ''.join(secrets.choice(character.value) for _ in range(self.length))