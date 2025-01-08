import random

MAX_NUMBER_OF_ROUNDS = 3
ROCK = 'r'
PAPER = 'p'
SCISSORS = 'sr'


def prompt_for_choice(message, choices):
    while True:
        input_result = input(message)

        if input_result in choices:
            return input_result

        print('Invalid value')


def print_statistics():
    print("\nStatistics: ")
    print("\nFirst player:")

    for key in score['player']:
        print(f"{key.capitalize()}: {score['player'][key]}")

    print("\nSecond player:")

    for key in score['computer']:
        print(f"{key.capitalize()}: {score['computer'][key]}")


def get_initial_score():
    return {
        key: {
            'wins': 0,
            'ties': 0,
            'losses': 0
        } for key in ['player', 'computer']
    }


def determine_round_winner(choice_1, choice_2):
    print(f'First player chose {choices.get(choice_1)}')
    print(f'Second player chose {choices.get(choice_2)}')

    if choice_1 == choice_2:
        print('Tie')
        score['player']['ties'] += 1
    elif losing_map.get(choice_1) == choice_2:
        print("Second player wins.")
        score['computer']['wins'] += 1
        score['player']['losses'] += 1
        # print('You lose')
    else:
        print("First player wins.")
        score['player']['wins'] += 1


def check_for_game_winner():
    if score['player']['wins'] == 2:
        print('First player is the winner!')
    elif score['computer']['wins'] == 2:
        print('Second player is the winner!')


choices = {ROCK: '🪨', PAPER: '🧻', SCISSORS: '✂️'}
losing_map = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}
possible_choices = tuple(choices.keys())
round = 0
score = get_initial_score()

while round <= MAX_NUMBER_OF_ROUNDS:
    round += 1
    # computer_choice = random.choice(possible_choices)
    first_player_choice = prompt_for_choice('(Player 1) Rock, paper, or scissors? (r/p/s)',
                                            possible_choices)
    second_player_choice = prompt_for_choice('(Player 2) Rock, paper, or scissors? (r/p/s)',
                                             possible_choices)

    # print(f'You chose {choices.get(choice)}')
    # print(f'Computer chose {choices.get(computer_choice)}')

    determine_round_winner(first_player_choice, second_player_choice)
    check_for_game_winner()

    wins = [score[key]['wins'] for key in score.keys()]
    game_ended = round == 3 or 2 in wins

    if game_ended:
        should_continue_key = 'n'

        while True:
            should_continue_key = input('Continue (y/n)').lower()

            if should_continue_key in ['y', 'n']:
                break

            print('Invalid value')

        if should_continue_key != 'y':
            print_statistics()
            break

        round = 0
        score = get_initial_score()
