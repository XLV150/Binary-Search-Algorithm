low = 1
high = 1000

#### NOTE ####

# CHOOSE YOUR NUMBER AND ENTER IT.
# THE PROGRAM WILL GUESS A NUMBER, UNTIL IT GUESSES CORRECTLY

# THIS PROGRAM CAN GUESS ANY NUMBER YOU CHOOSE IN UNDER 10 GUESSES
# IT USES THE BINARY SEARCH ALGORITHM

print("To think of a number between {} and {}.".format(low, high))
numberchoice = int(input("Enter the number you choose: "))

guesses = 1
while True:
    guess = low + (high - low) // 2

    if guess == numberchoice:
        print("The number you entered was {}, it took me {} guesses to get it right.".format(numberchoice, guesses))
        break
    elif guess < numberchoice:
        print("Guessed {}, Guessing lower.".format(guess))
        guesses += 1
        low = guess + 1
    elif guess > numberchoice:
        print("Guessed {}, Guessing higher.".format(guess))
        guesses += 1
        high = guess - 1



