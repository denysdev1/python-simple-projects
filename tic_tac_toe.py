from termcolor import colored, cprint

ZERO = '0'
CROSS = 'X'
EMPTY_CELL = "   "
BOARD_SIZE = 4


def show_board(board):
    line = "---+" * (BOARD_SIZE - 1) + '---'

    for row in board:
        separator = colored('|', 'light_magenta')
        cprint(line, 'light_magenta')
        cprint(separator.join(row))

    cprint(line, 'light_magenta')


def is_filled(row):
    unique_row_values = set(row)

    return len(unique_row_values) == 1 and row[0] != EMPTY_CELL


def check_for_winner(board):
    row_length = len(board)
    left_diagonal = [None for _ in range(BOARD_SIZE)]
    right_diagonal = [None for _ in range(BOARD_SIZE)]

    for i in range(row_length):
        current_row = board[i]
        col_values = [board[k][i] for k in range(row_length)]
        left_diagonal[i] = current_row[i]
        right_diagonal[-(i + 1)] = current_row[-(i + 1)]

        for row in [current_row, col_values, left_diagonal, right_diagonal]:
            if is_filled(row):
                return row[0]


def get_position(pos):
    input_value = int(input(f"Enter {pos} (1-3): ")) - 1

    if input_value > BOARD_SIZE - 1 or input_value < 0:
        raise ValueError

    return input_value


def get_move(board):
    while True:
        try:
            row = get_position('row')
            col = get_position('col')

            if not board[row][col].strip():
                return (row, col)

            print("This spot is already taken")
        except ValueError:
            print("Invalid value")


def play_game():
    board_is_full = False
    board = [[EMPTY_CELL for _ in range(BOARD_SIZE)]
             for _ in range(BOARD_SIZE)]
    symbol = ZERO

    while not board_is_full:
        if all(all(cell.strip() for cell in row) for row in board):
            break

        print(f"Player {symbol}'s turn")

        row, col = get_move(board)
        board[row][col] = f" {symbol} "
        show_board(board)

        winner = check_for_winner(board)
        symbol = ZERO if symbol == CROSS else CROSS

        if winner:
            print(f"Player {winner.strip()} wins!")

            return

    print("Board is full!")


if __name__ == "__main__":
    play_game()
