# Project 4 - XO Board Game

## Description

This step focuses on applying the Python concepts learned so far by building a complete command-line XO Board Game.

The project combines multiple Python concepts into a playable two-player game.

The main goal of this project is to understand how different programming concepts can work together to create a complete interactive application.

I chose this project because I wanted to move beyond small isolated exercises and build a real project with user input, game logic, conditions, loops, functions, and data structures.

* * *

## Topics Covered

  * Functions
  * Function Parameters
  * Arguments
  * Return Values
  * Lists
  * List Indexing
  * `while` Loops
  * `for` Loops
  * `if` Statements
  * Input Validation
  * `break`
  * `continue`
  * `input()`
  * String Methods
  * `.upper()`
  * `all()`
  * `in` Operator
  * List Modification
  * Game Logic
  * Function Reuse
  * Function Composition

* * *

## Project

### XO Board Game

A command-line two-player XO Board Game where players take turns placing `X` and `O` symbols on a 3×3 board.

The game allows the first player to choose between `X` and `O`. The second player automatically receives the remaining symbol.

The board is displayed using the following layout:

    7 | 8 | 9
    -----------
    4 | 5 | 6
    -----------
    1 | 2 | 3

Features include:

  * Choose `X` or `O` for Player 1
  * Automatically assign the remaining symbol to Player 2
  * Display the game board
  * Take player input
  * Prevent players from choosing an occupied position
  * Validate player moves
  * Check all possible winning combinations
  * Detect the winner
  * Detect a draw when all positions are occupied
  * Reset the board after a draw
  * Start a new game after a draw

The project is structured using multiple functions, where each function is responsible for one specific task.

The `play_game()` function acts as the main coordinator and controls the overall game flow.

* * *

## Why I Chose This Project

I chose this project because I wanted to practice combining different Python concepts into one complete application.

Instead of writing all the game logic inside one large block of code, I divided the program into several smaller functions.

For example:

  * `display_board()` is responsible for displaying the game board.
  * `reset_board()` is responsible for clearing the board.
  * `get_player_move()` is responsible for getting a valid player move.
  * `check_winner()` is responsible for checking all possible winning combinations.
  * `play_game()` coordinates the game flow and controls the players' turns.

This project helped me understand the importance of:

  * Reusable code
  * Single responsibility
  * Function composition
  * Input validation
  * Loops and control flow
  * Lists and indexing
  * Breaking a larger problem into smaller logical components
  * Building a complete interactive program

This project was also an important step in my Python learning journey because it was one of my first projects where multiple functions worked together to create a complete playable application.

* * *

## Author

Erfan Nemati

* * *

## Example

### Input

    Choose X or O: X

    Choose a position from 1 to 9: 7
    
    Choose a position from 1 to 9: 5
    
    Choose a position from 1 to 9: 8
    
    Choose a position from 1 to 9: 1
    
    Choose a position from 1 to 9: 9
    
### Output

    =============
    Enjoy XO Game
    =============

     X | X | X
    -----------
       | O |
    -----------
     O |   |

    Game is Over and Player 1 is the Winner!

* * *
