import datetime
import random
import sys
import string


normalBodyTemp = dict() # create dictionary
normalBodyTemp = { # key : age group, value ( key : measurement site, value : temperature )
    '0~2 years' : {'Oral' : (),
                   'Ear' : (36.4, 38.0),
                   'Rectal' : (36.6, 38.0),
                   'Axillary' : (34.7, 37.3)
    },
    '3~10 years' : {'Oral' : (35.5, 37.5),
                    'Ear' : (36.1, 37.8),
                    'Rectal' : (36.6, 38.0),
                    'Axillary' : (35.9, 36.7)
    },
    '11~65 years' : {'Oral' : (36.4, 37.6),
                    'Ear' : (35.9, 37.6),
                    'Rectal' : (37.0, 38.1),
                    'Axillary' : (35.2, 36.9)
    },
    'over 65 years' : {'Oral' : (35.8, 36.9),
                       'Ear' : (35.8, 37.5),
                       'Rectal' : (36.2, 37.3),
                       'Axillary' : (35.6, 36.3)
    }
}

def validationCheck (aList) : # fuction to validate the user's input
    if len(aList) != 3 : # check the number of values is 3 or not 
        return 'Error : Your answer should contain 3 items(age group, measurement site, body temperature) :(' # return error message

    for i in range(len(aList)) :
        if aList[i] in '' : # check if there is no null value
            return 'Error : Your answer has a null input :(' # return error message
        elif aList[i] in ' ' : # check if there is no spaces
            return 'Error : Your answer have spaces :(' # return error message

    aList[1] = aList[1].strip() # if there are whitespaces, then remove

    if not aList[0] in normalBodyTemp : # check if there is age group which is ont of the given options
        return 'Age group should be one of ' + str(ageList) + ':(' # return error message
    elif not aList[1] in normalBodyTemp[aList[0]] : # check if there is a correct measurement site in age group 
        return 'The measurement site should be one of ' + str(measurementList) + ':(' # return error message
    elif aList[0] == '0~2 years' and aList[1] == 'Oral' : # there are no temperatures of Oral for 0~2 years 
        return 'There are no temperatures of Oral for this age :(' 
        
    try :
        temp = float(aList[2]) # try to convert the temperature to a float type
        if temp < 0 : # check if it is a positive real number
            raise ValueError # error occured
        aList[2] = temp # assign again 
    except ValueError : 
        return 'Error : Body temperature should be a positive real number :(' # return error message

    return True # if everything is ok, return true

def bodyTempCheck (age, measurement, temp) : # function to check if body temperature is normal or not
    if 40.0 < temp or 34.0 > temp : # check if temperature is valid 
        return 'Error occured..'
    elif normalBodyTemp[age][measurement][0] < temp and  normalBodyTemp[age][measurement][1] > temp : #check if temperature is normal
        return 'Your body temperature is normal'
    elif normalBodyTemp[age][measurement][1] < temp : #check if temperature is high
        return 'You have a high fever' 
    else :
        return 'Your body temperature is low' #otherwise, it's low 


def randomFunc (): # function to make a random user input 
    randAge = random.choice(ageList) # randomly choose random age
    randMeasurement = random.choice(measurementList) # randomly choose measurement site
    
    f = random.random() # 0.0 ~ 1.0
    if f < 0.3 : # 30% probability 
        randTemp = random.uniform(-40.0, -1.0) # randomly create negative real number  
    else : # 70% probability 
        temp = normalBodyTemp[randAge][randMeasurement] # get tuple from the dictionary 
        if not temp : # if temperature is empty
            temp = (35.0, 40.0)
            
        tempStart = temp[0] - 1.0 # random temperature from a slightly wider range
        tempEnd = temp[1] + 1.0 # ..
        randTemp = random.uniform(tempStart, tempEnd) # choose a random temperature 

    randList = [randAge, randMeasurement, str(randTemp)] # make a list to return 
    return randList
    
    
print('Welcome :) This program is to record the body temperature and show whether or not it is normal') # welcoming message
print('Let\'s start !!!\n')

ageList = ['0~2 years', '3~10 years', '11~65 years', 'over 65 years'] # list for age group
measurementList = ['Oral', 'Ear', 'Rectal', 'Axillary'] # list for measurement site
curDate = datetime.datetime.now() #datetime.now() variable
curDate = str(curDate) # convert to string
while True:
    answer = input('Type your age group among ' + str(ageList) +',\n' +
                   'the measurement site among ' + str(measurementList) +'\n'+
                   'and your body temperature (should be seperated by ,) : ')

    answer = list(answer.split(',')) # make a list for validation check 
    ans = validationCheck(answer) # return value
    if ans == True : # if the input is valid, then break
        break
    else:
        print(ans + ' try again..\n') # if the input is not valid, then keep repeating

bodyTemp = bodyTempCheck(answer[0],answer[1],answer[2]) # check if body temperature is normal or not


print(curDate, bodyTemp) # print the returned message with the current date and time 
print('\n')

print('***** 10 random auto-testing is starting for body temperature checking and recording *****\n') # auto testing message

newList = [] 
for i in range(10) :
    rand = randomFunc() # get a list of age group, measurement site and temperature 
    ans = validationCheck(rand) # validation check
    if ans == True : # if it is valid, then check the temperature 
        ans = bodyTempCheck(rand[0], rand[1], rand[2]) 

    #save result in a dictionary 
    elem = dict([('Age group', rand[0]), ('measurement site', rand[1]), ('temperature', rand[2]), ('temperature check', ans), ('recorded at', curDate)]) # rand 0 1 2, ans, curDate
    newList.append(elem) # save 10 dictionary variables in a list 
    
print(newList) # print out the list 
    
