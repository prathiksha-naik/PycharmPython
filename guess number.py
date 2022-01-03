#This is a guess the number game.
import random
print("Heloo.What is your name?")
name=input()
print('well,'+name+',I am thinking of a number between 1 and 20 ')
secretnumber=random.randint(1,20)
for guess in range(1,7):
    print('Take a guess.')
    guessnum=int(input("Enter the number"))
    if guessnum<secretnumber:
        print('your guess is too low.')
    elif guessnum>secretnumber:
        print('your guess is too high')
    else:
        break
if guessnum==secretnumber:
    print('Good job '+ name +' you guessed my number ')
else:
    print('Nope.The number I was thinking of was',secretnumber)
