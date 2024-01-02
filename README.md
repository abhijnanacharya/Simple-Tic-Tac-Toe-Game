# Tic-Tac-Toe Game

This Python script implements a Tic-Tac-Toe game with two modes: Human versus Computer and Computer versus Computer. The game features two different algorithms for the computer player: MiniMax and MiniMax with alpha-beta pruning.

## Usage

To run the game, use the following command:

```
python Tic_Tac_Toe_AI.py ALGO FIRST MODE
```
 - ALGO: 1 for MiniMax, 2 for MiniMax with alpha-beta pruning
 - FIRST: X or O
 - MODE: 1 for human vs. computer, 2 for computer vs. computer

## Algorithm
- For MiniMax (ALGO=1), the script uses the classic MiniMax algorithm to find the best move for the computer player.
- For MiniMax with alpha-beta pruning (ALGO=2), the script employs the MiniMax algorithm with alpha-beta pruning to optimize the search and reduce the number of explored nodes.

## Game Modes
1. Human versus Computer (MODE=1):

  - The human player is represented by 'X'.
  - The computer player is represented by 'O'.
  - The human player makes a move by entering a number from 1 to 9, corresponding to the position on the Tic-Tac-Toe board.
  - The computer player uses the selected algorithm to determine its moves.
2. Computer versus Computer (MODE=2):

  - The starting player ('X' or 'O') alternates between moves.
  - Both players are controlled by the computer, using the chosen algorithm for decision-making.
Example Usage
```
python Tic_Tac_Toe_AI.py 2 X 1
```
- Algorithm: MiniMax with alpha-beta pruning
- First move: X
- Mode: Human versus Computer

Acknowledgments
This implementation is based on the solution by Acharya, Abhijnan.

Note: The code and instructions are provided as-is and may be subject to modification or improvement.
