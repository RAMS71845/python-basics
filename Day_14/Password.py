while True:
    password = input("Enter a password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_length = False

    if len(password) >= 8:
        has_length = True

    special = "!@#$%^&*_-"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special:
            has_special = True

    score = 0

    if has_length:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        verdict = "Strong"
    elif score >= 3:
        verdict = "Medium"
    else:
        verdict = "Weak"

    print(f"\nScore: {score}/5 --> {verdict}")

    if not has_length:
        print("Missing: Length should be at least 8")
    if not has_upper:
        print("Missing: Uppercase letter")
    if not has_lower:
        print("Missing: Lowercase letter")
    if not has_digit:
        print("Missing: Digit")
    if not has_special:
        print("Missing: Special character")

    choice = input("\nCheck another? (y/n): ")

    if choice.lower() != "y":
        print("Goodbye!")
        break