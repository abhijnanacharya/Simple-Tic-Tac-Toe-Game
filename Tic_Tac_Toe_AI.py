import sys

# Tic-Tac-Toe board represented as a list of lists
board = [[' ' for _ in range(3)] for _ in range(3)]

# Counter to keep track of the number of nodes generated
search_node_count = 0

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if the board is full
def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Function to check if any player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    global search_node_count

    # Base case: check if the game is over
    if check_win(board, 'X'):
        return -1, 1
    if check_win(board, 'O'):
        return 1, 1
    if is_full(board):
        return 0, 1

    if is_maximizing:
        best_score = -float('inf')
        num_trees = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score, trees_generated = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    num_trees += trees_generated
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best_score, num_trees
    else:
        best_score = float('inf')
        num_trees = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score, trees_generated = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    num_trees += trees_generated
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best_score, num_trees

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    global search_node_count

    # Base case: check if the game is over
    if check_win(board, 'X'):
        return -1, 1
    if check_win(board, 'O'):
        return 1, 1
    if is_full(board):
        return 0, 1

    if is_maximizing:
        best_score = -float('inf')
        num_trees = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score, trees_generated = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    num_trees += trees_generated
                    best_score = max(score, best_score)
        return best_score, num_trees
    else:
        best_score = float('inf')
        num_trees = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score, trees_generated = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    num_trees += trees_generated
                    best_score = min(score, best_score)
        return best_score, num_trees

# Find the location Coordinate based on user Input row= (num-1)/ 3 and col= (num-1) mod 3
def num_to_coordinates(num):
    row = (num - 1) // 3
    col = (num - 1) % 3
    return row, col

# Find the best move for a player
def find_best_move(board, player, algo):
    best_score = -float('inf') if player == 'O' else float('inf')
    best_move = None
    num_trees = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if algo == 1:
                    score, trees_generated = minimax(board, 0, False if player == 'O' else True)
                else:
                    score, trees_generated = minimax_alpha_beta(board, 0, -float('inf'), float('inf'), False if player == 'O' else True)
                board[i][j] = ' '
                num_trees += trees_generated
                if (player == 'O' and score > best_score) or (player == 'X' and score < best_score):
                    best_score = score
                    best_move = (i, j)

    return best_move, num_trees

# Human vs Computer
def human_vs_computer(start, algo):
    starting_player = start

    if starting_player == 'O':
        best_move, num_trees = find_best_move(board, 'O', algo)
        if best_move:
            board[best_move[0]][best_move[1]] = 'O'
            print(f"Computer's move: {best_move[0] * 3 + best_move[1] + 1}")
            print(f"Number of nodes generated: {num_trees}")

    while True:
        print_board(board)
        if is_full(board):
            print("Tie!")
            break

        val = int(input("Enter your move (1-9): 0 to exit! "))
        if val==0:
            exit()
        if val < 1 or val > 9:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        player_row, player_col = num_to_coordinates(val)
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, 'X'):
            print_board(board)
            print("X Won!!")
            break

        best_move, num_trees = find_best_move(board, 'O', algo)
        if best_move:
            board[best_move[0]][best_move[1]] = 'O'
            print(f"Computer's move: {best_move[0] * 3 + best_move[1] + 1}")
            print(f"Number of nodes generated: {num_trees}")

            if check_win(board, 'O'):
                print_board(board)
                print("O Won!!")
                break
        else:
            print_board(board)
            print("TIE!")
            break

# Computer vs Computer Mode
def computer_vs_computer(start, algo):
    starting_player = start  # Because either X or O can start

    while True:
        print_board(board)
        if is_full(board):
            print("TIE!!")
            break

        best_move, num_trees = find_best_move(board, starting_player, algo)
        if best_move:
            board[best_move[0]][best_move[1]] = starting_player
            print(f"Player {starting_player}'s move: {best_move[0] * 3 + best_move[1] + 1}")
            print(f"Number of nodes explored {starting_player}: {num_trees}")

            if check_win(board, starting_player):
                print_board(board)
                print(f"Player {starting_player} WON!")
                break

        starting_player = 'X' if starting_player == 'O' else 'O'  # Alternate the starting player

# Main Method
if __name__ == "__main__":
    if len(sys.argv) == 4:
        algo = int(sys.argv[1])
        starting_player = sys.argv[2].strip().upper()
        mode = int(sys.argv[3])
        
        print("Solution: ")
        
        if algo==1:
            print("Algorithm: MiniMax")
        elif algo==2:
            print("Algorithm: MiniMax with alpha-beta pruning")
        
        if starting_player=='X':
            print("FIRST: X")
        elif starting_player=='O':
            print("FIRST: O")
        
        if mode==1:
            print("Mode: Human versus Computer ")
        elif mode==2:
            print("Mode: Computer versus Computer ")

        if algo not in (1, 2) or starting_player not in ('X', 'O') or mode not in (1, 2):
            print("Invalid input. Please check the arguments.")
            exit(1)

        if mode == 1:
            human_vs_computer(starting_player, algo)
        elif mode == 2:
            computer_vs_computer(starting_player, algo)
    else:
        print("Usage: python Tic_Tac_Toe.py ALGO FIRST MODE")
        print("ALGO: 1 for MiniMax, 2 for MiniMax with alpha-beta pruning")
        print("FIRST: X or O")
        print("MODE: 1 for human vs. computer, 2 for computer vs. computer")
        exit(1)
