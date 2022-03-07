import random

name = input("Hello, what is your name: ")

print("Well, " + name + ", I am thinking of a number between 1 and 10, take a guess.")
secretNumber = random.randint(1, 10)


#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    guess = int(input("Take a guess: "))

    if guess > secretNumber:
        print("Is too high")
    elif guess < secretNumber:
        print("Is too low.")
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print("Good job " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number i was thinking of was " + str(secretNumber))