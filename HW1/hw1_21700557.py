print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*') #decoration
print('|This program is \'Unit Converter\'                                                        |') #introduce what this program is
print('|There are serveral services for you, and each service has its own number and sub-menus  |') # explanation for user
print('|You can choose one of the services\' numbers you want to convert                         |') # tell how to use
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n') #decoration


print('The list of services') #show the list of services 
print('1. Area','2. Digital Storage','3. Energy','4. Length','5. Mass','6. Pressure','7. Speed','8. Time') #services

validServiceNum = [1,2,3,4,5,6,7,8] #list for valid numbers of service
validItemNum = [1,2,3] #list for valid numbers of submenu
serviceNum = input('The number of service: ') #get service number from the user


#error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
if (serviceNum == '') or (' ' in serviceNum) or (serviceNum.isalpha()) or (int(serviceNum) not in validServiceNum): 
  print('\n')
  print('Your input is wrong..') # tell uesr's input is wrong
  print('It is empty, non-numeric type, out of the item range, or it has spaces') # why it is wrong
  print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
  enterKey = input('Enter key : ') 

  if enterKey == '' : # if user hits enter key, program will be terminated 
    print('Program is terminated...')
    exit(0)
  
else: # if service number is valid 
  serviceNum = int(serviceNum) #type conversion to int 
  if serviceNum == 1 : #Area 
    print('The service you\'ve chosen : Area') #show the service user's chosen
    print('\n') #space for division
    print('There are submenu items of Area') # #tell there are submenu items of Digital Storage
    print('1. Square meter to Square inch','2. Square yard to Square foot','3. Square foot to Square inch') #submenu items of Area
    itemNum = input('The number of submenu item: ') #get item's number from user

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') #get enter key from user
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int 
      if itemNum == 1 : # 1. convert Square meter to Square inch
        print('The submenu item you\'ve chosen : Square meter to Square inch') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Square meter to the value of Square inch') # guide the user to enter an appropriate form of input (what user supposed to enter)
        squareMeter = float(input('The value of Square meter : ')) #get input from the user 
        print('\n') #space for division

        #error handling
        if squareMeter < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        squareInch = squareMeter * 1550 # calculation to convert the value of Square meter to the value of Square inch 
        print('The value converted from Square meter to Square inch : %.2f'%squareInch) # print the result of calculation 

      elif itemNum == 2 : # 2. convert Square yard to Square foot
        print('The submenu item you\'ve chosen : Square yard to Square foot') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Square yard to the value of Square foot') # guide the user to enter an appropriate form of input (what user supposed to enter)
        squareYard = float(input('The value of Square yard : ')) #get input from the user 
        print('\n') #space for division

        #error handling
        if squareYard < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        squareFoot = squareYard * 9 # calculation to convert the value of Square yard to the value of Square foot
        print('The value converted from Square yard to Square foot : %.2f'%squareFoot) # print the result of calculation 

      elif itemNum == 3 : # 3. convert Square foot to Square inch
        print('The submenu item you\'ve chosen : Square foot to Square inch') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Square foot to the value of Square inch') # guide the user to enter an appropriate form of input (what user supposed to enter)
        squareFoot = float(input('The value of Square foot : ')) #get input from the user 
        print('\n') #space for division

        #error handling
        if squareFoot < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        squareInch = squareFoot * 144 # calculation to convert the value of Square foot to the value of Square inch
        print('The value converted from Square foot to Square inch : %.2f'%squareInch) # print the result of calculation 

  elif serviceNum == 2 : # Digital Storage
    print('The service you\'ve chosen : Digital Storage') #show the service user's chosen
    print('\n')  #space for division
    print('There are submenu items of Digital Storage') #tell there are submenu items of Digital Storage
    print('1. Bit to Byte','2. Megabit to Kilobyte','3. Kilobit to Bit') #submenus for Digital Storage
    itemNum = input('The number of submenu item: ') #get item's number from user
 
    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') # get enter key from the user
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int 
      if itemNum == 1 : # 1. Bit to Byte
        print('The submenu item you\'ve chosen : Bit to Byte') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Bit to the value of Byte')  # guide the user to enter an appropriate form of input (what user supposed to enter)
        bit = float(input('The value of Bit : '))  #get input from the user
        print('\n')  #space for division

        #error handling
        if bit < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        byte = bit / 8 # calculation to convert the value of Bit to the value of Byte
        print('The value converted from Bit to Byte : %.2f'%byte) # print the result of calculation 

      elif itemNum == 2 : # 2. Megabit to Kilobyte
        print('The submenu item you\'ve chosen : Megabit to Kilobyte') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Megabit to the value of Kilobyte') # guide the user to enter an appropriate form of input (what user supposed to enter)
        megaBit = float(input('The value of Megabit : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if megaBit < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')  # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        kiloByte = megaBit * 125 # calculation to convert the value of Megabit to the value of Kilobyte
        print('The value converted from Megabit to Kilobyte : %.2f'%kiloByte) # print the result of calculation 

      elif itemNum == 3 : # 3. Kilobit to Bit
        print('The submenu item you\'ve chosen : Kilobit to Bit') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Kilobit to the value of bit') # guide the user to enter an appropriate form of input (what user supposed to enter)
        kiloBit = float(input('The value of Kilobit : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if kiloBit < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        bit = kiloBit* 1000 # calculation to convert the value of kilobit to the value of bit
        print('The value converted from Kilobit to Bit : %.2f'%bit) # print the result of calculation 

  elif serviceNum == 3 : # Energy
    print('The service you\'ve chosen : Energy') #show the service user's chosen
    print('\n') #space for division
    print('There are submenu items of Energy') #tell there are submenu items of Digital Storage
    print('1. Joule to Gram calorie','2. Kilocalorie to Watt hour','3. Kilowatt hour to Kilojoule') #submenus for Energy
    itemNum = input('The number of submenu item: ') #get item's number from user

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int 
      if itemNum == 1 : # 1. Joule to Gram calorie
        print('The submenu item you\'ve chosen : Joule to Gram calorie') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Joule to the value of Gram calorie') # guide the user to enter an appropriate form of input (what user supposed to enter)
        joule = float(input('The value of Joule : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if joule < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        gramCalorie = joule / 4.184 # calculation to convert the value of Joule to the value of Gram calorie
        print('The value converted from Joule to Gram calorie : %.2f'%gramCalorie) # print the result of calculation 

      elif itemNum == 2 : # 2. Kilocalorie to Watt hour
        print('The submenu item you\'ve chosen : Kilocalorie to Watt hour') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Kilocalorie to the value of Watt hour') # guide the user to enter an appropriate form of input (what user supposed to enter)
        kiloCalroie = float(input('The value of Kilocalorie : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if kiloCalroie < 0 :  #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        wattHour= kiloCalroie * 1.162 # calculation to convert the value of Kilocalorie to the value of Watt hour
        print('The value converted from Kilocalorie to Watt hour : %.2f'%wattHour) # print the result of calculation 

      elif itemNum == 3 : # 3. Kilowatt hour to Kilojoule
        print('The submenu item you\'ve chosen : Kilowatt hour to Kilojoule') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Kilowatt hour to the value of Kilojoule') # guide the user to enter an appropriate form of input (what user supposed to enter)
        kiloWattHour = float(input('The value of Kilowatt hour : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if kiloWattHour < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') # get enter key from the user
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0) # termination

        kiloJoule = kiloWattHour * 3600 # calculation to convert the value of Kilowatt hour to the value of Kilojoule
        print('The value converted from Kilowatt hour to Kilojoule : %.2f'%kiloJoule) # print the result of calculation 

  
  elif serviceNum == 4 : #Length
    print('The service you\'ve chosen : Length') #show the service user's chosen
    print('\n') #space for division
    print('There are submenu items of Length') 
    print('1. Meter to Millimetre','2. Centimeter to Micrometres','3. Mile to Kilometre') #submenus for Length
    itemNum = input('The number of submenu item: ')  #get item's number from user

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int 
      if itemNum == 1 : # 1. Meter to Millimetre
        print('The submenu item you\'ve chosen : Meter to Millimetre') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Meter to the value of Millimetre') # guide the user to enter an appropriate form of input (what user supposed to enter)
        meter= float(input('The value of Meter : ')) #get input from the user
        print('\n') #space for division

        #error handling
        if meter < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')  # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        milliMetre = meter * 1000 # calculation to convert the value of Meter to the value of Millimetre
        print('The value converted from Meter to Millimetre : %.2f'%milliMetre) # print the result of calculation 

      elif itemNum == 2 : # 2. Centimeter to Micrometres
        print('The submenu item you\'ve chosen : Centimeter to Micrometres') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Centimeter to the value of Micrometres') # guide the user to enter an appropriate form of input (what user supposed to enter)
        centiMeter = float(input('The value of Kilocalorie : '))  #get input from the user
        print('\n') #space for division

        #error handling
        if centiMeter < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')  # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        microMetres = centiMeter * 10000  # calculation to convert the value of Centimeter to the value of Micrometres
        print('The value converted from Centimeter to Micrometres : %.2f'%microMetres) # print the result of calculation 

      elif itemNum == 3 : # 3. Mile to Kilometre
        print('The submenu item you\'ve chosen : Mile to Kilometre') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Mile to the value of Kilometre') # guide the user to enter an appropriate form of input (what user supposed to enter)
        mile = float(input('The value of Mile : '))   #get input from the user
        print('\n') #space for division

        #error handling
        if mile < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        kiloMetre = mile * 1.609 # calculation to convert the value of Mile to the value of Kilometre
        print('The value converted from Mile to Kilometre : %.2f'%kiloMetre) # print the result of calculation 


  elif serviceNum == 5 : #Mass
    print('The service you\'ve chosen : Mass') #show the service user's chosen
    print('\n') #space for division
    print('There are submenu items')
    print('1. Kilogram to Gram','2. Stone to Kilogram','3. Pound to Gram') #submenus for Mass
    itemNum = input('The number of submenu item: ') #get item's number from user

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, has spaces or out of the item range') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int
      if itemNum == 1 : # 1. Kilogram to Gram
        print('The submenu item you\'ve chosen : Kilogram to Gram') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Kilogram to the value of Gram') # guide the user to enter an appropriate form of input (what user supposed to enter)
        kiloGram = float(input('The value of Kilogram : ')) #get input from the user
        print('\n')

        # error handling
        if kiloGram < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..') # tell the user why it is wrong 
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        gram = kiloGram * 1000 # calculation to convert the value of Kilogram to the value of Gram
        print('The value converted from Kilogram to Gram : %.2f'%gram) # print the result of calculation 

      elif itemNum == 2 : # 2. Stone to Kilogram
        print('The submenu item you\'ve chosen : Stone to Kilogram') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Stone to the value of Kilogram') # guide the user to enter an appropriate form of input (what user supposed to enter)
        stone = float(input('The value of Stone : ')) #get input from the user
        print('\n') #space for division

        # error handling
        if stone < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        kiloGram = stone * 6.35 # calculation to convert the value of Stone to the value of Kilogram
        print('The value converted from Stone to Kilogram : %.2f'%kiloGram) # print the result of calculation 

      elif itemNum == 3 : # 3. Pound to Gram
        print('The submenu item you\'ve chosen : Pound to Gram') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Pound to the value of Gram') # guide the user to enter an appropriate form of input (what user supposed to enter)
        pound = float(input('The value of Pound : ')) #get input from the user
        print('\n') #space for division

        # error handling 
        if pound < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        gram = pound * 454 # calculation to convert the value of Pound to the value of Gram
        print('The value converted from Pound to Gram : %.2f'%gram) # print the result of calculation 


  elif serviceNum == 6 : #Pressure
    print('The service you\'ve chosen : Pressure')  #show the service user's chosen
    print('\n') #space for division
    print('There are submenu items')
    print('1. Bar to Pascal','2. Pound-force per square inch to Torr','3. Standard atmosphere to Bar') #submenus for Pressure
    itemNum = input('The number of submenu item: ') #get item's number from user

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces')# show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int
      if itemNum == 1 : # 1. Bar to Pascal
        print('The submenu item you\'ve chosen : Bar to Pascal') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Bar to the value of Pascal') # guide the user to enter an appropriate form of input (what user supposed to enter)
        bar = float(input('The value of Bar : ')) 
        print('\n')

        #error handling
        if bar < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        pascal = bar * 100000 # calculation to convert the value of Bar to the value of Pascal
        print('The value converted from Bar to Pascal : %.2f'%pascal) # print the result of calculation 

      elif itemNum == 2 : # 2. Pound-force per square inch to Torr
        print('The submenu item you\'ve chosen : Pound-force per square inch to Torr') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Pound-force per square inch to the value of Torr') # guide the user to enter an appropriate form of input (what user supposed to enter)
        poundForcePerSquareInch = float(input('The value of Pound-force per square inch : '))
        print('\n')

        #error handling
        if poundForcePerSquareInch < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        torr = poundForcePerSquareInch * 51.715 # calculation to convert the value of Pound-force per square inch to the value of Torr
        print('The value converted from Pound-force per square inch to Torr : %.2f'%torr) # print the result of calculation 

      elif itemNum == 3 : # 3. Standard atmosphere to Bar
        print('The submenu item you\'ve chosen : Standard atmosphere to Bar') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Standard atmosphere to the value of Bar') # guide the user to enter an appropriate form of input (what user supposed to enter)
        standardAtmosphere = float(input('The value of Standard atmosphere : '))
        print('\n')

        #error handling
        if standardAtmosphere < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        bar = standardAtmosphere * 1.103 # calculation to convert the value of Standard atmosphere to the value of Bar
        print('The value converted from Standard atmosphere to Bar : %.2f'%bar) # print the result of calculation 


  elif serviceNum == 7 : #Speed
    print('The service you\'ve chosen : Speed')  #show the service user's chosen
    print('\n')
    print('There are submenu items')
    print('1. Meter per second to Kilometer per hour','2. Miles per hour to Foot per second','3. Kilometer per hour to Knot') #submenus for Speed
    itemNum = input('The number of submenu item: ')

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int
      if itemNum == 1 : # 1. Meter per second to Kilometer per hour
        print('The submenu item you\'ve chosen : Meter per second to Kilometer per hour') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Meter per second to the value of Kilometer per hour') # guide the user to enter an appropriate form of input (what user supposed to enter)
        meterPerSecond = float(input('The value of Meter per second : '))
        print('\n')

        #error handling
        if meterPerSecond < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        kilometerPerHour = meterPerSecond * 3.6 # calculation to convert the value of Meter per second to the value of Kilometer per hour
        print('The value converted from Meter per second to Kilometer per hour : %.2f'%kilometerPerHour) # print the result of calculation 

      elif itemNum == 2 : # 2. Miles per hour to Foot per second
        print('The submenu item you\'ve chosen : Miles per hour to Foot per second') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Miles per hour to the value of Foot per second') # guide the user to enter an appropriate form of input (what user supposed to enter)
        milesPerHour = float(input('The value of Miles per hour : '))
        print('\n')

        #error handling
        if milesPerHour < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        footPerSecond = milesPerHour * 1.467 # calculation to convert the value of Miles per hour to the value of Foot per second
        print('The value converted from Miles per hour to Foot per second : %.2f'%footPerSecond) # print the result of calculation 

      elif itemNum == 3 : # Kilometer per hour to Knot
        print('The submenu item you\'ve chosen : Kilometer per hour to Knot') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Kilometer per hour to the value of Knot') # guide the user to enter an appropriate form of input (what user supposed to enter)
        kilometerPerHour = float(input('The value of Kilometer per hour : '))
        print('\n')

        #error handling
        if kilometerPerHour < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        knot = kilometerPerHour / 1.852 # calculation to convert the value of Kilometer per hour to the value of Knot
        print('The value converted from Kilometer per hour to Knot: %.2f'%knot) # print the result of calculation 


  elif serviceNum == 8 : #Time
    print('The service you\'ve chosen : Time')  #show the service user's chosen
    print('\n')
    print('There are submenu items')
    print('1. Century to Month','2. Decade to Week','3. Calendar year to Day') #submenus for Time
    itemNum = input('The number of submenu item: ')

    #error handling : if the number is empty, non-numeric type, has spaces or out of the item range, 
    if (itemNum == '') or (' ' in itemNum) or (itemNum.isalpha()) or (int(itemNum) not in validItemNum): 
      print('\n')
      print('Your input is wrong..') # tell uesr's input is wrong
      print('It is empty, non-numeric type, out of the item range, or it has spaces') # show why it is wrong
      print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user to terminate the program
      enterKey = input('Enter key : ') 
      if enterKey == '' : # if user hits enter key, program will be terminated 
        print('Program is terminated...')
        exit(0) # termination

    else : # if item number is valid
      itemNum = int(itemNum) #type conversion to int
      if itemNum == 1 : # 1. Century to Month
        print('The submenu item you\'ve chosen : Century to Month') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Century to the value of Month') # guide the user to enter an appropriate form of input (what user supposed to enter)
        century = float(input('The value of Century : '))
        print('\n')

        #error handling
        if century < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        month = century * 1200 # calculation to convert the value of Century to the value of Month
        print('The value converted from Century to Month : %.2f'%month) # print the result of calculation 

      elif itemNum == 2 : # 2. Decade to Week
        print('The submenu item you\'ve chosen : Decade to Week') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Decade to the value of Week') # guide the user to enter an appropriate form of input (what user supposed to enter)
        decade = float(input('The value of Decade : '))
        print('\n')

        #error handling
        if decade < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        week = decade * 521 # calculation to convert the value of Decade to the value of Week
        print('The value converted from Decade to Week : %.2f'%week) # print the result of calculation 

      elif itemNum == 3 : # 3. Calendar year to Day
        print('The submenu item you\'ve chosen : Calendar year to Day') #show the item user's chosen 
        print('\n') #space for division
        print('You should enter the correct value (positive number) to convert the value of Calendar year to the value of Day') # guide the user to enter an appropriate form of input (what user supposed to enter)
        calendarYear = float(input('The value of Calendar year : '))
        print('\n')

        #error handling
        if calendarYear < 0 : #if user input is negative number, program will be terminated when user hits enter key
          print('Your input is negative number..')
          print('Because of that, this program will be terminated when you hit the enter key') # get comfirmation from the user
          enterKey = input('Enter key : ') 
          if enterKey == '' : # if user hits enter key, program will be terminated 
            print('Program is terminated...')
            exit(0)

        day = calendarYear * 365 # calculation to convert the value of Calendar year to the value of Day
        print('The value converted from Calendar year to Day: %.2f'%day) # print the result of calculation 