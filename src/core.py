import secrets
import string
import math

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    character_pool = ''
    required_chars = []

    if use_uppercase:
        character_pool += uppercase_letters
        required_chars.append(secrets.choice(uppercase_letters))
    if use_lowercase:
        character_pool += lowercase_letters
        required_chars.append(secrets.choice(lowercase_letters))
    if use_digits:
        character_pool += digits
        required_chars.append(secrets.choice(digits))
    if use_special:
        character_pool += symbols
        required_chars.append(secrets.choice(symbols))

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    remaining_length = length - len(required_chars)
    if remaining_length < 0:
        raise ValueError("Password length too short for selected character types.")

    password = [secrets.choice(character_pool) for _ in range(remaining_length)]
    password.extend(required_chars)
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

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
    return len(password) * math.log2(pool_size)

def assess_strength(entropy):
    if entropy < 36:
        return "Very weak", 10
    elif entropy < 60:
        return "Weak", 30
    elif entropy < 120:
        return "Strong", 70
    else:
        return "Very strong", 100

def estimate_crack_time(password, attempts_per_second=10e9):
    pool_size = 0
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    total_combinations = pool_size ** len(password)
    seconds = total_combinations / attempts_per_second

    days = int(seconds // (24 * 3600))
    hours = int((seconds % (24 * 3600)) // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    parts = []
    if days > 0:
        parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minutes")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} seconds")

    return ", ".join(parts)
