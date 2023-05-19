# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

def print_board():
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')1
    print('---------')

def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    # Check if the board is full
    if ' ' not in board:
        return True
    return False

# Function to make a move
def make_move(player):
    while True:
        move = input(f"{player}'s turn (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            board[int(move) - 1] = player
            break
        else:
            print('Invalid move. Please try again.')

def play_game():
    player = 'X'
    while not is_game_over():
        print_board()
        make_move(player)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    print_board()
    if ' ' not in board:
        print("It's a tie!")
    else:
        print(f"{player} wins!")

play_game()
