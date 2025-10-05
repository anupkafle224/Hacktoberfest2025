import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True,
                      include_numbers=True, include_symbols=True):
    """
    Generate a secure random password with customizable options.
    
    Args:
        length (int): Length of the password (default: 12)
        include_uppercase (bool): Include uppercase letters
        include_lowercase (bool): Include lowercase letters
        include_numbers (bool): Include numbers
        include_symbols (bool): Include special symbols
    
    Returns:
        str: Generated password
    """
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"


    if not characters:
        print("At least one character type must be selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("===Password Generator===")
    print("Generate a secure password with customization options\n")
    try:
        
        length = int(input("Enter password length (default 12): ") or 12)

        print("\nSelect character types to include:")
        uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        lowercase = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
        numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'    

        password = generate_password(length, uppercase, lowercase, numbers, symbols)
            
        if password:
            print(f"\nGenerated Password: {password}")
            print(f"Password Length: {len(password)}")
                
            # Password strength indicator
            strength_score = sum([uppercase, lowercase, numbers, symbols])
            strength_levels = ["Very Weak", "Weak", "Moderate", "Strong"]
            print(f"Password Strength: {strength_levels[min(strength_score-1, 3)]}")
        
    except ValueError:
        print("Please enter a valid number for password length.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()