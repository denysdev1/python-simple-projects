class ATM:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


class ATMDisplay:
    def show_welcome(self):
        print("Welcome to the ATM!")

    def show_balance(self, balance):
        print(f'Your current balance is: ${balance}')

    def show_deposit_success(self, amount):
        print(f"Successfully deposited ${amount}.")

    def show_withdrawal_success(self, amount):
        print(f"Successfully withdrew ${amount}.")

    def show_error(self, message):
        print(message)

    def show_menu_options(self, actions):
        print()
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")

    def prompt_for_amount(self, action_type):
        return input(f"Enter the amount to {action_type}: ")

    def prompt_for_option(self):
        return input("Please, choose an option: ")


class ATMInterface:
    ACTIONS = ['Check Balance', 'Deposit', 'Withdraw', 'Exit']

    def __init__(self, atm: ATM, display: ATMDisplay):
        self.atm = atm
        self.display = display

    def get_amount_input(self, action_type: str):
        while True:
            try:
                amount = float(self.display.prompt_for_amount(action_type))
                if amount < 1:
                    self.display.show_error(
                        f"{action_type.capitalize()} amount must be positive.")
                    continue
                return amount
            except ValueError:
                self.display.show_error("Please enter a valid number.")

    def handle_balance(self):
        balance = self.atm.get_balance()
        self.display.show_balance(balance)

    def handle_deposit(self):
        amount = self.get_amount_input("deposit")
        try:
            self.atm.deposit(amount)
            self.display.show_deposit_success(amount)
        except ValueError as e:
            self.display.show_error(str(e))

    def handle_withdrawal(self):
        amount = self.get_amount_input("withdraw")
        try:
            self.atm.withdraw(amount)
            self.display.show_withdrawal_success(amount)
        except ValueError as e:
            self.display.show_error(str(e))

    def show_menu(self):
        self.display.show_welcome()
        while True:
            self.display.show_menu_options(self.ACTIONS)
            option = self.get_menu_option()

            if option == 1:
                self.handle_balance()
            elif option == 2:
                self.handle_deposit()
            elif option == 3:
                self.handle_withdrawal()
            elif option == 4:
                break

    def get_menu_option(self):
        while True:
            try:
                option = int(self.display.prompt_for_option())
                if 1 <= option <= len(self.ACTIONS):
                    return option
                self.display.show_error("Invalid option.")
            except ValueError:
                self.display.show_error("Invalid option.")


def main():
    atm = ATM()
    display = ATMDisplay()
    interface = ATMInterface(atm, display)
    interface.show_menu()


if __name__ == '__main__':
    main()
