import random


def generate_number():
    unique_numbers = random.sample(range(10), k=4)

    if unique_numbers[0] == 0:
        unique_numbers[0], unique_numbers[1] = unique_numbers[1], unique_numbers[0]

    return int(''.join(map(str, unique_numbers)))


def get_number_length(number):
    return len(str(number))


def are_digits_unique(number: int):
    digits = str(number)

    return len(digits) == len(set(digits))


def get_cows_and_bulls(guess: str, secret: str):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls

    return cows, bulls


def guess_number(number_to_guess: int):
    number_length = get_number_length(number_to_guess)

    while True:
        errored = False

        try:
            guess = int(input("Guess: "))
        except ValueError:
            errored = True

        if errored or not are_digits_unique(guess):
            print(f"""Invalid guess. Please enter a {
                  number_length}-digit number with unique digits.""")
            continue

        cows, bulls = get_cows_and_bulls(
            str(guess), str(number_to_guess))

        if bulls == 4:
            break

        print(f'{cows} cows, {bulls} bulls')

    print("Congratulations! You guessed the correct number!")


def main():
    number_to_guess = generate_number()
    number_length = get_number_length(number_to_guess)

    print(f"""I have generated a {
          number_length}-digit number with unique digits. Try to guess it!""")

    guess_number(number_to_guess)


if __name__ == '__main__':
    main()
