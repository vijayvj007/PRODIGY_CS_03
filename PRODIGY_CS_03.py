import re

def check_password_strength(password):
    strength = "Weak"
    score = 0
    suggestions = []

    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long")
        return strength, suggestions

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one numeric digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"

    return strength, suggestions

password = input("Input a password: ")
strength, suggestions = check_password_strength(password)
print(f"Password strength: {strength}")
if suggestions:
    print("\nSuggestions for improvement:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
