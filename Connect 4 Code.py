def draw(grid):
    print("")
    print("1 2 3 4 5") # Print column headers
    print("| | | | |")
    print(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], "- row 1")
    print(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], "- row 2")
    print(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], "- row 3")
    print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], "- row 4\n")

def add_piece(grid, column, player):

    if player == 1:
        piece = "B"
    else:
        piece = "R"

    # Find the lowest row that can fit the piece. As the four rows
    # is at the bottom, we can count upwards.
    row = -1
    for i in range(len(board)):
        if grid[i][column-1] == "0":
            row = i

    # If row = -1 then a space could not be found,
    # so the turn should be skipped. Otherwise we can insert the piece.
    if row == -1:
        print("Column is full! Skipping turn")
    else:
        grid[row][column-1] = piece

    return grid

#- MAIN PROGRAM ----------------------------------------------

board = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]

won = False
player = 1

draw(board)

while not won == True:

    print("It is player " + str(player) + "'s go.")

    c_choice = int(input("Enter the column number. "))

    while not (c_choice > 0 and c_choice < 6):
        print("There has been an error")
        c_choice = int(input("Enter the column number: "))

    board = add_piece(board, c_choice, player)

    if player == 1:
        player = 2
    else:
        player = 1

    draw(board)

print("Player " + str(player) + " has won!")
input("Press enter to exit.")
