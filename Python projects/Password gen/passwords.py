import random
import string

def generate_password(length):
    # ---Define the character pool---
    characters = string.ascii_letters + string.digits + string.punctuation
    # ---Generate a random password---
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    # ---Collect user input---
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the desired length for each password: "))

    # ---Generate and display passwords---
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(password_length)
        print(password)

if __name__ == "__main__":
    main()
