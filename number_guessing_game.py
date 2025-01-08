import random


def prompt_user(message, is_number=True):
    while True:
        try:
            value = input(message)

            return int(value) if is_number else value
        except ValueError:
            print("Invalid value")


def guess_number():
    is_playing = True
    best_score = 0

    while is_playing:
        min_value = prompt_user(
            "Specify min value (default 1): ")
        max_value = prompt_user("Specify max value (default 100): ")
        max_guesses = prompt_user('Specify max number of guesses: ')
        number_to_guess = random.randint(min_value, max_value)
        attempts_total = 0
        is_playing = True

        while True:
            guess = prompt_user(f'Guess the number (between {
                min_value} and {max_value}): ')
            attempts_total += 1

            if max_guesses < attempts_total:
                print(f"""You have run out of attempts! The correct number was {
                      number_to_guess}""")

                return

            if guess < number_to_guess:
                print('Too low! Try again')
            elif guess > number_to_guess:
                print('Too high! Try again')

            if guess == number_to_guess:
                break

        print(f"""Congratulations! You guessed the number in {
            attempts_total} {'attempt' if attempts_total == 1 else 'attempts'}.""")

        best_score = min(best_score, attempts_total)

        if best_score != 0:
            print(f"Best score: {best_score}")
        else:
            best_score = attempts_total

        attempts_total = 0
        is_playing = True if prompt_user(
            'Want to continue playing? (y/n): ', False).lower() == 'y' else False


guess_number()
