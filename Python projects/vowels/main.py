def count_vowels(text):
    # Convert the text to lowercase to make counting case-insensitive
    text = text.lower()
    
    # Initialize a dictionary to hold the counts of each vowel
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Count the vowels
    for char in text:
        if char in vowel_counts:
            vowel_counts[char] += 1

    # Calculate the total number of vowels
    total_vowels = sum(vowel_counts.values())
    
    # Print the results
    print(f"Total Number of vowels: {total_vowels}")
    for vowel, count in vowel_counts.items():
        print(f"{vowel} = \"{count}\"")

# Get user input
user_input = input("Enter a sentence: ")
count_vowels(user_input)
