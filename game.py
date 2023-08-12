from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    ans = ' '
    
    #Keep asking player one their choice
    while ans not in ['X','O']:
          ans = input("Player 1, choose X or O: ").upper()
            
    #assign Player 2, the opposite marker
    player_1= ans 
    
    if player_1 == 'O':
        player_2 = 'X'
    else:
        player_2 = 'O'
        
    return {player_1,player_2}

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    
    #WIN TIC TAC TOE?
    #ALL ROWS,and check to see if they all share the same marker
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    #ALL COLUMNS , check to see if they all share the same marker 
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    #2 DIAGONALS, check to see if they match 
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

import random 

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
             return False
    
    #Board is full is we return 
    return True

def player_choice(board):
    
    position =0 
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
        
    return position

def replay():
    
    ans = 'Wrong'
    
    while ans not in ['Y','N']:
        ans = input("DO YOU WANT TO PLAY AGAIN(Y/N): ").upper()
        
    if ans not in ['Y','N']:
        print("I don't understand!")
        
    if ans == 'Y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe')

#while True:
while True:
    #play game 
     
    ##set everything up(board,whos first,Choose markers X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn +' will go first')
    
    play_game = input("Ready to play! Y or N").upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        
    ##Game play
    while game_on:
        
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player1_marker,position)
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 won!!')
                game_on = False                
            #check if it is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    break
            #No tie and no win? Then next player's turn
                else:
                    turn = 'Player 2'  
        ###Player One turn 
        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player2_marker,position)
            #Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 won!!')
                game_on = False                
            #check if it is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    break
            #No tie and no win? Then next player's turn
                else:
                    turn = 'Player 1'
        ###Player Two turn 

    
#break out of the loop 
    if replay() != True:
        break