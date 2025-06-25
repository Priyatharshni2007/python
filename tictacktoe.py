def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Other diagonal
        return True
    return False


def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column 1-3): ")
        try:
            row = int(input("Row: ")) - 1
            col = int(input("Col: ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid position! Choose from 1 to 3.")
                continue
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue

            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw! 🤝")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a number (1-3).")


# Start the game
tic_tac_toe()
