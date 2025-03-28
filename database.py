from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DB_URL = "mysql+pymysql://randomuser:ikcL1P6d6pkUuwOBLkTWzFDY3d6GwHow@dpg-cvjeoueuk2gs738ter20-a/db_restapi_so4z"
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()