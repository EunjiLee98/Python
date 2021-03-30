from tkinter import *
import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter.scrolledtext import *
from tkinter.filedialog import *


count = 0 # used for counting how many records are saved
ageString = '' # used for validation to insert age group in results 
measurementString = ''# used for validation to insert measurement in results 
txt = '' # used for getting entire contents 


#<-----function for random input----->
def randomInput():
    import random
    #print('random input sucessfully...')
    rgroup = random.choice(agegrouplist) # choose random age group
    rspot = random.choice(list(temperaturerangedict.keys()))# choose random age measurement site
    rerror = random.uniform(0, 1) # choose random body temperature
    if rerror < 0.3: # Q8-c 
        rtemperature = random.uniform(-18, 0)
    else:
        rtemperature = random.uniform(34, 39) # 34.7 ~ 38.1
        
    #<-----automatically fill input widgets----->
    if rgroup == "0-2 years" : # compare which years match with age group
        ageRadio1.select() # if it is matched, then automatically first radio button will be selected
    elif rgroup == "3-10 years" : 
        ageRadio2.select() # second radio button will be selected
    elif rgroup == "11-65 years" : 
        ageRadio3.select() # third radio button will be selected
    else :
        ageRadio4.select() # fourth radio button will be selected

    if rspot == "Oral" : # compare with spots match with measurement site 
        measurementRadio1.select() # if it is matched, then automatically first radio button will be selected
    elif rspot == "Ear" :
        measurementRadio2.select() # second radio button will be selected
    elif rspot == "Rectal" :
        measurementRadio3.select() # third radio button will be selected
    else :
        measurementRadio4.select() # fourth radio button will be selected

    entry.delete(0,"end") # clear textbox for random temperature 
    entry.insert(0,rtemperature) # insert random temperature 


#<-----function for validation----->
def validateInput(): # Q3
    tempAge = ageSelected.get() # get integer value from selected age group
    tempMeasurement = measurementSelected.get() # get integer value from selected measurement site

    #print('validation function')
    if tempAge == 1 : # same algorithm as above
        ageString = "0-2 years" 
    elif tempAge == 2 : # =
        ageString = "3-10 years"
    elif tempAge == 3 : # =
        ageString = "11-65 years"
    elif tempAge == 4: # =
        ageString = "> 65 years"
    else : 
        ageString = '' # if there is no selected button

    if tempMeasurement == 1 : # same algorithm as above
        measurementString = "Oral"
    elif tempMeasurement == 2 : # =
        measurementString = "Ear" 
    elif tempMeasurement == 3 : # =
        measurementString = "Rectal"
    elif tempMeasurement == 4: # =
        measurementString = "Axillary"
    else : 
        measurementString = '' # if there is no selected button

    if ageString == '' : # if there is no selected button for age group
        messagebox.showinfo("Error ocurred", "The age group button must be selected")
        return 
    else :
        if not ageString in agegrouplist: # if there is no age group 
            messagebox.showinfo("Error ocurred", "The age group must be one of " + str(agegrouplist) + '.')
            return
     
    if measurementString == '' : # if there is no selected button for measurement site
        messagebox.showinfo("Error ocurred", "The measurement sites button must be selected")
        return
    else : # if there is no measurement site
        if not measurementString in temperaturerangedict.keys(): 
            messagebox.showinfo("Error ocurred", "The measurement site must be one of " + str(list(temperaturerangedict.keys())) + '.')
            return
            
    bodytemp = entry.get() # get body temperature 
    if bodytemp == '' : # if there is no input for body temperature 
        messagebox.showinfo("Error ocurred", "The temperature must be filled out")
        return
    else :
        bodytemp = float(bodytemp)
        if bodytemp < 0: # if body temperature is negative 
            messagebox.showinfo("Error ocurred", "The temperature must be a positive real number.")
            return
        
    #<-----keep record----->
    from datetime import datetime
    timestamp = datetime.now() # get date and time
    checkmessage = checkBodytemperature(ageString,measurementString,bodytemp) # get check message

    resultList = [timestamp,ageString,measurementString,bodytemp,checkmessage] # make all information in a list 
    result.insert(END, resultList) # insert into result
    result.insert(END,'\n')

    global count
    count += 1 # count how many records 

    global txt # get entire records 
    txt = result.get("1.0", tk.END)

    deselect() # deselect all in order to receive next input 
    
