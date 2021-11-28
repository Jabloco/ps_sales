import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///' + os.path.join(basedir, 'psprice.sqlite3'))
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
