## How many days are there until 
#  x event, birthdays, anniversary

# import b/c we are working with dates
import datetime

# define a number of methods 

def header():
    print("-------------------------")
    print("Calculate Date Difference")
    print("-------------------------")

# getting user input for birthday, x, anniversay
def get_birthday():
    year = int(input("What year were you born in?: "))
    month = int(input("What month were you born in?: "))
    day = int(input("What day were you born in?: "))

    birthdate = datetime.date(year, month, day)
    return birthdate

# calculating - we need to find the difference between the dates
def compare(original_date, target_date):
    thisyear = datetime.date(original_date.year, original_date.month, original_date.day)
    dt = thisyear - target_date
    return dt.days 

# output to screen - logic such as how many days or if the date has passed
def printoutput(days):
    if days < 0:
        print("You had your birthday {} days ago".format(-days))
    elif days > 0:
        print("Your birthday is in {} days".format(days))
    else:
        print("Happy birthday!!")

# define a main method

def main():
    header()
    existingdate = get_birthday()
    print(str(existingdate))
    today = datetime.date.today()
    print(str(today))
    numofdays = compare(existingdate, today)
    print(str(numofdays))
    printoutput(numofdays)


main()
