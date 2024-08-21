# Atomic Chess

## Overview

**Atomic Chess** is a variant of chess with unique rules involving explosions. The game is played on a standard chessboard with the same pieces as regular chess but with a twist: capturing a piece causes an explosion that affects nearby squares. The primary objective remains the same—capture the opponent's king—but with additional strategic elements due to the explosion mechanic.

## Project Structure

The project consists of a single Python file, which contains the implementation of the Atomic Chess game. The main class, `ChessVar`, is responsible for managing the game state, processing moves, and enforcing the game's rules.

## Features

- **Initialization**: Starts a new game with pieces in their standard chess positions.
- **Move Handling**: Allows players to make moves using algebraic notation (e.g., 'e2', 'e4').
- **Explosion Mechanic**: Capturing a piece causes an explosion affecting the surrounding squares, removing affected pieces except for pawns.
- **Game State**: Tracks the game state and determines if the game is unfinished or if a player has won.
- **Turn Management**: Alternates turns between white and black.
- **Game Ending**: Ends the game when a king is captured or exploded.

## Usage

### Initializing a Game

To start a new game of Atomic Chess, create an instance of the `ChessVar` class:

```python
from ChessVar import ChessVar

game = ChessVar()

### Making Moves

To make a move, use the make_move method with the starting and ending positions in algebraic notation:

result = game.make_move('e2', 'e4')

The method returns True if the move is successful and False if the move is invalid or if the game has already been decided.

### Checking the Game State

To get the current state of the game, use the get_game_state method:

state = game.get_game_state()
print(state)  # Output can be 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'

### Printing the Board

To print the current state of the board, use the print_board method:

game.print_board()

This method will output the board's current configuration to the console.

## Rules and Constraints

- Capturing Pieces: When a piece is captured, it and all pieces in the surrounding 8 squares (except pawns) are removed from the board due to an explosion.

- King Captures: Kings cannot capture pieces and capturing a king ends the game.

- No Castling, En Passant, or Pawn Promotion: These standard chess rules are not applicable in Atomic Chess.

- Pawn Moves: Pawns can move two squares forward on their first move only.

## Example
Here’s an example demonstrating how to use the ChessVar class:

game = ChessVar()

print(game.make_move('e2', 'e4'))  # Output: True
print(game.make_move('e7', 'e5'))  # Output: True
print(game.make_move('f1', 'c4'))  # Output: True

game.print_board()

print(game.get_game_state())  # Output: UNFINISHED

## Installation

To use the ChessVar class, ensure you have Python installed on your system. Simply place the ChessVar.py file in your working directory and import it as needed.
