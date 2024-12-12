import random

def hangman():
    # List of fruit names
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'mango', 'orange']
    
    # Randomly select a fruit from the list
    secret_word = random.choice(fruits)
    word_length = len(secret_word)
    
    # Number of chances: length of the word + 2
    chances = word_length + 2
    guessed_letters = []
    correct_guesses = ['_'] * word_length
    
    print("Welcome to Hangman!")
    print(f"The secret word has {word_length} letters.")
    
    while chances > 0 and '_' in correct_guesses:
        print("\nCurrent word: " + ' '.join(correct_guesses))
        print(f"You have {chances} chances left.")
        
        # Get the user's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    correct_guesses[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            chances -= 1
        
    # Final result
    if '_' not in correct_guesses:
        print(f"Congratulations! You've guessed the word: {secret_word}")
    else:
        print(f"Game over! The secret word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    hangman()
