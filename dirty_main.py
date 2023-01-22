from application.db.people import *
from application.salary import *
import datetime

now = datetime.datetime.today()


def main():
    print(now)
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
