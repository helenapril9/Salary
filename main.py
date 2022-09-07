# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from application import salary
from application.db import people
from application import time_view

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    time_view.time_now()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
