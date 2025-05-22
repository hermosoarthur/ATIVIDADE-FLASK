from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Config:
    DEBUG = True
    PORT = 5002
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
