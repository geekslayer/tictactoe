### this will be the main program
import os

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
    board[0] = [empty_square,empty_square,empty_square]
    board[1] = [empty_square,empty_square,empty_square]
    board[2] = [empty_square,empty_square,empty_square]

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
        print('A move already has been done here, please choose another square! ')
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

    if (board[0][2] == player_symbol[player_number] and board[1][2] == player_symbol[player_number] and board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][1] == player_symbol[player_number] and board[1][1] == player_symbol[player_number] and board[2][1] == player_symbol[player_number]):
        return True
    elif (board[0][0] == player_symbol[player_number] and board[1][0] == player_symbol[player_number] and board[2][0] == player_symbol[player_number]):
        return True
    elif (board[0][0] == player_symbol[player_number] and board[0][1] == player_symbol[player_number] and board[0][2] == player_symbol[player_number]):
        return True
    elif (board[1][0] == player_symbol[player_number] and board[1][1] == player_symbol[player_number] and board[1][2] == player_symbol[player_number]):
        return True
    elif (board[2][0] == player_symbol[player_number] and board[2][1] == player_symbol[player_number] and board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][0] == player_symbol[player_number] and board[1][1] == player_symbol[player_number] and board[2][2] == player_symbol[player_number]):
        return True
    elif (board[0][2] == player_symbol[player_number] and board[1][1] == player_symbol[player_number] and board[2][0] == player_symbol[player_number]):
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
    move = input(f'Player {player_in_turn} play your turn ')

    try:
        move = int(move)
    except Exception as e:
        pass

    if type(move) != int:
        print('You must enter a valid move between 1 and 9')
        next_move()
    else:
        if move >= 1 and move <= 9:
            print_in_game_board(move)
        else:
            print('You must enter a valid move between 1 and 9')
            next_move()

def play_tictactoe():
    global player_symbol,player_in_turn, turns_played, done
    clear()
    
    player_symbol[0] = input('Player 1, what do you want to be X or O? ').upper()

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

        # move = int(input(f'Player {player_in_turn} play your turn '))
        # print_in_game_board(move)
        next_move()

        if done: break

        if player_in_turn == 1:
            player_in_turn = 2
        else:
            player_in_turn = 1

    if is_player_winner(player_in_turn-1):
        print(f'Player # {player_in_turn} is the big winner')
    else:
        print('Nobody won it is a tie!!!!')

    answer = input('Do you want to play a game? Type yes or y if you want to play again. ').lower()

    if answer == 'yes' or answer[0] == 'y':
        play_tictactoe()

###########

play_tictactoe()
# move = 8
# print(move_mapping[move-1])
