import random


def computerPlays():
    comp = random.choice(['rock','paper','scissors'])
    if(comp == 'rock'):
        comp = 'r'
    elif(comp == 'paper'):
        comp = 'p'
    else:
        comp = 's'
    return comp







print('Welcome to the game here are the rules:\n => Enter P for Paper\n => R for Rock\n and \n => S for scissors')
userInput = input()
if(userInput == 'p'):
    print('You entered P')
    randomGotten = computerPlays()
    print(randomGotten)
    if(userInput != randomGotten):
        if(randomGotten == 'r'):
            print('Paper wins: You win...')
        else:
            print('Scissor wins: I win, Looser!!!')
    else:
        print('Null, No one wins')
elif(userInput == 'r'):
    print('You entered R')
    randomGotten = computerPlays()
    print(randomGotten)
    if(userInput != randomGotten):
        if(randomGotten == 'p'):
            print('Paper wins: I win, Losser!!!')
        else:
            print('Rock wins: You win...')
    else:
        print('Null, No one wins')

elif(userInput == 's'):
    print('You entered S')
    randomGotten = computerPlays()
    print(randomGotten)
    if(userInput != randomGotten):
        if(randomGotten == 'r'):
            print('Rock wins: i win Looser!!!')
        else:
            print('Scissors wins: You win...')
    else:
        print('Null, No one wins')
else:
    print('Please select a valid option to play the game')





