import random
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Game board

def print_board():
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def choose_player_symbol(player_num):
    symbol = ""
    while symbol != "X" and symbol != "O":
        symbol = input(f"Player {player_num}'s turn (Symbol: X or O): ").upper()
    return symbol

def choose_game_mode():
    while True:
        print("Choose game mode:")
        print("1. Player vs Player")
        print("2. Player vs AI")
        mode = input("Option: ")
        if mode == "1":
            return "PvP"
        elif mode == "2":
            return "PvAI"
        else:
            print("Invalid mode. Please try again.")

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def reset_board():
    for i in range(9):
        board[i] = " "

def make_move(symbol, position):
    if position < 1 or position > 9 or board[position - 1] != " ":
        return False
    board[position - 1] = symbol
    return True

def check_win(symbol):
    return (
        (board[0] == symbol and board[1] == symbol and board[2] == symbol) or
        (board[3] == symbol and board[4] == symbol and board[5] == symbol) or
        (board[6] == symbol and board[7] == symbol and board[8] == symbol) or
        (board[0] == symbol and board[3] == symbol and board[6] == symbol) or
        (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
        (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
        (board[0] == symbol and board[4] == symbol and board[8] == symbol) or
        (board[2] == symbol and board[4] == symbol and board[6] == symbol)
    )

def is_board_full():
    return " " not in board

def update_score(player, scores):
    scores[player] += 1

def display_score(scores):
    print("Score:")
    print(f"Player 1: {scores['Player 1']}")
    print(f"Player 2: {scores['Player 2']}")
    print(f"AI: {scores['AI']}")
    print("")

def player_vs_player(scores):
    player1_symbol = choose_player_symbol(1)
    player2_symbol = "O" if player1_symbol == "X" else "X"

    print("\nPlayer 1's turn (Symbol: {})".format(player1_symbol))
    print("Player 2's turn (Symbol: {})\n".format(player2_symbol))

    while True:
        print_board()

        # Player 1's turn
        while True:
            try:
                position = int(input("Player 1's move (1-9): "))
                if make_move(player1_symbol, position):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        if check_win(player1_symbol):
            print_board()
            print("Player 1 wins!")
            update_score("Player 1", scores)
            break

        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        print_board()

        # Player 2's turn
        while True:
            try:
                position = int(input("Player 2's move (1-9): "))
                if make_move(player2_symbol, position):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        if check_win(player2_symbol):
            print_board()
            print("Player 2 wins!")
            update_score("Player 2", scores)
            break

        if is_board_full():
            print_board()
            print("It's a tie!")
            break

def player_vs_ai(scores):
    player_symbol = choose_player_symbol(1)
    ai_symbol = "O" if player_symbol == "X" else "X"

    print("\nPlayer's turn (Symbol: {})".format(player_symbol))
    print("AI's turn (Symbol: {})\n".format(ai_symbol))

    while True:
        print_board()

        # Player's turn
        while True:
            try:
                position = int(input("Your move (1-9): "))
                if make_move(player_symbol, position):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        if check_win(player_symbol):
            print_board()
            print("Congratulations! You won!")
            update_score("Player", scores)
            break

        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        print_board()

        # AI's turn
        print("AI's turn...")
        time.sleep(1)

        position = get_ai_move(ai_symbol)

        if make_move(ai_symbol, position):
            print("AI chooses position:", position)
        else:
            print("AI made an invalid move.")

        if check_win(ai_symbol):
            print_board()
            print("AI wins!")
            update_score("AI", scores)
            break

        if is_board_full():
            print_board()
            print("It's a tie!")
            break

def get_ai_move(symbol):
    # Check for winning moves
    for i in range(1, 10):
        if make_move(symbol, i):
            if check_win(symbol):
                board[i - 1] = " "  # Undo the move
                return i
            board[i - 1] = " "  # Undo the move

    # Check for blocking opponent's winning moves
    opponent_symbol = "O" if symbol == "X" else "X"
    for i in range(1, 10):
        if make_move(opponent_symbol, i):
            if check_win(opponent_symbol):
                board[i - 1] = " "  # Undo the move
                return i
            board[i - 1] = " "  # Undo the move

    # If no immediate winning or blocking moves, make a random move
    available_positions = [i for i, val in enumerate(board) if val == " "]
    return random.choice(available_positions) + 1

print("Welcome to Tic Tac Toe!")

scores = {"Player 1": 0, "Player 2": 0, "Player": 0, "AI": 0}

while True:
    reset_board()  # Reset the board for a new game

    mode = choose_game_mode()
    if mode == "PvP":
        player_vs_player(scores)
    elif mode == "PvAI":
        player_vs_ai(scores)

    display_score(scores)

    if not play_again():
        print("More games on my github!")
        break
