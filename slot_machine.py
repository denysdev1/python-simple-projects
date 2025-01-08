import random


def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))

            if balance >= 1:
                return balance

            print("Balance must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def place_bet(balance):
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: $"))

            if bet_amount >= 1 and bet_amount <= balance:
                return bet_amount

            if 1 == balance:
                print("Invalid bet amount. You can bet only $1")
            else:
                print(f"""Invalid bet amount. You can bet between $1 and ${
                      balance}""")
        except ValueError:
            print("Please enter a valid number for the bet amount.")


def spin_reels(balance, bet_amount):
    symbols = ['🍋', '🍉', '🍒', '⭐', '🔔']
    reels = random.choices(symbols, k=3)
    unique_reels_number = len(set(reels))
    winnings = 0

    print(' | '.join(reels))

    if unique_reels_number == 2:
        winnings = bet_amount * 2

        print(f"You won ${winnings}")
    elif unique_reels_number == 1:
        winnings = bet_amount * 10

        print(f"You wno ${winnings}")
    else:
        print("You lost!")

    return balance + winnings - bet_amount


def play_slots(balance):
    while balance >= 1:
        print(f"\nCurrent balance: ${balance}")

        bet_amount = place_bet(balance)
        balance = spin_reels(balance, bet_amount)

        if not balance:
            break

        play_again = input(
            "Do you want to play again? (y/n): ").strip().lower() == 'y'

        if not play_again:
            break

    print("You are out of money! Game over.")


def main():
    balance = get_starting_balance()

    print(
        f"\nWelcome to the Slot Machine Game\nYou start with a balance of ${balance}.")
    play_slots(balance)


if __name__ == "__main__":
    main()
