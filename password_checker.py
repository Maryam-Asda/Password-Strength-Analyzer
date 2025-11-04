# Function to check the password strength and return score and feedback
def check_password_strength(password):
    score = 0
    feedback = []
    
    # 1. Check Length (Must be at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")
    
    # 2. Check for Uppercase Letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter (A, B, C...).")

    # 3. Check for Digits (Numbers)
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit (0-9).")

    # 4. Check for Special Characters
    special_characters = "!@#$%^&*()-_+=<>?" 
    if any(c in special_characters for c in password):
        score += 1
    else:
        feedback.append(f"Password must contain at least one special character (e.g., {special_characters}).")
    
    # Determine the strength level based on the score
    if score == 4:
        strength = "Very Strong! 🎉"
    elif score == 3:
        strength = "Strong 👍"
    elif score == 2:
        strength = "Medium 🟡"
    else:
        strength = "Very Weak 🔴"
        
    return strength, feedback, score

# --- Main Program Execution ---

# Get input from the user
user_password = input("Enter the password to check: ")

# Run the function
strength, feedback, score = check_password_strength(user_password)

# Print the final result and feedback
print("-" * 40)
print(f"** Password Strength Assessment:** {strength}")
print(f"** Score:** {score}/4")

if feedback:
    print("\n** To improve strength, you should add:**")
    for item in feedback:
        print(f"- {item}")
print("-" * 40)
