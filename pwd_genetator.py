import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()