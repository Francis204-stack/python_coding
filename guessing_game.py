import random

print("-----Number Guessing Game-----")
secret_number = random.randint(1, 50)

while True:
    guess = int(input("Guess a number between 1 and 50: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct! You guessed the number!")
        break
