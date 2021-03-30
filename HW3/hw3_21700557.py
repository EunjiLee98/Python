import datetime
import string
import random

def formatChecker (date, dateFormat) : # function to check if the formats are consistent

    if dateFormat == 1 :
        if date.find('-') == 4 and date.find('-',5) == 7: # check if the format is valid
            return True 
            
        elif date.find('/') == 2 or date.find('/',3) == 7 or date.find('/') == 4 or date.find('/',5) == 7 :
            # in case : MM/DD-YYYY or MM-DD/YYYY or MM/DD/YYYY or YYYY/MM-DD or YYYY-MM/DD or YYYY/MM/DD
            print('Error: 1 is not matched with -') # error message
            return False

    elif dateFormat == 2 :
        if date.find('/') == 2 and date.find('/',3) == 5: # check if the format is valid
            return True
        elif date.find('-') == 4 or date.find('-',5) == 7 or date.find('-') == 2 or date.find('-',3) == 5:
            # in case : YYYY-MM/DD or YYYY/MM-DD or YYYY-MM-DD or MM-DD/YYYY or MM/DD-YYYY or MM-DD-YYYY
            print('Error: 2 is not matched with /') # error message
            return False

        
def dateChecker (date, dateFormat) : # function to check if the date if valid date
    if dateFormat == 1 : # format YYYY-MM-DD
        tempdate = date.split("-")
        month = tempdate[1] # MM
        day = tempdate[2] # DD

    elif dateFormat == 2 : # format MM/DD/YYYY
        tempdate = date.split("/")
        month = tempdate[0] # MM
        day = tempdate[1] # DD


    month = int(month) #type conversion to check the range 
    day = int(day) # =
    
    if 0 < month and month < 13 : # if month is valid 
        if oddeven(month) == 1 : # if month is odd
            if 0 < day and day < 32 : # day should be the range 1~31
                return True
            else :
                print('Day is out of range') #error messege
                return False
            
        elif oddeven(month) == 2 : #if month is even
            if month == 2 and 0 < day < 29 : #February case 
                return True
            elif month != 2 and 0 < day and day < 31 : # except February, if month is even 
                return True
            else :
                print('Day is out of range') #error message
                return False
            
    else : #if month if not valid 
       print('Month is out of range') #error message
       return False

        
def weekday (date) : # function returns its weekday name
    weekdayString = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun'] # list for weekday

    if date.find('-') == 4 : # if date format is YYYY-MM-DD
        tempdate = date.split('-')
        year = tempdate[0] # YYYY
        month = tempdate[1] # MM
        day = tempdate[2] # DD

    elif date.find('/') == 2 : # if date format is MM/DD/YYYY
        tempdate = date.split('/')
        year = tempdate[2] # YYYY
        month = tempdate[0] # MM
        day = tempdate[1] # DD
        
    year = int(year) # type conversion to calculate 
    month = int(month) # =
    day = int(day) # =

    weekday = datetime.date(year,month,day).weekday() # get the integer (Mon = 0 ~ Sun = 6)
    weekday = weekdayString[weekday] # get the String (Mon ~ Sun)
    weekdayFormat = datetime.datetime(year,month,day) # formatting
    print('The weekday of ' + '{:%Y-%m-%d}'.format(weekdayFormat) + ' is ' + weekday + ' . ') # Print what weekday the given day is 

    year = year + 1 # a year after 
    weekday = datetime.date(year,month,day).weekday() # get the integer (Mon = 0 ~ Sun = 6)
    weekday = weekdayString[weekday] # get the String (Mon ~ Sun)
    weekdayFormat = datetime.datetime(year,month,day) # formatting
    print('The date of a year after ' + date + ' is ' + '{:%Y-%m-%d}'.format(weekdayFormat) + ' . ' + 'Its weekday is ' + weekday + ' . ') # Print what weekday it will be, a year after the given day

    return weekday #return its weekday name 
    
def weekdayForRandom (date) : #weekday for random 
    weekdayString = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun'] # list for weekday

    if date.find('-') == 4 : # if date format is YYYY-MM-DD
        tempdate = date.split('-')
        year = tempdate[0] # YYYY
        month = tempdate[1] # MM
        day = tempdate[2] # DD

    elif date.find('/') == 2 : # if date format is MM/DD/YYYY
        tempdate = date.split('/')
        year = tempdate[2] # YYYY
        month = tempdate[0] # MM
        day = tempdate[1] # DD
        
    year = int(year) # type conversion to calculate 
    month = int(month) # =
    day = int(day) # =
    
    weekday = datetime.date(year,month,day).weekday()  # get the integer (Mon = 0 ~ Sun = 6)
    weekday = weekdayString[weekday] # get the String (Mon ~ Sun)
    weekdayFormat = datetime.datetime(year,month,day) # formatting
    print('The weekday of ' + '{:%Y-%m-%d}'.format(weekdayFormat) + ' is ' + weekday + ' . ')
    
