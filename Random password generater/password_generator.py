import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    length = int(input("Enter the length of the password (or enter 0 to exit): "))
    
    if length == 0:
        print("Exiting...")
        break
    
    password = generate_password(length)
    print("Generated Password:", password)
    print()