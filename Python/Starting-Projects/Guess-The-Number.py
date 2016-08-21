import random

Tries = 1
secret_number = random.randint(1,100)
guess = int(input("Take a guess: "))
print secret_number

while secret_number != guess and Tries < 6:

    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    guess = int(input("Take a guess: "))
    Tries += 1

if Tries == 6:
    print("\nSorry you reached the maximum number of tries")
    print("The secret number was ",secret_number)

else:
    print ("\nYou guessed it! The number was " ,secret_number)
    print("You guessed it in ", Tries,"attempts")


#The simple One

"""import random

a = random.randint(0,11)
b = int(raw_input("> "))
turn = 0

print a

while a != b and turn < 6:
    print ("Sorry, Try again.")
    turn += 1
    b = int(raw_input("> "))

if turn == 6:
    print ("Sorry, you lose the game")

else:
    print ("You won the game!!!!")
"""
