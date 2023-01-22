from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

now = datetime.datetime.today()


def main():
    print(now)
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
