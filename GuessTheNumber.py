import random

guess_count = 0
randint = 1#random.randint(1, 2)  # create the number we want to guess
while guess_count <= 3:
    guess = int(input("Guess: "))  # create the first guess from user
    if guess == randint:  # checks if guess is correct by comparing to the random number
        print("Correct!")
        break
    elif guess != randint:
        print("Wrong, try again!")
        guess_count += 1
    else:
        continue

if guess_count >= 3:
    print("you lost, try again !")

    