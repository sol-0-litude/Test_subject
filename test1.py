import secrets

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password must be at least 8 characters long")

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%&*()_+-=[]{}|;:,.<>?`~"
    all_chars = lowercase + uppercase + digits + special

    # Ensure at least one of each required type
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill remaining characters with random choices
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # Shuffle for randomness
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def check_password(password):
    if len(password) < 8:
        return "Weak password"

    if not any(char.isdigit() for char in password):
        return "Add at least one number"

    if not any(char.isupper() for char in password):
        return "Add at least one uppercase letter"

    if not any(char.islower() for char in password):
        return "Add at least one lowercase letter"

    if not any(char in '!@#$%&*()_+-=[]{}|;:,.<>?`~' for char in password):
        return "Add at least one special character"

    return "Strong password"


def main():
    print("=== Random Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                raise ValueError("Password must be at least 8 characters long")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    password = generate_password(length)
    print(f"\nGenerated password: {password}\nPassword strength: {check_password(password)}")