#<-----deselect----->
def deselect(): 
    ageSelected.set(5) # there is no 5, so it will choose nothing 
    measurementSelected.set(5) # same above
    entry.delete(0,"end") # delect all from entry 

#<-----function for checking body temperature----->
def checkBodytemperature(agegroup, measurespot, bodytemperature):
    #print('checkBodytemperature function')
    if agegroup == '0-2 years' and measurespot == 'Oral':
        messagebox.showinfo("Result", 'Measurement Error') # pop-up error message
        return 'Measurement Error'
    
    bodytemperaturelow = temperaturerangedict[measurespot][agegroup][0]
    bodytemperaturehigh = temperaturerangedict[measurespot][agegroup][1]
    
    if bodytemperaturelow <= bodytemperature <= bodytemperaturehigh:
        messagebox.showinfo("Result", 'Normal Temperature') # pop-up the result 
        return 'Normal Temperature'
    elif bodytemperature > bodytemperaturehigh:
        messagebox.showerror("Result",'You have fever. Please see a doctor.') # pop-up the result
        return 'You have fever. Please see a doctor.' 
    else:
        messagebox.showwarning("Result",'Low Temperature') # pop-up the result
        return 'Low Temperature'

    
def fileFunc() : #function to save in a file
    global count
    
    name = askopenfilename()
    f = open(name, 'r+')
    f.write(txt)
    result.delete(1.0, tk.END)
    outputText = str(count) + ' records are saved in ' + name #pop-up where and how many records are saved
    f.close()
    messagebox.showinfo(title="Result", message=outputText)
       
    count = 0 # make count value zero for next 
    
"""
MAIN FUNCTION
"""

window = tk.Tk()
window.title("Thermometer program made by Eunji Lee")
window.geometry("800x800+100+100")
window.resizable(False, False)

#<-----body temperature table dictionary----->
temperaturerangedict = {'Oral': {'0-2 years':(0, 0), '3-10 years':(35.5, 37.5), '11-65 years':(36.4, 37.6), '> 65 years':(35.8, 36.9)},
                        'Ear':{'0-2 years':(36.4, 38.0), '3-10 years': (36.1, 37.8), '11-65 years': (35.9, 37.6), '> 65 years': (35.8, 37.5)},
                        'Rectal': {'0-2 years':(36.6, 38.0), '3-10 years': (36.6, 38.0), '11-65 years': (37.0, 38.1), '> 65 years': (36.2, 37.3)},
                        'Axillary': {'0-2 years':(34.7, 37.3), '3-10 years': (35.9, 36.7), '11-65 years': (35.2, 36.9), '> 65 years': (35.6, 36.3)}
                        }
agegrouplist = ['0-2 years', '3-10 years', '11-65 years', '> 65 years'] # age group list

#<-----Font&Title setting----->
fontForTitle=tk.font.Font(family="맑은 고딕", size=20)
fontForOther=tk.font.Font(family="맑은 고딕", size=16)

title=tk.Label(window, text="Thermometer program",font = fontForTitle, anchor = "w", width=70, height=1)
title['bg'] = '#ffccc8'
title.pack()

#<-----Radiobutton setting----->
ageSelected = tk.IntVar() # used for getting integer value
measurementSelected = tk.IntVar()

#<-----age groups----->
ageFrame = tk.Frame(window) # frame for age group
ageFrame.pack(pady = "6m", padx=5, fill=tk.X)

ageLabel = tk.Label(ageFrame, text="Age groups", font = fontForOther, width=15, anchor="w") # label for age group
ageLabel.pack(side="left", padx=5)

optionFrame = Frame(ageFrame) #frame for radio buttons for age group
optionFrame.pack(side="left", padx=5)

ageRadio1 = tk.Radiobutton(optionFrame, text="0-2 years", value=1, variable=ageSelected) #radio button 1 for age group 
ageRadio1.pack(side="left")
 
ageRadio2 = tk.Radiobutton(optionFrame, text="3-10 years", value=2, variable=ageSelected) #radio button 2 for age group
ageRadio2.pack(side="left")

