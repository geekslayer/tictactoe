### this will be the main program
import os

import signal
import sys

#######

__msg_move_already_done:str = 'A move already has been done here, please choose another square! '
__move_must_be_valid:str = 'You must enter a valid move between 1 and 9'
__no_winner_its_a_tie:str = 'Nobody won it\'s a tie!!!!'

__input__intro_player_x_or_o:str = 'Player 1, what do you want to be X or O? '
__input__want_to_replay:str = 'Do you want to play a game? Type yes or y if you want to play again. '

#######

empty_square:str = ' '
board = [0,1,2]
player_symbol = [1,2]
player_in_turn = 0
done = False
turns_played = 0

move_mapping = [([0,2]),([1,2]),([2,2]),([0,1]),([1,1]),([2,1]),([0,0]),([1,0]),([2,0])]

########

def clear():
    cleared = False
    try:
        os.system('cls')
        cleared = True
    except Exception as e:
        pass

    if not cleared:
        try:
            os.system('clear')
            cleared = True
        except Exception as e:
            pass

def init_board():
    global board, turns_played, done

    turns_played = 0
    done = False
    board[0] = [empty_square]*3
    board[1] = [empty_square]*3
    board[2] = [empty_square]*3

def print_board():
    global board
    print(f'{board[0][0]}|{board[0][1]}|{board[0][2]}')
    print(f'{board[1][0]}|{board[1][1]}|{board[1][2]}')
    print(f'{board[2][0]}|{board[2][1]}|{board[2][2]}')

def print_clean_board():
    init_board()
    print_board()

def validate_move(move:int,x:int,y:int):
    global board, player_symbol,turns_played

    if board[y][x] == empty_square:
        board[y][x] = player_symbol[player_in_turn-1]
    else:
        turns_played -= 1
        print(__msg_move_already_done)
        next_move()

def determine_index(move:int):
    global board, player_symbol,turns_played,move_mapping

    position = move_mapping[move-1]
    validate_move(move,position[0],position[1])

    # if move == 1:
    #     validate_move(move,0,2)
    # elif move == 2:
    #     validate_move(move,1,2)
    # elif move == 3:
    #     validate_move(move,2,2)
    # elif move == 4:
    #     validate_move(move,0,1)
    # elif move == 5:
    #     validate_move(move,1,1)
    # elif move == 6:
    #     validate_move(move,2,1)
    # elif move == 7:
    #     validate_move(move,0,0)
    # elif move == 8:
    #     validate_move(move,1,0)
    # elif move == 9:
    #     validate_move(move,2,0)

def is_player_winner(player_number:int):
    global board, player_symbol

    if (board[0][2] == board[1][2] == board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][1] == board[1][1] == board[2][1] == player_symbol[player_number]):
        return True
    elif (board[0][0] == board[1][0] == board[2][0] == player_symbol[player_number]):
        return True
    elif (board[0][0] == board[0][1] == board[0][2] == player_symbol[player_number]):
        return True
    elif (board[1][0] == board[1][1] == board[1][2] == player_symbol[player_number]):
        return True
    elif (board[2][0] == board[2][1] == board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][0] == board[1][1] == board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][2] == board[1][1] == board[2][0] == player_symbol[player_number]):
        return True

    return False

def print_in_game_board(position:int):
    global done, turns_played
    
    determine_index(position)
    clear()
    print_board()
    turns_played += 1

    done = is_player_winner(player_in_turn-1) or turns_played >= 9

def next_move():
    global player_in_turn
    move = input(f'Player {player_in_turn} play your turn ')

    try:
        move = int(move)
    except Exception as e:
        pass

    if type(move) != int:
        print(__move_must_be_valid)
        next_move()
    else:
        if move >= 1 and move <= 9:
            print_in_game_board(move)
        else:
            print(__move_must_be_valid)
            next_move()

def play_tictactoe():
    global player_symbol,player_in_turn, turns_played, done
    clear()
    
    player_symbol[0] = input(__input__intro_player_x_or_o).upper()

    if player_symbol[0] == 'X':
        player_symbol[1] = 'O'
    else:
        player_symbol[1] = 'X'

    player_in_turn = 1

    init_board()

    ######

    clear()
    while not done:
        if turns_played == 0:
            print_board()

        next_move()

        if done: break

        if player_in_turn == 1:
            player_in_turn = 2
        else:
            player_in_turn = 1

    if is_player_winner(player_in_turn-1):
        print(f'Player # {player_in_turn} is the big winner')
    else:
        print(__no_winner_its_a_tie)

    answer = input(__input__want_to_replay).lower()

    if answer == 'yes' or answer[0] == 'y':
        play_tictactoe()

###########

try:

    play_tictactoe()

except KeyboardInterrupt:
    print('Game has been interupted!! Ctrl + C was pressed!!! :(')
    sys.exit()
    
