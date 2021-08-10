def display_board(board):
    print('\n'*5)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("_|_|_")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("_|_|_")
    print(board[1]+'|'+board[2]+'|'+board[3])

# players choose identifiction
def player_inputs():
    indict = ""
    while indict != "X" and indict != "O":
        indict = input("Player1: Choose X or O: ").upper()
    if indict == "X":
        return ("X", "O")
    else:
        return ("O",'X')

# placing the chosen position
def place_indict(board, indict, position):
    board[position]=indict

#  win check
def win_check(board, indict):
    return ((board[1]== board[2]== board[3]== indict)or
           (board[4]== board[5]==board[6]==indict)or
            (board[7]==board[8]==board[9]==indict)or
            (board[7]==board[4]== board[1]==indict)or
           (board[8]==board[5]==board[2]==indict)or
           (board[3]==board[6]==board[9]==indict)or
           (board[1]==board[5]==board[9]==indict)or
           (board[3]==board[5]==board[7]==indict))

#  first to play
import random
def choose_fplayer():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# check for vacant spaces
def space_check(board, position):
    
    return board[position] == ' '



# check for vacant spaces
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# accepting input
def player_choice(board):
    position = 0
    
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position= int(input('Choose a position: (1-9) '))
    return position

# game replay choice
def replay():
    CON_TOPLAY=input('Play again? Yes or No')
    return CON_TOPLAY == 'Yes'




print('Welcome to Tic Tac Toe')

while True:
    
    t_board =[' ']*10
    player1_indict , player2_indict = player_inputs()
    
    turn = choose_fplayer()
    print(turn + 'Will go first')
    
    play_game = input("Ready to play? y or n ")
    if play_game == 'y':
        game_strt = True
    else:
        game_strt = False
        
        
    while game_strt:
        if turn == 'Player1':
            display_board(t_board)
            position = player_choice(t_board)
            place_indict(t_board, player1_indict, position)
            
            if win_check(t_board, player1_indict):
                display_board(t_board)
                print('Player 1 HAS WON!')
                game_strt= False
            
            
            
            else:
                if full_board_check(t_board):
                    display_board(t_board)
                    print('TIE GAME')
                    game_strt= False
                else:
                    turn = 'Player2'
                    
                    
                    
        else:
            display_board(t_board)
            position = player_choice(t_board)
            place_indict(t_board, player2_indict, position)
            
            if win_check(t_board, player2_indict):
                display_board(t_board)
                print('Player 2 HAS WON!')
                game_strt= False
            
            
            
            else:
                if full_board_check(t_board):
                    display_board(t_board)
                    print('TIE GAME')
                    game_strt= False
                else:
                    turn = 'Player1'
                    
                    
                    
                    
                    
                    
    if not replay():
        break
                    
                    