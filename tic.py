
def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()
def check_winner(board, player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False

def is_board_full(board):
    return " " not in board

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0
    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "

                if score > best_score:
                    best_score = score

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score
def best_move(board):
    best_score = -1000
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move
def play_game():
    board = [" "] * 9
    print("TIC-TAC-TOE")
    print("You are X")
    print("Computer is O")

    while True:
        display_board(board)
        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid move. Try again.")
                continue
            index = position - 1
            if board[index] != " ":
                print("Invalid move. Try again.")
                continue
            board[index] = "X"
        except ValueError:
            print("Invalid move. Try again.")
            continue
        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            break
        if is_board_full(board):
            display_board(board)
            print("Draw!")
            break
        computer_position = best_move(board)
        board[computer_position] = "O"

        print("Computer chose position:", computer_position + 1)
        if check_winner(board, "O"):
            display_board(board)
            print("Computer wins!")
            break
        if is_board_full(board):
            display_board(board)
            print("Draw!")
            break
play_game()