def isconsistent(adate, aformat):
    if len(adate) != len(aformat):
        print('Error: the date is wrong.')
        return False
    for i in range(len(aformat)):
        if aformat[i] in ['Y', 'M', 'D']:
            if not adate[i].isdecimal():
                print('Error:', adate[i], ': Y or M or D matches a number.')
                return False
        else:
            if adate[i] != aformat[i]:
                print('Error:', adate[i], 'is not matched with', aformat[i])
                return False
    return True

def isvalid(adate, aformat):
    global ayear
    global amonth
    global aday

    ypos = aformat.find('Y')
    ayear = adate[ypos:ypos+4]
    ayear = int(ayear)
    
    mpos = aformat.find('M')
    amonth = adate[mpos:mpos+2]
    amonth = int(amonth)
    if amonth <1 or amonth > 12:
        print('Month is out of range.')
        return False

    dpos = aformat.find('D')
    aday = adate[dpos:dpos+2]
    aday = int(aday)
    if amonth in [1, 3, 5, 7, 9, 11]:
        if aday < 1 or aday > 31:
            print('Day is out of range.')
            return False
    if amonth in [4, 6, 8, 10, 12]:
        if aday < 1 or aday > 30:
            print('Day is out of range.')
            return False
    if amonth == 2:
        if aday <1 or aday > 28:
            print('Day is out of range.')
            return False

    return True

import datetime
def weekdayStr(mydatedate):
    dayString = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    myweekday = mydatedate.weekday() #요일을 정수로 변환하여 반환
    myweekday = dayString[myweekday]
    return myweekday

dateformat_options=['YYYY-MM-DD', 'MM/DD/YYYY']

while True:
    mydateformat = 0
    while mydateformat!='1' and mydateformat!='2':
        print('Date format options: 1. YYYY-MM-DD, 2. MM/DD/YYYY')
        mydateformat = input('Choose a date format: ')

    mydateformat = int(mydateformat)
    while True:
        mydate = input('Enter a date: ')
        if isconsistent(mydate, dateformat_options[mydateformat-1]) and isvalid(mydate, dateformat_options[mydateformat-1]):
            break
        
    mydatedate =datetime.date(ayear, amonth, aday) 
    print('The weekday of', mydatedate, "is", weekdayStr(mydatedate), ".")

    mynextdate =datetime.date(ayear+1, amonth, aday) 
    print('The date of a year after', mydatedate, "is", mynextdate, '. Its weekday is', weekdayStr(mynextdate), ".")

    again = input('\nDo you like to test another day? (y): ')
    print()
    if again != 'y':
        break

print('The random auto-testing is starting....')

import random
def randdate():
    rand_format = random.randrange(2)
    rand_date = ''
    if rand_format == 1:
        rand_date += str(random.randrange(2000, 2021))
        for i in [20, 50]:
            rand_date += '-'
            rand_num = random.randrange(1, i)
            if rand_num < 10:
                rand_date += '0' + str(rand_num)
            else:
                rand_date += str(rand_num)
    else:
        for i in [20, 50]:
            rand_num = random.randrange(1, i)
            if rand_num < 10:
                rand_date += '0' + str(rand_num)
            else:
                rand_date += str(rand_num)
            rand_date += '/'
        rand_date += str(random.randrange(2000, 2021))

    return rand_date
    
for i in range(10):
    rdate = randdate()
    print('\nThe date to test:',rdate, end='\t')
    rformat = random.choice(dateformat_options)
    print('with the format:', rformat)
    if not isconsistent(rdate, rformat):
        print('The date formate', rformat, 'is not consistent with the date', rdate)
    elif not isvalid(rdate, rformat):
        print('The date', rdate, 'is not a valid date.')
    else:
        print('The date', rdate, 'is valid.')
        rdatedate =datetime.date(ayear, amonth, aday) 
        print('The weekday of', rdate, "is", weekdayStr(rdatedate), ".")
