import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
