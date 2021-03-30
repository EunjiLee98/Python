print('Welcome! This program .....') # Q1 

# body temperature table dictionary 
temperaturerangedict = {'Oral': {'0-2 years':(0, 0), '3-10 years':(35.5, 37.5), '11-65 years':(36.4, 37.6), '> 65 years':(35.8, 36.9)},
                        'Ear':{'0-2 years':(36.4, 38.0), '3-10 years': (36.1, 37.8), '11-65 years': (35.9, 37.6), '> 65 years': (35.8, 37.5)},
                        'Rectal': {'0-2 years':(36.6, 38.0), '3-10 years': (36.6, 38.0), '11-65 years': (37.0, 38.1), '> 65 years': (36.2, 37.3)},
                        'Axillary': {'0-2 years':(34.7, 37.3), '3-10 years': (35.9, 36.7), '11-65 years': (35.2, 36.9), '> 65 years': (35.6, 36.3)}
                        }
agegrouplist = ['0-2 years', '3-10 years', '11-65 years', '> 65 years'] # age group list 

def validateInput(ainputlist): # Q3 
    if len(ainputlist) != 3: # Q3-c, d  
        return 'The number of items must be 3 seperated by comma. (ex: item1, item2, item3)' # Q3-e 

    if not ainputlist[0].strip() in agegrouplist: # Q3-a 
        return 'The age group must be one of ' + str(agegrouplist) + '.' # Q3-e 

    if not ainputlist[1].strip() in temperaturerangedict.keys(): # Q3-a  
        return 'The measurement site must be one of ' + str(list(temperaturerangedict.keys())) + '.' # Q3-e 

    try:
        bodytemp = float(ainputlist[2]) # Q3-b 
        if bodytemp < 0:
            return 'The temperature must be a positive real number.' # Q3-e 
    except:
        return 'The temperature must be a positive real number.' # Q3

    return True # Q3-e 

while True: # Q5
    # Q2 
    userinput = input('\nEnter your age group ('+str(agegrouplist)+'), \nthe masurement site('+str(list(temperaturerangedict.keys()))+'), \nand you body temperature in order, seperating them by , : ')
    userinputlist = userinput.split(',')
    message = validateInput(userinputlist) # Q4 
    if message==True:
        break
    else: # Q5 
        print(message)

# Q6 
def checkBodytemperature(agegroup, measurespot, bodytemperature):
    if agegroup == '0-2 years' and measurespot == 'Oral':
        return 'Measurement Error'
    bodytemperaturelow = temperaturerangedict[measurespot][agegroup][0]
    bodytemperaturehigh = temperaturerangedict[measurespot][agegroup][1]
    if bodytemperaturelow <= bodytemperature <= bodytemperaturehigh:
        return 'Normal Temperature'
    elif bodytemperature > bodytemperaturehigh:
        return 'You have fever. Please see a doctor.'
    else:
        return 'Low Temperature'

# Q7 
checkmessage = checkBodytemperature(userinputlist[0].strip(), userinputlist[1].strip(), float(userinputlist[2]))
from datetime import datetime
timestamp = datetime.now()
# Q7 
print(timestamp, checkmessage)
print()

# Q8 
def randomInput():
    import random
    rgroup = random.choice(agegrouplist)
    rspot = random.choice(list(temperaturerangedict.keys()))
    rerror = random.uniform(0, 1)
    if rerror < 0.3: # Q8-c 
        rtemperature = random.uniform(-18, 0)
    else:
        rtemperature = random.uniform(34, 39) # 34.7 ~ 38.1
    return [rgroup, rspot, rtemperature]

resultlist = list()
for i in range(10): # Q9 
    result = dict() # Q9 
    rinput = randomInput()
    result['age group'] = rinput[0]
    result['measured at'] = rinput[1]
    result['temperature'] = rinput[2]
    message = validateInput(rinput)
    if message==True:
        checkmessage = checkBodytemperature(rinput[0], rinput[1], rinput[2])
        result['temperature check'] = checkmessage
    else: # Q9-b 
        result['temperature check'] = 'Measurement Error'
    result['recorded at'] = str(datetime.now())
    #import time
    #time.sleep(1)
    resultlist.append(result) # Q9-c 
    
print('\nThe 10 random auto-testing for body temperature checking & recording......\n') 
print(resultlist) # Q10 
