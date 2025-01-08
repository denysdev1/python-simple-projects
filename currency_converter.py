USD = 'USD'
EURO = 'EUR'
CAD = 'CAD'

EXCHANGE_RATES = {
    USD: {
        CAD: 1.43944,
        EURO: 0.961390,
    },
    EURO: {
        USD: 1.04016,
        CAD: 1.49723
    },
    CAD: {
        USD: 0.694717,
        EURO: 0.667948,
    },
}


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                raise ValueError()

            return amount
        except ValueError:
            print("Invalid amount")


def get_currency(message, choices):
    while True:
        choice = input(message).upper()

        if choice in choices:
            return choice

        print("Invalid value")


def convert_currency(amount, source, target):
    try:
        converted_currency = amount * EXCHANGE_RATES[source][target]
    except KeyError:
        converted_currency = amount
    finally:
        conversion_history.append(f"""{amount:.2f} {
                                  target} = {converted_currency:.2f} {source}""")

        print(f"""{amount:.2f} {source} is equal to {
            converted_currency:.2f} {target}""")
        print('=======================')

        currencies = [c for c in EXCHANGE_RATES[source] if c != target]

        for currency in currencies:
            converted = amount * EXCHANGE_RATES[source][currency]

            print(f"""{amount:.2f} {source} is equal to {
                  converted:.2f} {currency}""")


def show_conversions():
    print("\nConversion history:\n")

    for conversion in conversion_history:
        print(conversion)


conversion_history = []
currencies = (USD, EURO, CAD)
FORMATTED_CURRENCIES = '/'.join(list(currencies)).upper()


def main():
    while True:
        amount = get_amount()
        source_currency = get_currency(
            f"Source currency {FORMATTED_CURRENCIES}: ", currencies)
        target_currency = get_currency(
            f"Target currency {FORMATTED_CURRENCIES}: ", currencies)
        convert_currency(amount, source_currency, target_currency)

        should_continue = get_currency("Continue? (Y/N): ", ['Y', 'N']) == 'Y'

        if not should_continue:
            break

    show_conversions()


if __name__ == '__main__':
    main()
