print('Welcome to the \'Go shopping\' game.')
characterList = ['Rich person', 'Ordinary person', 'Beggar']
print('The characters that you can enjoy are ',characterList, '\n')    

selCharacter = input('Choose your character (1. Rich person 2. Ordinary person 3. Beggar) : ')  
while  not selCharacter.isdecimal() or (int(selCharacter) > 3 or int(selCharacter) < 1):
               print('Choose again')
               selCharacter = input('Choose your character (1. Rich person 2. Ordinary person 3. Beggar) : ') 

selCharacter = int(selCharacter)
if selCharacter == 1 :
               print('Your character is Rich person\n')
elif selCharacter == 2 :
               print('Your character is Ordinary person\n')
else :
               print('Your character is Beggar\n')

print('Let\'s go shopping!!\n')
eventList = ['Event1 Buy T-shirt', 'Event2 Buy Jeans', 'Event3 Buy Shoes', 'Event4 Payment Method']
optionList = [['1. 100,000won', '2. 50,000won'], ['1. 80,000won', '2. 40,000won'], ['1. 120,000won', '2. 60,000won'], ['1. Card', '2. Cash']]
score = 0

for i in range (len(eventList)) :
               print('[',eventList[i],']', 'What is your choice?\n')
               selOption = input(optionList[i])

               while  not selOption.isdecimal() or (int(selOption) > 2 or int(selOption) < 1):
                              print('Choose again')
                              selOption = input(optionList[i])


               selOption = int(selOption)
               if selCharacter == 1 :
                              if selOption == 1 :
                                             score += 5
                              elif selOption == 2 :
                                             score += 2
               elif selCharacter == 2 :
                              if selOption == 1 :
                                             score += 3
                              elif selOption == 2 :
                                             score += 1
               else :
                              if selOption == 1 :
                                             score += 1
                              elif selOption == 2 :
                                             score += 5

               print(characterList[selCharacter-1],"/", eventList[i], "/", 'Choice', optionList[i][selOption-1],"/", 'Your score is ', score, '\n')

if selCharacter == 1 :
               if score < 14 :
                              print('You failed T_T..')
               else :
                              print('You succeeded >_<!!')
elif selCharacter == 2 :
               if score < 8 :
                              print('You failed T_T..')
               else :
                              print('You succeeded >_<!!')

else :
               if score < 12 :
                              print('You failed T_T..')
               else :
                              print('You succeeded >_<!!')
