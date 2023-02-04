import win32gui
import schedule
from datetime import datetime
from activitytablerepository import ActivityTableRepository
from injector import singleton, inject


class WindowsMonitor:

    @singleton
    @inject
    def __init__(self, ActivityTableRepository: ActivityTableRepository):
        self.ActivityTableRepository = ActivityTableRepository
        self.stop_flag = False

    def __get_active_window(self):
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def start_monitoring(self):
        self.__update_state()
        schedule.every(1).second.do(self.__monitor_windows_activity)
        while not self.stop_flag:
            schedule.run_pending()

    def __update_state(self):
        self.active_window = self.__get_active_window()
        self.start_time = datetime.now()

    def __monitor_windows_activity(self):
        current_title = self.__get_active_window()
        is_title_not_match = current_title != self.active_window
        if current_title and is_title_not_match:
            self.__record_activity()

    def __record_activity(self):
        stop = datetime.now()
        self.ActivityTableRepository.insert_data(self.active_window, self.start_time, stop)
        self.__update_state()

    def stop_monitoring(self):
        self.stop_flag = True
        schedule.clear()
