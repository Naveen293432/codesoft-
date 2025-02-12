import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
        
        print("Select password complexity:")
        print("1: Letters only")
        print("2: Letters and numbers")
        print("3: Letters, numbers, and symbols")
        
        complexity = int(input("Enter complexity level (1-3): "))
        if complexity not in [1, 2, 3]:
            print("Invalid complexity level. Please choose between 1 and 3.")
            return
        
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
