from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import DATETIME

Base = declarative_base()
metadata = Base.metadata


class migrations(Base):

    __tablename__ = 'ActivityTable'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    Title = Column(String(1000))
    TimeSpentInMinutes = Column(INTEGER)
    Start = Column(DATETIME)
    Stop = Column(DATETIME)
