import re

def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return False
    
    # Contain uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    
    # Contain at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Contain at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def main():
    password = input("Enter a password to check its strength: ")
    
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak.")

if __name__ == "__main__":
    main()
