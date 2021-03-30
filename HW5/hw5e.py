########### from HW4 ##########
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
        return 'The temperature must be a positive real number.' # Q3-e 

    return True # Q3-e 

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


########## HW5 GUI ##########
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *     
from tkinter.scrolledtext import *
from tkinter import messagebox

# function for the random input button
def randomInputAssign():
    rinput = randomInput() # from HW4
    agegroup.set(agegrouplist.index(rinput[0])+1) # to GUI 
    measuresite.set(list(temperaturerangedict.keys()).index(rinput[1])+1) # to GUI 
    temperature.set(rinput[2]) # to GUI

# function for the temperature test button
nTest=0
def run():
    if agegroup.get()==0: # if the age radiobutton is NOT selected 
        messagebox.showerror('Error', 'Choose your age group')
    elif measuresite.get()==0: # if the site radiobutton is NOT selected
        messagebox.showerror('Error', 'Choose the measurement site')
    else:
        sel_agegroup = agegrouplist[agegroup.get()-1]
        sel_measuresite = list(temperaturerangedict.keys())[measuresite.get()-1]
        sel_temperature = temperature.get()

        message = validateInput([sel_agegroup, sel_measuresite, sel_temperature]) # from HW4
        if message==True:
            # from HW4
            checkmessage = checkBodytemperature(sel_agegroup, sel_measuresite, float(sel_temperature))
            if checkmessage == 'Normal Temperature':
                messagebox.showinfo('Test Result', checkmessage)
            elif checkmessage == 'You have fever. Please see a doctor.':
                messagebox.showerror('Test Result', checkmessage)
            else:
                messagebox.showwarning('Test Result', checkmessage)

            # to ScrolledText
            from datetime import datetime
            timestamp = datetime.now()
            t1.insert(END, str(timestamp)+'\t'+sel_agegroup+'\t'+sel_measuresite+'\t'+sel_temperature+'\t'+checkmessage+'\n')
            global nTest
            nTest+=1 # count the number of records 
            # reset values in input widgets
            agegroup.set(0) 
            measuresite.set(0) 
            temperature.set('') 
            
        else: 
            messagebox.showerror('Error', message)


# function for the file save button
def savefile():
    savefilename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", '*.txt')]) # file save dialog
    if savefilename is None or savefilename=='': # asksaveasfile return `None` if dialog closed with "cancel".
        return
    savefilefile = open(savefilename, 'w')
    savefilefile.write(t1.get(1.0, END))
    savefilefile.close()
    # success
    global nTest
    messagebox.showinfo('Save Result', 'Total '+str(nTest)+' records are saved at '+savefilename)
    nTest=0
    t1.delete(1.0, END) # reset the contents of ScrolledText

# Top-level window
root = Tk()
# program title
root.title("Body Temperature Recorder")

# frame for input widgets
frame_input = ttk.Frame(root, padding="13 13 12 12")
frame_input.pack()

# radiobuttons for the age group options
agegroup = IntVar()
ttk.Label(frame_input, text="Choose your age group", width=25).grid(row=1, column=1)
ttk.Radiobutton(frame_input, text='0-2 years', variable=agegroup, value=1).grid(row=1, column=2)
ttk.Radiobutton(frame_input, text='3-10 years', variable=agegroup, value=2).grid(row=1, column=3)
ttk.Radiobutton(frame_input, text='11-65 years', variable=agegroup, value=3).grid(row=1, column=4)
ttk.Radiobutton(frame_input, text='> 65 years', variable=agegroup, value=4).grid(row=1, column=5)

# radiobutton for the measurement site options
measuresite = IntVar()
ttk.Label(frame_input, text="Choose the measurement site", width=25).grid(row=2, column=1)
ttk.Radiobutton(frame_input, text='Oral', variable=measuresite, value=1).grid(row=2, column=2, sticky=W)
ttk.Radiobutton(frame_input, text='Ear', variable=measuresite, value=2).grid(row=2, column=3, sticky=W)
ttk.Radiobutton(frame_input, text='Rectal', variable=measuresite, value=3).grid(row=2, column=4, sticky=W)
ttk.Radiobutton(frame_input, text='Axillary', variable=measuresite, value=4).grid(row=2, column=5, sticky=W)

# text entry for the body temperature
temperature = StringVar()
ttk.Label(frame_input, text="Temperature", width=25).grid(row=3, column=1)
ttk.Entry(frame_input, textvariable=temperature, width=20).grid(row=3, column=2, columnspan=4, sticky=W)

# button for generating random inputs
ttk.Button(frame_input, text="Random input for all", command=randomInputAssign, width=70).grid(row=4, column=1, columnspan=5)

# frame for output widgets
frame_output = ttk.Frame(root, padding="13 13 12 12")
frame_output.pack()

# button for checking the body temperature
ttk.Button(frame_output, text="Test the input", command=run).pack()

# multiline text for recording results
t1 = ScrolledText(frame_output, height = 10, width=80)
t1.pack()

# button for saving records in a file
ttk.Button(frame_output, text="Save as a file", command=savefile).pack()

# show up the top-level window
root.mainloop()
    




