#The Guessing Game 
#Step-by-step to develop a program. 
#The guessing game program will do the following: 
#• The player only gets five turns. 
#• The program tells the player after each guess if the number is higher or lower. 
#• The program prints appropriate messages for when the player wins and loses. 
  
import random
def guessgame():
    n = random.randint(1,100)
    for i in reversed (range(5)):
        N = int(input('Enter your guess(1-100):'))
        if N < n:
            print('HIGHER.', i,'gueses left.')
        elif N > n: 
            print('LOWER.',i,'guesses left.')
        else:
            print('Yes. The correct number is', n)
            break
        if i == 0:
            print('You lose. The correct number is', n)
            break
    R = str(input('Do you want to restart the game?(y/n):'))  
    if R == 'y':
        guessgame()
    elif R  == 'n':
        print('Goodbye!')
        
        
guessgame()
