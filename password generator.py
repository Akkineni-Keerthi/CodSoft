import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    length = int(input("Enter the desired length of the password: "))

    if length < 1:
        print("Password length should be at least 1.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")


password_generator()
