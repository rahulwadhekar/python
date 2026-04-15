passwords = ["abc123", "securePass1", "helloWorld", "pass9876", "short1", "StrongPass99"]

valid_passwords = []
invalid_passwords = []

for pwd in passwords:
    has_digit = any(char.isdigit() for char in pwd)

    if len(pwd) > 8 and has_digit:
        valid_passwords.append(pwd)
    else:
        invalid_passwords.append(pwd)

print("Valid Passwords:", valid_passwords)
print("Invalid Passwords:", invalid_passwords)