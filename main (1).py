import random
import string

#  generate a random password
def generate_password(length=12):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Ask  for the length of the password
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Generated Password: {password}")
