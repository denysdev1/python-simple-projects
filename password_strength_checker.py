import re

strengths = ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']


def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password) != None:
        strength += 1
    if re.search('[A-Z]', password) != None:
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>\\/\[\]_+=~`-]', password) != None:
        strength += 1

    return strengths[strength]


def main():
    password = input("Enter a password: ")
    strength = check_strength(password)

    print(f'Password strength: {strength}')


if __name__ == '__main__':
    main()
