
import random

# Generate a random integer between 1 and 100 (inclusive).
number = random.randint(1, 100)

# Keep asking the user until they guess the correct number.
while True:
    try:
        # Get the user's input and convert it to an integer.
        guess = int(input("Guess a number between 1 and 100: "))

        # Check whether the input is within the allowed range.
        if guess < 1 or guess > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        # Check whether the user's guess matches the secret number.
        if guess == number:
            print("Congratulations! You've guessed the correct number.")
            break

        # Tell the user if their guess is too low.
        elif guess < number:
            print("Too low! Try again.")

        # If the guess is not correct or too low, it must be too high.
        else:
            print("Too high! Try again.")

    except ValueError:
        # Handle non-integer input, such as 99.9 or abc.
        print("Invalid input! Please enter a whole number, such as 50.")
