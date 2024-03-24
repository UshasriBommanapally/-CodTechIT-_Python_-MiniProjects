import random
import string

def generate_password(length, complexity):
    pool = ""
    if complexity == 'low':
        pool = string.ascii_letters + string.digits
    elif complexity == 'medium':
        pool = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        pool = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None

    password = ''.join(random.choices(pool, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity level ('low', 'medium', or 'high'): ")

    password = generate_password(length, complexity)

    if password:
        print("Your generated password is:", password)
    else:
        print("Password generation failed. Please try again with valid inputs.")

if __name__ == "__main__":
    main()
