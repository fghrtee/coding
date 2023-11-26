def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    for _ in range(9):
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    else:
        print_board(board)
        print("It's a draw!")

# Uncomment the line below to play Tic Tac Toe
# tic_tac_toe()
