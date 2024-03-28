"""EX03 - Functional Battleship."""

__author__ = "730385160"
import random
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
row_counter: int = 1


def input_guess(grid_size: int, position: str) -> int:
    """Returns their guess in a row or column."""
    assert position == "row" or position == "column"

    if position == "row":
        guess = int(input("Guess a row: "))
    elif position == "column":
        guess = int(input("Guess a column: "))
    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, result: bool) -> None:
    """Returns the grid marked by a hit or miss."""
    row_counter: int = 1
    while row_counter <= grid_size:
        column_counter: int = 1
        grid: str = ""
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    if result:
                        grid += RED_BOX
                    if not result:
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


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Returns True or False based on guesses and secret location."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Runs the entire game beginning with a prompt for inputs."""
    turn: int = 1
    won_game: bool = False

    while turn <= 5 and not won_game:
        print(f"=== Turn {turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct:
            won_game = True
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
        else:
            print("Miss!")
            turn += 1
    if turn > 5 and not won_game:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
        