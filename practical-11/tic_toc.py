# Block 1: Function to print the board
def print_board(board):
    # Function to print the current state of the board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Block 2: Function to check if a player has won
def check_winner(board, player):
    # Function to check if the current player has won
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Block 3: Function to check if the game is a draw
def check_draw(board):
    # Function to check if the game is a draw (no empty spaces left)
    return ' ' not in board

# Block 4: Main function to play the game
def play_game():
    # Initial board setup with 9 empty spaces
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    # Block 5: Game loop
    while True:
        # Get input from the current player
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if board[move] != ' ':
                print("That position is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        # Place the player's mark on the board
        board[move] = current_player
        print_board(board)

        # Block 6: Check if the current player has won
        if check_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Block 7: Check if the game is a draw
        if check_draw(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Block 8: Entry point of the program
if __name__ == "__main__":
    play_game()

