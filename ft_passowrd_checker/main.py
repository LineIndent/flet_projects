import re


class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.common_passwords = ["password", "1234", "admin", "qwerty"]
        self.complexity_regex = re.compile(
            r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])"
        )

    def length_check(self):
        length = len(self.password)
        if length < 8:
            return "Very Weak"
        elif length >= 8 and length < 12:
            return "Weak"
        elif length >= 12 and length < 16:
            return "Moderate"
        else:
            return "Strong"

    def character_check(self):
        characters = set(self.password)
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        digits = set("0123456789")
        special_characters = set("!@#$%^&*()_+-=[]{};:,.<>/?`~")

        score = 0
        if any(char in lower_case for char in characters):
            score += 1
        if any(char in upper_case for char in characters):
            score += 1
        if any(char in digits for char in characters):
            score += 1
        if any(char in special_characters for char in characters):
            score += 1

        if score == 1:
            return "Very Weak"
        elif score == 2:
            return "Weak"
        elif score == 3:
            return "Moderate"
        else:
            return "Strong"

    def repeat_check(self):
        for i in range(len(self.password) - 2):
            if self.password[i] == self.password[i + 1] == self.password[i + 2]:
                return "Very Weak"
        return "Moderate"

    def sequential_check(self):
        for i in range(len(self.password) - 2):
            if (
                self.password[i : i + 3].isdigit()
                or self.password[i : i + 3].islower()
                or self.password[i : i + 3].isupper()
            ):
                return "Very Weak"
        return "Moderate"


password = input("Enter your password: ")

password_strength_checker = PasswordStrengthChecker(password)
length_strength = password_strength_checker.length_check()
character_strength = password_strength_checker.character_check()
repeat_strength = password_strength_checker.repeat_check()

print("Password Strength:", length_strength, character_strength, repeat_strength)
