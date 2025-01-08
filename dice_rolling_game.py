import random

dice_counter = 0


def ask_user():
    while True:
        choice = input('Roll the dice? (y/n): ').lower()
        if choice in ['y', 'n']:
            return choice == 'y'

        print('Invalid choice')


def ask_number_of_dice():
    while True:
        try:
            dice_to_roll = int(
                input('How many dice do you want to roll? (enter a number): '))
            return dice_to_roll
        except ValueError:
            print('Please enter a valid number')


while True:
    dice_roll = tuple(random.sample(range(1, 7), k=2))
    dice_counter += 1

    print(dice_roll)
    print('Dice counter:', dice_counter)

    # Ask to continue
    if not ask_user():
        break

    # Roll additional dice if requested
    dice_number = ask_number_of_dice()
    for _ in range(dice_number - 1):
        print(tuple(random.sample(range(1, 7), k=2)))
    dice_counter += dice_number - 1
