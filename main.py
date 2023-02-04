from WindowsMonitor import WindowsMonitor
from injector import Injector, singleton, inject
import sys
import threading

class Menu:

    @inject
    @singleton
    def __init__(self, monitor: WindowsMonitor):
        self.monitor = monitor
        self.monitor_thread = None

    def main_menu(self):
        while True:
            self.print_interface()

            try:
                choice = int(input("Enter your choice [1-3]: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            self.check_conditions(choice)

    def check_conditions(self, choice):
        thread_is_not_alive = self.monitor_thread is None or not self.monitor_thread.is_alive()
        thread_is_alive = self.monitor_thread is not None and self.monitor_thread.is_alive()
        
        if choice == 1:
            if thread_is_not_alive:
                self.monitor_thread = threading.Thread(target=self.monitor.start_monitoring)
                self.monitor_thread.start()
        elif choice == 2:
            if thread_is_alive:
                self.stop_function()
                self.monitor_thread = None
        elif choice == 3:
            if thread_is_alive:
                self.stop_function()
            print("Quitting Windows Monitor")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

    def print_interface(self):
        print("\nWindows Monitor Main Menu")
        print("1. Start Monitoring")
        print("2. Stop Monitoring")
        print("3. Quit")

    def stop_function(self):
        self.monitor.stop_monitoring()
        self.monitor_thread.join()


if __name__ == "__main__":
    injector = Injector()
    main = injector.get(Menu)
    main.main_menu()
