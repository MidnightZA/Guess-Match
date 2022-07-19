### Guess and Match Game
### The objective of the game is to guess the positions of the matching pair

import random

def game_board(board):
    print('\nLETTER ROW 1 --- ' + board[0],'| '+board[1],'| '+board[2],'| '+board[3],'| '
          +board[4],'| '+board[5],'| '+board[6],'| '
          +board[7],'| '+board[8],'| '+board[9])
    print('--------------------------------------------------------')
    print('LETTER ROW 2 --- ' +board[10],'| '+board[11],'| '+board[12],'| '+board[13],'| '
          +board[14],'| '+board[15],'| '+board[16],'| '
          +board[17],'| '+board[18],'| '+board[19])


def Tries():
    
    tries = 0
    options = range(1,11)
    
    while tries not in options:
        try:
            tries = int(input('How many tries would you like? [1-10] '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if tries < 0:
                print('Tries cannot be NEGATIVE!!')
            elif tries == 0:
                print('Tries cannot be ZERO')
        if tries not in options:
            print(f'Sorry, Please enter a number between 1 and {options[-1]}')
        if tries in options:
            if tries == 1:
                print(f'You have {tries} try to win the game\n')
            else:
                print(f'You have {tries} tries to win the game\n')
            
    return tries

def Mixer(letters1,letters2):
    
    random.shuffle(letters1)
    random.shuffle(letters2)

def GuessLetter1():
    
    letter1_position = 0
    guess_options = range(1,len(letters1)+1)
    
    while letter1_position not in guess_options:
        try:
            letter1_position = int(input(f'What is your guess for the LETTER 1 POSITION?(1-{guess_options[-1]}) '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if letter1_position not in guess_options:
                print(f'Invalid Entry, Please enter a number between 1 and {guess_options[-1]}')
    return letter1_position-1

def GuessLetter2():
    
    letter2_position = 0
    guess_options = range(1,len(letters2)+1)
    
    while letter2_position not in guess_options:
        try:
            letter2_position = int(input(f'What is your guess for the LETTER 2 POSITION?(1-{guess_options[-1]}) '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if letter2_position not in guess_options:
                print(f'Invalid Entry, Please enter a number between 1 and {guess_options[-1]}')
    return letter2_position-1

def replay():
    board = ['~'] * 20
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



def cheat():
    print('\nThis is the answer to the game board:')
    print(letters1)
    print(letters2)


### GAME CODE BELOW




print("Welcome to Guess and Match\n")
print("There are 10 letters (A-J) in ROW 1 and ROW 2")
print("The ojective of the game is to match the LETTERS in ROW 1 to the LETTERS in ROW 2")

board = ['~']*20
letters1 = ['A','B','C','D','E','F','G','H','I','J']
letters2 = ['A','B','C','D','E','F','G','H','I','J']
game_on = True
#Mixer(letters1,letters2)
remainder = len(letters1)




while game_on == True:

    board = ['~'] * 20
    game_board(board)

    print("\nFirst you have to choose how many tries you will like to have")
    tries = Tries()
    Mixer(letters1, letters2)

    ### Uncomment this to show the answer
    cheat()

    while tries > 0 and remainder !=0:
    
        LetterGuess1 = GuessLetter1()
        LetterGuess2 = GuessLetter2()

        if letters1[LetterGuess1] == letters2[LetterGuess2]:
            if board[LetterGuess1] == letters1[LetterGuess1]:
                print(f'You have already matched LETTER {letters1[LetterGuess1]}')
            else:
                remainder = remainder - 1
                print(f'\nCORRECT, Matched letter {letters1[LetterGuess1]}\n')
                print(f'There are {remainder} combinations left to match\n')

                board[LetterGuess1] = letters1[LetterGuess1]
                board[LetterGuess2+10] = letters2[LetterGuess2]

                game_board(board)
            
        else:
            print('\nNo Match\n')
            game_board(board)
            tries = tries - 1
            if tries == 0:
                print('\nGAME OVER')
                print('You have ran out of tries\n')
            else:
                if tries == 1:
                    print(f'(You have {tries} try left)')
                else:
                    print(f'(You have {tries} tries left)')
                print('\nHINT:')
                print(f'\tROW 1 position {LetterGuess1+1} is {letters1[LetterGuess1]}')
                print(f'\tROW 2 position {LetterGuess2+1} is {letters2[LetterGuess2]}\n')

        if remainder == 0:
            print('\n\nCONGRATULATIONS')
            print('You have won\n')


    game_on = replay()

