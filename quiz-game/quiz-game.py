import random
from termcolor import cprint
import csv
import os


class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = list(map(lambda option: (
            chr(97 + option[0]), option[1]), enumerate(options)))
        self.answer = answer

    def display(self, number):
        print(f"Question {number}: {self.text}")

        for option in self.options:
            print(f"{option[0].upper()}) {option[1]}")

    def is_correct(self, choice):
        correct_answer, selected_option = next(
            ((letter, opt) for letter, opt in self.options if letter == choice), None)

        return selected_option == self.answer, correct_answer


QUESTIONS = [
    Question(
        text='What is the capital of France?',
        options=['Paris', 'London', 'Rome', 'Madrid'],
        answer='Paris',
    ),
    Question(
        text='Who wrote the play Romeo and Juliet?',
        options=['William Shakespeare', 'Charles Dickens',
                 'Jane Austen', 'Mark Twain'],
        answer='William Shakespeare',
    ),
    Question(
        text='What is the largest planet in our solar system?',
        options=['Earth', 'Jupiter', 'Saturn', 'Mars'],
        answer='Jupiter',
    ),
    Question(
        text='Which superhero is known as the "Dark Knight"?',
        options=['Superman', 'Batman', 'Spider-Man', 'Iron Man'],
        answer='Batman',
    ),
    Question(
        text='What is the name of the wizarding school in Harry Potter?',
        options=['Beauxbatons', 'Durmstrang', 'Hogwarts', 'Ilvermorny'],
        answer='Hogwarts',
    ),
]


def answer_question(question):
    while True:
        answer = input("Your answer: ").lower().strip()
        options = [letter for letter, _ in question.options]

        if answer not in options:
            print('Invalid value')
        else:
            return answer


def import_questions():
    file_name = input('Enter a filename with quiz questions: ').strip()

    if not file_name:
        return

    with open(os.getcwd() + '/quiz-game/' + file_name, 'r', encoding='UTF-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for question, options, answer in csv_reader:
            QUESTIONS.append(Question(question, options.split(','), answer))


def play_game():
    import_questions()
    random.shuffle(QUESTIONS)

    score = 0

    for number, question in enumerate(QUESTIONS, start=1):
        question.display(number)
        answer = answer_question(question)
        is_correct, correct_answer = question.is_correct(answer)

        if is_correct:
            cprint('Correct!\n', 'green')
            score += 1
        else:
            cprint(f"""Wrong! The correct answer is {
                   correct_answer.upper()}\n""", "red")

    print(f"Your final score: {score}/{len(QUESTIONS)}")


def main():
    play_game()


if __name__ == '__main__':
    main()
