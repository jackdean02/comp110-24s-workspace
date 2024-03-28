"""EX02 - One Shot Battleship."""

__author__ = "730385160"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_counter: int = 1

guess_row = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    
guess_column = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        
while row_counter <= grid_size:
    column_counter: int = 1
    grid: str = ""
    if guess_row == row_counter:
        while column_counter <= grid_size:
            if guess_column == column_counter:
                if guess_column == secret_column and guess_row == secret_row:
                    grid += RED_BOX
                else:
                    grid += WHITE_BOX
            else:
                grid += BLUE_BOX
            column_counter += 1  
    else:
        while column_counter <= grid_size:
            grid += BLUE_BOX
            column_counter += 1
    print(grid)
    row_counter += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_column == secret_column and guess_row != secret_row:
    print("Close! Correct column, wrong row.")
elif guess_column != secret_column and guess_row == secret_row:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")