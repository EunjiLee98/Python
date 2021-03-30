print('Welcome to the \'Go to Work\' game.\n') # Game Title and welcome message
roles = ['Dad', 'Mom', 'I'] # list of roles to choose
myRole = ''
while myRole == '': # repeat until the user chooses a role
    myRole = input('Choose your character (1. Dad 2. Mom 3. I): ')
    if not myRole.isdecimal(): # wrong input
        print('Choose again')
        myRole = ''
    else:
        myRole = int(myRole)
        if myRole <1 or myRole > 3: # out of index
            print('Choose again')
            myRole = ''
print('Your character is', roles[myRole-1]+'.') # Role selection result
print("\nLet's go to work!\n") # Game start message

# 4 events
events = ['Event1 Take transportation', 'Event2 Buy a morning meal', 'Event3 Go to the office', 'Event4 Drop by the restroom']
# sub options for 4 events
sub options = [['1. Bus', '2. Car'],
              ['1. Buy', "2. Don't buy"],
              ['1. Stairs', '2. Elevator'],
              ['1. Yes', '2. No']]
score = 1 # Game score
for i in range(4): # play all 4 events one by one
    print(events[i]+', what is your choice?')

    choiceEvent = ''
    while choiceEvent == '': # repeat until the user chooses an option
        choiceEvent = input(str(suboptions[i])+'? ') 
        if not choiceEvent.isdecimal(): # wrong input
            print('Choose again')
            choiceEvent = ''
        else:
            choiceEvent = int(choiceEvent)
            if choiceEvent <1 or choiceEvent > 2: # out of range
                print('Choose again')
                choiceEvent = ''
    # apply different scores for different roles
    if myRole == 1:
        score += 2
    if myRole == 2:
        score += 3
    if myRole == 3:
        score += 1
    # event result
    print('\n', roles[myRole-1], ',', events[i], ', Choice', suboptions[i][choiceEvent-1], ', Your current score: ', score)
    # warning message if the accumulated score is under the expected score at each step
    if score < (i+1)*2:
        print('Hurry Up! You are out of time!')
    print('\n')

# After the game is over
if score < 9: # failure case
    print('T.T Failed')
else: # success case
    print('~~ Success ~~')

input() # hold the program until the user confirms the result
