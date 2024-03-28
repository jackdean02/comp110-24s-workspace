"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730385160"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
location = int(input("Pick a secret boat location between 1 and 4: "))
if location < 1:
    print(f"Error! {location} too low!")
    exit()
if location > 4:
    print(f"Error! {location} too high!")
    exit()
pick = int(input("Guess a number between 1 and 4: "))
if pick < 1:
    print(f"Error! {pick} too low!")
    exit()
if pick > 4:
    print(f"Error! {pick} too high!")
    exit()
if location == pick:
    if location == 1:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if location == 2:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if location == 3:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if location == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")
else:
    if pick == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if pick == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if pick == 3:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if pick == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship.")
