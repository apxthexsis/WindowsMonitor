from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ActivityTable(Base):
    __tablename__ = 'ActivityTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String)
    TimeSpentInMinutes = Column(Integer)
    start = Column(DateTime)
    stop = Column(DateTime)
