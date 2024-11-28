from sqlalchemy import engine, create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///todooo.db")
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

