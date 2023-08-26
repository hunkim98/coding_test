# Grid Game Challenge

## Description

In this coding test, you are tasked with implementing a grid-based game that involves two players, Goorm and the Player. The game takes place on a square grid of a given size. Each player starts at a specific position and follows a set of movement instructions to navigate the grid. The goal is to reach as many unique positions as possible while avoiding revisiting any previously visited positions.

### Game Rules

1. The game is played on a square grid of a specified size (N x N).
2. The grid contains two players: Goorm and the Player.
3. Each player starts at a unique initial position on the grid.
4. The grid is filled with movement instructions. Each cell contains a movement instruction in the format "XDIR" where X is an integer representing the number of steps to move, and DIR is the direction of movement (L, R, U, D).
5. Players move according to the instructions in the cells they occupy.
6. If a player steps on a cell they have visited before, the game is over for that player.
7. Players cannot move outside the boundaries of the grid. When reaching a boundary, they wrap around to the opposite side.

### Your Task

You are required to implement the main logic for the game using JavaScript. The game follows these steps:

1. Read the input from standard input.
2. Initialize the game grid and player positions based on the input.
3. Process the movement instructions for both players.
4. Keep track of visited positions for both players.
5. Determine when a player's game is over due to revisiting a position.
6. Calculate and compare the final scores of Goorm and the Player.
7. Print the result indicating which player wins and their score.

### Input

- The first line contains an integer N, the size of the square grid (1 ≤ N ≤ 100).
- The second line contains two integers Y and X (1 ≤ Y, X ≤ N), representing the starting position of Goorm.
- The third line contains two integers Y and X (1 ≤ Y, X ≤ N), representing the starting position of the Player.
- The following N lines each contain N cells, where each cell has a movement instruction in the format "XDIR" (1 ≤ X ≤ 9, DIR ∈ {L, R, U, D}).

### Output

- Print a single line with the result of the game. If Goorm wins, output "goorm SCORE" where SCORE is the final score of Goorm. If the Player wins, output "player SCORE" where SCORE is the final score of the Player.

### Example

Input:

3
1 1
3 3
1L 2L 1D
2U 3R 1D
2R 2R 1U

Output:

goorm 4
