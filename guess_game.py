import random
number=random.randint(1,100)
while True:
    guess=int(input("enter a number between 1 to 100"))
    if guess<number:
        print("too low, try again")
    elif guess>number:
        print("too high, try again")
    else:
        print("congratulations,you guessed it right")
        break