ageRadio3 = tk.Radiobutton(optionFrame, text="11-65 years", value=3, variable=ageSelected) #radio button 3 for age group 
ageRadio3.pack(side="left")

ageRadio4 = tk.Radiobutton(optionFrame, text="> 65 years", value=4, variable=ageSelected) #radio button 4 for age group 
ageRadio4.pack(side="left")

#<-----measurement sites----->
measurementFrame = Frame(window) # frame for measurement sites 
measurementFrame.pack(side="top", pady = "3m", fill=tk.X, padx=5)

measurementLabel = tk.Label(measurementFrame, text="Measurement sites", font = fontForOther, width=15, anchor="w") # label for measurement sites
measurementLabel.pack(side="left", padx=5)

option2Frame = Frame(measurementFrame) # frame for radio buttons for measurement sites 
option2Frame.pack(side="left", padx=5)
 
measurementRadio1 = tk.Radiobutton(option2Frame, text="Oral", value = 1, variable=measurementSelected) #radio button 1 for Measurement site
measurementRadio1.pack(side="left")

measurementRadio2 = tk.Radiobutton(option2Frame, text="Ear", value = 2, variable=measurementSelected) #radio button 2 for Measurement site
measurementRadio2.pack(side="left")

measurementRadio3 = tk.Radiobutton(option2Frame, text="Rectal", value = 3, variable=measurementSelected) #radio button 3 for Measurement site 
measurementRadio3.pack(side="left")

measurementRadio4 = tk.Radiobutton(option2Frame, text="Axillary", value = 4, variable=measurementSelected) #radio button 4 for Measurement site 
measurementRadio4.pack(side="left")

#<-----Body temperature----->
bodyFrame = Frame(window) # frame for label for body temperature 
bodyFrame.pack(side="top", pady = "6m", fill=tk.X, padx=5)

bodyLabel = tk.Label(bodyFrame, text="Body temperature", font = fontForOther, width=15, anchor="w") # label for body temperature
bodyLabel.pack(side="left", padx=5)

option3Frame = Frame(bodyFrame) # frame for entry
option3Frame.pack(side="left", padx=5)
entry = tk.Entry(option3Frame)
entry.pack()

deselect() # function to deselect 

#<-----random button for random input----->
randomFrame = Frame(window) #frame for random button
randomFrame.pack(side="top", pady = "6m", fill=tk.X, padx=5)

randomButton = tk.Button(randomFrame, highlightbackground='#ff9999',text="Button to generate random input",
                         relief="solid", anchor="center", width=80, font=fontForOther,
                         height=2, highlightcolor='#f498fd', command=randomInput)
randomButton.pack()
    
#<-----test button for temperature----->
testFrame = Frame(window) #frame for test button
testFrame.pack(side="top", pady = "3m", fill=tk.X, padx=5)

testButton = tk.Button(testFrame, highlightbackground='#ff99ff',text="Button to test the temperature",
                         relief="solid", anchor="center", width=80, font=fontForOther,
                         height=2, highlightcolor='#f498fd', command=validateInput)
testButton.pack()

testResultFrame = Frame(window) # frame for test result
testResultFrame.pack(side="top", pady = "3m", fill=tk.X, padx=5)

testResultTitle=tk.Label(testResultFrame, text="Temperature Test Results (Accumulated)",
                             font = fontForOther, anchor = "w", width=80, height=2)
testResultTitle.pack()

#<-----textbox for test result----->
resultFrame = tk.Frame(window) # frame for textbox for test result
resultFrame.pack(fill=tk.X)

result = ScrolledText(resultFrame, bg = '#ffe6cc', height = 10, width=120)
result.pack()
    
#<-----file button for saving the results----->
fileFrame = Frame(window) # frame for file button
fileFrame.pack(side="top", pady = "3m", fill=tk.X, padx=5)

fileButton = tk.Button(fileFrame, highlightbackground='#ccffcc',text="Button to save the results in a file",
                         relief="solid", anchor="center", width=80, font=fontForOther,
                         height=2, highlightcolor='#33ff33', command=fileFunc)
fileButton.pack()

window.mainloop()
