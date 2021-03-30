print('Unit Converter\nWe provide the best unit conversion service in the world!')  # Q1
serviceList = ['1. Length', '2. Temperature', '3. Plane Angle', '4. Mass', '5. Area', '6. Volume', '7. Time']                 # Q2-A 7 services 
print('The services that you can enjoy are\n',serviceList)                                                    # Q2 
selService = input('Choose the service number: ')                                                            # Q2-B select
if not selService.isdecimal():                                                                              # Q2-C wrong input
  print('Wrong input.\nThe program will be terminated.')                                                       # Q2-C 
  input()                                                                                                   # Q2-C terminate after enter
else:                                                                                                       # Q2 
  selService = int(selService)                                                                              # Q2 
  if selService < 1 or selService > 7:                                                                      # Q2-C out of service range
    print('Out of the service range.\nThe program will be terminated.')                                     # Q2-C 
    input()                                                                                                 # Q2-C terminate after enter
  else:                                                                                                     # Q3      
    submenuList = [['1. cm > inches', '2. km > miles', '3. feet > m'],['1. Celsius > Fahrenheit', '2. Celsius > Kelvin', '3. Fahrenheit > Kelvin'],
		   ['1. Degrees > Radians', '2. Degrees > Minute of arc', '3. Radians > Degrees'],
                   ['1. kg > pounds', '2. oz > g', '3. kg > oz'],['1. Squared meters > Squared yards', '2. Squared kilometers > Hectare', '3. Acre > Hectare'],
                   ['1. Liter > Cubic meter', '2. Liter > Cubic foot', '3. Cubit meter > Cubit foot'],['1. Day > Seconds', '2. Week > Minutes', '3. Month > Hours']]
                                                                                                            # Q3-A submenu for each service (list of lists)
                                                                                                            
    print('The menu for \''+ serviceList[selService-1][3:]+'\'', 'is', submenuList[selService-1])              # Q3 
    selItem= input('Choose the menu number: ')                                                                                       # Q3-B select
    if not selItem.isdecimal():                                                                                                           # Q3-C wrong input
      print('Wrong input.\nThe program will be terminated.')                                                                                 # Q3-C 
      input()                                                                                                                             # Q3-C terminate after enter
    else:                                                                                                                                 # Q3 
      selItem = int(selItem)                                                                                                              # Q3 
      if selItem < 1 or selItem > 3:                                                                                                      # Q3-C out of menu
        print('Out of the menu range.\nThe program will be terminated.')                                                                 # Q3-C 
        input()                                                                                                                           # Q3-C terminate after enter
      else:                                                                                                                               # Q4
        print('The selected service menu: \''+ serviceList[selService-1][3:]+'\' -', '\''+ submenuList[selService-1][selItem-1][3:]+'\'')    # Q4-A 
        unitValue = input('Enter the value to convert. Only positive integers are valid: ')                                                    # Q4-A 
        if not unitValue.isdecimal():                                                                                                     # Q4-B wrong input
          print('Wrong input.\nThe program will be terminated.')                                                                             # Q4-B 
          input()                                                                                                                         # Q4-B terminate after enter
        else:                                                                                                                             # Q4 
          unitValue = int(unitValue)                                                                                                      # Q4 
          if unitValue < 1:                                                                                                               # Q4-B not positive value
            print('Wrong input.\nThe program will be terminated.')                                                                           # Q4-B 
            input()                                                                                                                       # Q4-B terminate after enter
          else:                                                   # Q4-C Google Unit Converter's formular 
            if selService == 1:                                   # Service 1 Length conversion
              divValueList = [2.54, 1.609, 3.281]                 
              conValue = unitValue / divValueList[selItem-1]
            elif selService == 2:                                 # Service 2 Temperature conversion
              if selItem == 1:                                    
                conValue = (unitValue * 9/5) + 32
              elif selItem == 2:                                  
                conValue = unitValue + 273.15
              elif selItem == 2:                                  
                conValue = (unitValue-32) * 5/9 + 273.15
            elif selService == 3:                                 # Service 3 Plane Angle conversion
              mulValueList = [3.14/180, 60, 180/3.14]             
              conValue = unitValue * mulValueList[selItem-1]
            elif selService == 4:                                 # Service 4 Mass conversion
              mulValueList = [2.205, 28.35, 35.274]               
              conValue = unitValue * mulValueList[selItem-1]
            elif selService == 5:                                 # Service 5 Area conversions
              mulValueList = [1.196, 100, 1/2.471]                
              conValue = unitValue * mulValueList[selItem-1]
            elif selService == 6:                                 # Service 6 Volume conversion
              divValueList = [1000,  28.317, 1/35.315]            
              conValue = unitValue / divValueList[selItem-1]
            elif selService == 7:                                 # Service 7 Time conversion
              mulValueList = [86400,  10080, 730]                 
              conValue = unitValue * mulValueList[selItem-1]

            print('The converted result is', round(conValue, 2))   # Q4-C