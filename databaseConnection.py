import os
import json
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

path = os.getcwd()
file = "connection.json"
fullpath = os.path.join(path,file)

with open(fullpath, mode='r') as myfile:
    content = json.load(myfile)
host = content["database"]["host"]
password = content["database"]["password"]
username = content["database"]["user"]
database = content["database"]["database"]

SQLPARAMETERS = "postgresql://{}:{}@{}/{}".format(username,password,host,database)
engine = create_engine(
    SQLPARAMETERS
)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db(): #Session Maker to create sessions to the DB
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



