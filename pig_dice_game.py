import random
from typing import Tuple, List

MAX_SCORE = 100


def roll_dice() -> int:
    rolled_value = random.randint(1, 6)
    print(f"You rolled a {rolled_value}")
    return rolled_value


def get_player_choice() -> str:
    while True:
        choice = input("Roll again? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid choice\n")


def play_turn(scores: List[int], current_player: int) -> Tuple[List[int], bool]:
    initial_score = scores[current_player]
    current_score = initial_score

    while True:
        rolled_value = roll_dice()
        current_score = current_score + rolled_value if rolled_value != 1 else initial_score

        if current_score >= MAX_SCORE:
            scores[current_player] = current_score
            return scores, True

        if rolled_value == 1:
            break

        if get_player_choice() == 'n':
            break

    scores[current_player] = current_score
    display_turn_results(initial_score, current_score, scores)
    return scores, False


def display_turn_results(initial_score: int, final_score: int, scores: List[int]):
    points_scored = final_score - initial_score if final_score > initial_score else 0
    print(f"\nYou scored {points_scored} points this turn.")
    print(f"Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}\n")


def main():
    scores = [0, 0]
    current_player = 1

    while True:
        current_player = 1 if not current_player else 0
        print(f"Player {current_player + 1}'s turn")

        scores, game_won = play_turn(scores, current_player)

        if game_won:
            print(f"Player {current_player + 1} won!")
            print(f"Final scores: Player 1: {
                  scores[0]}, Player 2: {scores[1]}")
            break


if __name__ == '__main__':
    main()
