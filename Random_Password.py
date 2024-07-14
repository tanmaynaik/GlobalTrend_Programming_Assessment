""" Write a Python function that generates a random password. 
The password should contain a mix of uppercase letters, 
lowercase letters, digits, and special characters """

import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

print("Randomly generated password: ", generate_password(12))