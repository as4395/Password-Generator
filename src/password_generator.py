import secrets
import string
import math
import sys

# Prompt the user for password preferences
def customize_password():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    return length, use_uppercase, use_lowercase, use_digits, use_special

# Generate a secure password based on selected options
def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    character_pool = ''
    required_characters = []
    
    if use_uppercase:
        character_pool += uppercase_letters
        required_characters.append(secrets.choice(uppercase_letters))
    if use_lowercase:
        character_pool += lowercase_letters
        required_characters.append(secrets.choice(lowercase_letters))
    if use_digits:
        character_pool += digits
        required_characters.append(secrets.choice(digits))
    if use_special:
        character_pool += symbols
        required_characters.append(secrets.choice(symbols))
    
    if not character_pool:
        raise ValueError("At least one character type must be selected")

    password = [secrets.choice(character_pool) for _ in range(length - len(required_characters))]
    password.extend(required_characters)
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Estimate entropy based on password length and character set size
def calculate_entropy(password):
    pool_size = 0
    
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    entropy = len(password) * math.log2(pool_size)
    return entropy

# Classify strength based on entropy score
def assess_strength(entropy):
    if entropy < 36:
        return "Very weak", 10
    elif entropy < 60:
        return "Weak", 30
    elif entropy < 120:
        return "Strong", 70
    else:
        return "Very strong", 100

# Estimate time to crack password using brute force
def estimate_crack_time(password, attempts_per_second=10e9):
    possible_combinations = 0
    if any(c.islower() for c in password):
        possible_combinations += 26
    if any(c.isupper() for c in password):
        possible_combinations += 26
    if any(c.isdigit() for c in password):
        possible_combinations += 10
    if any(c in string.punctuation for c in password):
        possible_combinations += len(string.punctuation)
    
    password_length = len(password)
    total_combinations = possible_combinations ** password_length
    
    seconds_to_crack = total_combinations / attempts_per_second
    
    # Convert seconds to days, hours, minutes, and seconds
    days = int(seconds_to_crack // (24 * 3600))
    hours = int((seconds_to_crack % (24 * 3600)) // 3600)
    minutes = int((seconds_to_crack % 3600) // 60)
    seconds = int(seconds_to_crack % 60)
    
    time_estimate = ""
    if days > 0:
        time_estimate += f"{days} days, "
    if hours > 0:
        time_estimate += f"{hours} hours, "
    if minutes > 0:
        time_estimate += f"{minutes} minutes, "
    if seconds > 0:
        time_estimate += f"{seconds} seconds"
    if time_estimate.endswith(", "):
        time_estimate = time_estimate[:-2]  # Remove trailing comma and space
    
    return time_estimate if time_estimate else "less than a second"

def main():
    while True:
        length, use_uppercase, use_lowercase, use_digits, use_special = customize_password()
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        entropy = calculate_entropy(password)
        strength, score = assess_strength(entropy)
        crack_time = estimate_crack_time(password)
        
        print("\nGenerated password:", password)
        print("Entropy: {:.2f} bits".format(entropy))
        print("Strength: {} ({}/100)".format(strength, score))
        print("Estimated time to crack:", crack_time) # Using brute force only
        print()
        
        create_another = input("Do you want to create another password? (yes/no): ").lower()
        if create_another != 'yes':
            sys.exit(0)

if __name__ == "__main__":
    main()
