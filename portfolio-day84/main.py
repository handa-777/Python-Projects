import random

tokens = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

ver_line = "-----------"
board_length = len(tokens[0])


def game_start():
    print("Welcome to Tic Tac Toe\n")
    game_choice()


def game_choice():
    while True:
        game_type = input("Do you want to play with friends?(1) or with Computer?(2)\nPress 1 or 2: ")
        if game_type == '1':
            multi_game()
            break
        elif game_type == '2':
            single_game()
            break
        else:
            print("Wrong Input. Please enter 1 or 2.")


def single_game():
    player = input("Choose X or O: ").upper()
    player_num = 0
    computer_num = 0
    turn_count = 0
    max_turn = 0
    while True:
        if player == 'X':
            player_num += 1
            computer_num += 2
            max_turn += 8
            break
        elif player == 'O':
            player_num += 2
            computer_num += 1
            max_turn += 9
            break
        else:
            print("Please choose between X or O")

    if player_num == 1:
        get_token(player_num)
        print_board()

    while True:
        if turn_count % 2 == 0:
            random_play(computer_num)
        else:
            get_token(player_num)
        print_board()
        game_over = check_game_over()

        if game_over == player_num:
            print("Game Over! You Win!")
            break
        elif game_over == computer_num:
            print("Game Over! You Lose!")
            break

        turn_count += 1
        if turn_count == max_turn:
            print(f"Game Over! Draw!")
            break


def random_play(computer_num):
    while True:
        row_num = random.randint(1, 3)
        col_num = random.randint(1, 3)
        if 1 <= row_num <= 3 and 1 <= col_num <= 3 and tokens[row_num - 1][col_num - 1] == 0:
            tokens[row_num - 1][col_num - 1] = computer_num
            break


def multi_game():
    player_num = 1
    turn_count = 0
    print("Please enter the location where you want to place the token.\n\n")

    while True:
        print(f'Player {player_num}\n')
        get_token(player_num)
        print_board()
        game_over = check_game_over()
        if game_over != 0:
            print(f"Game Over! The winner is Player {game_over}!")
            break

        turn_count += 1
        if turn_count == 9:
            print(f"Game Over! Draw!")
            break

        if turn_count % 2 == 0:
            player_num += -1
        else:
            player_num += 1


def get_token(player_num):
    while True:
        row_num = int(input("Please enter the row number you want.(from 1 to 3): "))
        col_num = int(input("Please enter the column number you want.(from 1 to 3): "))
        if row_num > 3 or row_num < 1 or col_num > 3 or col_num < 1:
            print("Row number and Column number should be between 1 and 3. Please try again.")
        elif tokens[row_num - 1][col_num - 1] != 0:
            print("You can't place a token in a location where it already exists. Please try again.")
        else:
            tokens[row_num - 1][col_num - 1] = player_num
            break


def print_board():
    for row in range(0, board_length):
        hor_line = ''
        for col in range(0, board_length):
            if tokens[row][col] == 0:
                hor_line += '   '
            elif tokens[row][col] == 1:
                hor_line += ' X '
            else:
                hor_line += ' O '
            if col != 2:
                hor_line += '|'
        print(hor_line)
        if row == 2:
            print('\n')
        else:
            print(ver_line)


def check_game_over():
    winner = 0
    for row in tokens:
        if row.count(row[0]) == board_length:
            winner = row[0]
            break

    for i in range(0, board_length):
        if tokens[0][i] == tokens[1][i] and tokens[0][i] == tokens[2][i]:
            winner = tokens[0][i]
            break

    if tokens[1][1]:
        if (tokens[0][0] == tokens[1][1] and tokens[0][0] == tokens[2][2]
                or tokens[0][2] == tokens[1][1] and tokens[0][2] == tokens[2][0]):
            winner = tokens[0][0]

    return winner
    

game_start()
