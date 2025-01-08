import random
import string


def generate_password():
    length = int(input("Enter password length: "))

    with_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    with_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    with_special_characters = input(
        "Include special characters? (y/n): ").lower() == 'y'

    if length < (with_uppercase + with_numbers + with_special_characters) + 1:
        raise ValueError(
            "Password length is too short for the specified criteria.")

    password = []

    char_pool = string.ascii_lowercase

    if with_uppercase:
        char_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if with_numbers:
        char_pool += string.digits
        password.append(random.choice(string.digits))
    if with_special_characters:
        char_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)

    return ''.join(password)


def main():
    try:
        password = generate_password()

        print(password)
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
