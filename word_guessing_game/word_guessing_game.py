import random
import re

MAX_ATTEMPTS = 6


def get_secret_word():
    try:
        with open('./word_guessing_game/words.txt', 'r') as file:
            contents = file.read().strip()

            if not contents:
                print("No words loaded.")

            words = contents.split('\n')

            return random.choice(words)
    except FileNotFoundError:
        print("words.txt does not exist.")

        return ''


def ask_letter(guessed_letters: str):
    while True:
        letter = input("Enter a letter: ").strip().lower()

        if not re.search('[a-z]', letter):
            print("Enter only letters from a to z.")
        elif len(letter) != 1:
            print("Enter only one letter")
        elif letter in guessed_letters:
            print("You already guessed that letter.")
        else:
            return letter


def guess_word():
    secret_word = get_secret_word()

    if not secret_word:
        return

    guessed_letters = ''
    attempts = MAX_ATTEMPTS

    while attempts:
        letter = ask_letter(guessed_letters)

        if letter in secret_word:
            guessed_letters += letter
            word_to_display = ''.join([
                letter if letter in guessed_letters else '_' for letter in secret_word])

            print("Good guess")
            print(word_to_display)

            attempts = MAX_ATTEMPTS
        else:
            print("Wrong guess")

            attempts -= 1

        if len(guessed_letters) == len(secret_word):
            print("\nCongratulations! You guessed the word")

            return

    print(f"\nGame over! The word was {secret_word}")


def main():
    guess_word()


if __name__ == "__main__":
    main()
