import random
# ---Getting user input---
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("That's not a valid number. Please try again.")
# ---Game mechanics---
def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