def oddeven (num) : #function to check if it is odd or even
    if num % 2 == 0 :
        return 2 # if it is even, return 2
    else :
        return 1 # if it it odd, return 1


def randomDate (): # function to return a randomly composed date
    randomFormat = random.randrange(1,3) # random format 1 or 2 
    year = random.randrange(2000,2021) # year between 2000 and 2020
    month = random.randrange(1,20) # month between 01 and 19
    day = random.randrange(1,50) # day between 01 and 49

    year = str(year) # type conversion to add '0'
    if 0 < month and month < 10 : # if month is single digit 
        month = str(month)
        month = str(0) + str(month) # add '0' before month
    if 0 < day and day < 10 :  # if day is single digit 
        day = str(day)  
        day = str(0) + str(day) # add '0' before day

    year = str(year) # type conversion to add year-month-day or month/day/year
    month = str(month) # =
    day = str(day) # =
    
    if randomFormat == 1 : # if format is YYYY-MM-DD
        randomDate = year + '-' + month + '-' + day
        return randomDate # return a randomly composed date

    elif randomFormat == 2 : # if format is MM/DD/YYYY
        randomDate = month + '/' + day + '/' + year
        return randomDate # return a randomly composed date
        
    
    
print('Date format options : 1. YYYY-MM-DD, 2. MM/DD/YYYY') # ask the user to choose a date format
option = input('Choose a date format : ')
option = int(option)

while not option == 1 and not option == 2 : # keep repeating if the input number is not valid
    print('Date format options : 1. YYYY-MM-DD, 2. MM/DD/YYYY')
    option = input('Choose a date format : ')
    option = int(option)
    
date = input('Enter a date : ')

while not formatChecker(date,option) or not dateChecker(date,option) : # keep repeating if the date if not valid
    date = input('Enter a date : ')

weekday(date)

answer = input('\nDo you like to test another day? (y/n) : ') # Ask the user if he/she wants to test another date
print('\n')


while answer == 'y' : # If y, repeat 
    print('Date format options : 1. YYYY-MM-DD, 2. MM/DD/YYYY') # ask the user to choose a date format
    option = input('Choose a date format : ')
    option = int(option)

    while not option == 1 and not option == 2 : # keep repeating if the input number is not valid
        print('Date format options : 1. YYYY-MM-DD, 2. MM/DD/YYYY')
        option = input('Choose a date format : ')
        option = int(option)
        
    date = input('Enter a date : ')

    while not formatChecker(date,option) or not dateChecker(date,option) : # keep repeating if the date if not valid
        date = input('Enter a date : ')

    weekday(date)
    
    answer = input('\nDo you like to test another day? (y/n) : ') # ask the user if he/she wants to test another date

print('\nThe random auto-testing is starting....\n') 

randomDateList = [] #random date list 

for i in range(10) : # 10 times 
    randomDateList.append(randomDate()) # compose 10 random dates 
    randomDateFormat = random.randrange(1,3) # random date format 1 or 2 
    
    if randomDateFormat == 1 : # random date format is 1 (YYYY-MM-DD)
        print('The date to test : ' + randomDateList[i] + '  with the format : YYYY-MM-DD')
        if not formatChecker(randomDateList[i], randomDateFormat) : # check their format consistency 
            print('The date format YYYY-MM-DD is not consistent with the date ' + randomDateList[i])
        elif not dateChecker(randomDateList[i], randomDateFormat) : # check the validity of the random date 
            print('The date ' + randomDateList[i] + ' is not a valid date.')
        else :
            print('The date ' + randomDateList[i] + ' is valid') # if the date is a valid date, print its weekday
            weekdayForRandom(randomDateList[i])
        
    elif randomDateFormat == 2 : # random date format is 1 (MM-DD-YYYY)
        print('The date to test : ' + randomDateList[i] + '  with the format : MM/DD/YYYY')
        if not formatChecker(randomDateList[i], randomDateFormat) : # check their format consistency 
            print('The date format MM/DD/YYYY is not consistent with the date ' + randomDateList[i])
        elif not dateChecker(randomDateList[i], randomDateFormat) : # check the validity of the random date 
            print('The date ' + randomDateList[i] + ' is not a valid date.')
        else :
            print('The date ' + randomDateList[i] + ' is valid') # if the date is a valid date, print its weekday
            weekdayForRandom(randomDateList[i])

    print('\n')     
