import random
import string

def generate_password(length=12):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+[]{}|;:,.<>?'

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (default is 12): ") or 12)
    
    if password_length < 1:
        print("Invalid password length. Setting it to default (12).")
        password_length = 12

    password = generate_password(password_length)
    print("Generated Password:", password)
