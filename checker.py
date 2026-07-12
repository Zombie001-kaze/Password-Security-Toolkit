from common_passwords import COMMON_PASSWORDS
import re
import math

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"\d", password):
        charset += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def check_password(password):
    score = 0
    suggestions = []

    # Check password rules
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 2
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 2
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 2
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        suggestions.append("Add a special character.")

    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("⚠ This is a commonly used password. Choose something unique.")
        score = max(0, score - 4)

    # Determine strength
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    entropy = calculate_entropy(password)

    return score, strength, suggestions, entropy
