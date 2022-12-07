"""Sets database url so that tests don't use the database of the normal app"""
from os import environ
environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
