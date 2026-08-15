import random

# Generate a random number between 1 and 100
computer = random.randint(1, 100)

# Initialize attempt counter
attempts = 0

# Continue the game until the user guesses correctly
while True:

    # Get and validate user input
    try:
        user = int(input("Enter a number between 1 and 100: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Increase attempt count for each valid guess
    attempts += 1

    print("User number:", user)
    print("Attempts:", attempts)

    # Check if the user's guess is correct
    if user == computer:
        print("It's correct!")
        print("You guessed it in", attempts, "attempts!")
        break

    # Give feedback if the guess is too high
    elif user > computer:
        print("Too high!")

    # Give feedback if the guess is too low
    else:
        print("Too low!")


# A Sample Output
# Enter a number between 1 and 100: 50
# User number: 50
# Attempts: 1
# Too low!

# Enter a number between 1 and 100: 75
# User number: 75
# Attempts: 2
# Too high!

# Enter a number between 1 and 100: 63
# User number: 63
# Attempts: 3
# It's correct!
# You guessed it in 3 attempts!
