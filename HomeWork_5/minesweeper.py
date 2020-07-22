"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 5
Program:minesweeper.py
"""


def create_game_board(size, mines):  # creates the game board array
    from random import sample
    board = [[0 for i in range(size)] for i in range(size)]
    rand_list = sample(list(range(size * size)),
                       mines if mines < size else size)  # random list of indexes where mines will be
    for i in rand_list:
        row = i // size
        col = i % size
        board[row][col] = "x"
        updateValues(row, col, board)  # updating mines surroundings values
    return board


def Create_PlayBoard(size):  # creates the game board array
    playboard = [[" " for i in range(size)] for i in range(size)]
    return playboard


def Game_dict(realboard):  # Makes a dict with the row, column as keys and True for zero False for else as values
    size = len(realboard)
    Game_dict = {(row, col): True if realboard[row][col] == 0 else False for row in range(size) for col in range(size)}
    return Game_dict


def updateValues(mine_row, col, gameboard):  # updating mines surroundings values
    size = len(gameboard)
    # row above
    if mine_row - 1 > -1:
        row = gameboard[mine_row - 1]
        if row[col] != 'x':
            row[col] += 1
        if col - 1 > -1:
            if row[col - 1] != 'x':
                row[col - 1] += 1
        if size > col + 1:
            if row[col + 1] != 'x':
                row[col + 1] += 1
    row = gameboard[mine_row]
    if col - 1 > -1:
        if row[col - 1] != 'x':
            row[col - 1] += 1
    if size > col + 1:
        if row[col + 1] != 'x':
            row[col + 1] += 1
    if size > mine_row + 1:
        row = gameboard[mine_row + 1]
        if row[col] != 'x':
            row[col] += 1
        # left
        if col - 1 > -1:
            if row[col - 1] != 'x':
                row[col - 1] += 1
        # right
        if size > col + 1:
            if row[col + 1] != 'x':
                row[col + 1] += 1


def cell_value(row, col, value):  # returns cell value
    return value[row][col]


def play(realboard, playboard, Game_dict):
    print_board(playboard)
    row, col = user_cell(len(realboard))
    value = cell_value(row, col, realboard)
    if value == 'x':  # losing scenario
        print_board(realboard)
        print()
        print('GAME OVER !')
        play_again()

    else:
        playboard[row][col] = value
        if value == 0:
            open_cells(row, col, realboard, playboard, Game_dict)
    blank_count = sum([playboard[row].count(" ") for row in range(len(playboard))])
    x_count = sum([realboard[row].count("x") for row in range(len(realboard))])
    if blank_count == x_count:  # winning scenario
        print_board(playboard)
        print('BOARD CLEARED , YOU WON !')
        play_again()

    play(realboard, playboard, Game_dict)  # if the game is still on


def print_board(board):  # board print function
    board_size = len(board)
    print("  +" + "---+" * board_size)
    for row in range(1, board_size + 1):
        border = str(row) + " |"
        cell = "".join([" {} |"] * len(board)).format(*board[row - 1])
        print(border + cell)
        print("  +" + "---+" * board_size)
    print(" ".join(["  "] + [" {} "] * len(board)).format(*list(range(1, board_size + 1))))


def user_cell(size):  # returns the cell picked by the user
    row = int(input("select a row:")) - 1
    col = int(input("select a column:")) - 1
    while 0 <= row < size and 0 <= col < size:
        break
    else:
        print("the value you entered is out of range!, try again!")
        row = int(input("select a row:")) - 1
        col = int(input("select a column:")) - 1
    return row, col


def open_cells(row, col, realboard, playboard, game_dict):  # open all the cells around zero recursively
    main_val = (col, realboard, playboard, game_dict)
    if game_dict[(row, col)] is False:
        return
    left_cell(row, *main_val)
    right_cell(row, *main_val)
    if row - 1 > -1:
        cell_up_down(row - 1, *main_val)
        left_cell(row - 1, *main_val)
        right_cell(row - 1, *main_val)
    if len(realboard) > row + 1:
        cell_up_down(row + 1, *main_val)
        left_cell(row + 1, *main_val)
        right_cell(row + 1, *main_val)


def left_cell(row, col, realboard, playboard, game_dict):  # opens cells in case they are clear of mines
    if 0 < col <= len(realboard) - 1:
        value = cell_value(row, col - 1, realboard)
        if value != 'x':
            playboard[row][col - 1] = value
            game_dict[(row, col)] = False
            if value == 0:
                open_cells(row, col - 1, realboard, playboard, game_dict)


def right_cell(row, col, realboard, playboard, game_dict):  # opens cells in case they are clear of mines
    if 0 <= col < len(realboard) - 1:
        value = cell_value(row, col + 1, realboard)
        if value != 'x':
            playboard[row][col + 1] = value
            game_dict[(row, col)] = False
            if value == 0:
                open_cells(row, col + 1, realboard, playboard, game_dict)


def cell_up_down(row, col, realboard, playboard, game_dict):  # opens cells in case they are clear of mines
    if 0 <= row <= len(realboard) - 1:
        value = cell_value(row, col, realboard)  # Returns the cell value in the real board
        if value != 'x':
            playboard[row][col] = value
            if value == 0:
                open_cells(row, col, realboard, playboard, game_dict)


def play_again():
    answer = input("would you like to play again? (y/n):")
    while True:  # str input validation
        if answer.lower() == 'y':
            print("OK , lets play again!")
            _ans = 1
            minesweeper(_ans)
        if answer.lower() == 'n':
            print("goodbye!")
            exit()
        else:
            print("wrong input")
            answer = input("would you like to play again? (y/n):")


def minesweeper(_ans=0):  # user interact function
    if _ans == 0:  # to prevent title reprint
        print("------Minesweeper-----")
    print()
    size = input("Enter the size of the play board: ")
    num_of_mines = input("Enter the number of mines:")
    while True:  # allowing only 9x9 size board game and less than 2*size mines
        if size.isdigit() and num_of_mines.isdigit() and 1 < int(size) <= 9 and int(num_of_mines) < 2 * int(size):
            size = int(size)
            num_of_mines = int(num_of_mines)
            break
        else:
            print("notice ! the play board most be less than 9X9:")
            size = input("Enter the size of the play board: ")
            num_of_mines = input("Enter the number of mines:")
    blank_board = create_game_board(size, num_of_mines)
    playboard = Create_PlayBoard(size)
    history_dict = Game_dict(blank_board)
    play(blank_board, playboard, history_dict)


minesweeper()
