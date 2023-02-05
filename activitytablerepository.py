from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables import ActivityTable


class ActivityTableRepository:
    def __init__(self):
        self.my_conn = create_engine("mysql+mysqldb://root:admin123@localhost:3306/mymaindb")
        Session = sessionmaker(bind=self.my_conn)
        self.session = Session()


    def insert_data(self, Title, start_time, stop):
        timedelta = stop - start_time
        TimeSpentInMinutes = timedelta.total_seconds() / 60
        record = ActivityTable(Title=Title, TimeSpentInMinutes=TimeSpentInMinutes, start=start_time, stop=stop)
        self.session.add(record)
        self.session.commit()
