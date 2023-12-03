password = input()
command = input().split()

while command[0] != "Complete":
    if command[0] == "Make":
        if command[1] == "Upper":
            index = int(command[2])
            character = password[index]
            password = password.replace(character, character.upper(), 1)
            print(password)
        elif command[1] == "Lower":
            index = int(command[2])
            character = password[index]
            password = password.replace(character, character.lower(), 1)
            print(password)

    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if 0 <= index < len(password):
            password = password[:index] + char + password[index:]
            print(password)

    elif command[0] == "Replace":
        char = command[1]
        old_char = char
        value = int(command[2])
        if char in password:
            char = ord(char)
            new_char = char + value
            new_char = chr(new_char)
            password = password.replace(old_char, new_char)
            print(password)

    elif command[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for char in password:
            if char.isalpha() or char.isdigit() or char == "_":
                continue
            else:
                print(f"Password must consist only of letters, digits and _!")

        test_upper = any(char.isupper() for char in password)
        if not test_upper:
            print("Password must consist at least one uppercase letter!")

        test_lower = any(char.islower() for char in password)
        if not test_lower:
            print("Password must consist at least one lowercase letter!")

        test_digit = any(char.isdigit() for char in password)
        if not test_digit:
            print("Password must consist at least one digit!")
    command = input().split()