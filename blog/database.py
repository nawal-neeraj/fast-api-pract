from os.path import join, dirname
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

userName: str = os.getenv('USERNAME')
password = os.getenv("PASS")
port = os.getenv("PORT")
dbname = os.getenv("DBNAME")
DATABASE_URL = f"mysql+pymysql://{userName}@{port}:3306/{dbname}"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()