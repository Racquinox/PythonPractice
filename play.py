import random

num = random.randint(1, 10)

print("Guess a number from 1 to 10")
guess = int(input())


while guess != num:

    if guess > num:
        print("Too high, try again")
        guess = int(input())

    elif guess < num:
        print("Too low, try again")
        guess = int(input())

else:
    print("You got it!")
