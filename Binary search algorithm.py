low = 1
high = 1000

#### NOTE ####

# CHOOSE YOUR NUMBER AND DONT FORGET IT.
# THE PROGRAM WILL GUESS A NUMBER, IF ITS TOO HIGH YOU SIMPLY ENTER l, for lower
# IF ITS TOO LOW, ENTER h, for higher
# AND ITS ITS CORRECT, ENTER c

# THIS PROGRAM CAN GUESS ANY NUMBER YOU CHOOSE IN UNDER 10 GUESSES
# IT USES THE BINARY SEARCH ALGORITHM

print("To think of a number between {} and {}.".format(low, high))
input("hit enter to start")
print()

guesses = 1
while True:
    print("Guessing in the range of {} and {}.".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("The computers guess is {}. Should it guess h or l, or c if it was correct. ".format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("It took the computer {} guesses.".format(guesses))
        break

    guesses += 1
