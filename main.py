# program that calculates how many years, days, hours, and minutes you have lived
# continuously ask for the three inputs and give the calculations until a negative number has been entered
# use methods and exception handling
# input: year month day

# Author: Laura Figueroa

from datetime import datetime, date


def is_valid_date(year, month, day):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29
    return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]


def get_date():
    while True:
        try:
            year = int(input("Enter year of birth:\n"))
        except ValueError:
            print("You did not enter a valid number, please try again")
            get_date()
            break
        if datetime.now().year >= year >= 0:
            break
        print("Year of birth cannot be negative or greater than current year, please try again")
        get_date()
        break
    while True:
        try:
            month = int(input("Enter month of birth as number: \n"))
        except ValueError:
            print("You did not enter a valid number, please enter a month number from 1-12")
            get_date()
            break
        if 1 <= month <= 12:
            break
        print("Month entered must be between 1 and 12, please try again")
        get_date()
        break
    while True:
        try:
            day = int(input("Enter day of birth: \n"))
        except ValueError:
            print("Day entered was not a valid number, please try again")
            get_date()
            break
        if 0 < day <= 31:
            break
        print("Day must be between 1 and 31, please try again")
        get_date()
        break
    if is_valid_date(year, month, day):
        calculate_age(year, month, day)
    else:
        print("The date entered is not valid")
        get_date()
    try:
        end_program = int(input("Enter a negative number to end program\n"))
        if end_program >= 0:
            get_date()
        else:
            print("*** EXIT ***")
    except ValueError:
        get_date()


def calculate_age(y, m, d):
    birth_date = date(y, m, d)
    current_date = date(datetime.now().year, datetime.now().month, datetime.now().day)

    days = (current_date - birth_date).days
    years = current_date.year - birth_date.year
    days -= years*365
    months = days // 30
    days -= months*30
    hours = datetime.now().hour
    minutes = datetime.now().minute
    print(" %d year(s),  %d month(s), %d day(s), %d hours, %d minutes" % (years, months, days, hours, minutes))


if __name__ == '__main__':
    get_date()

