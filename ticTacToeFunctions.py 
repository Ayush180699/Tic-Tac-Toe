from IPython.display import clear_output
import random
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    
def player_input():
    marker=''
    while marker not in('O','X'):
        marker = input('Player 1: Do you want to be X or O')
    return marker

#test_board = ['#','','O','X','O','X','O','X','O','X']
def player_choice(board):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(test_board,pos):
        pos=int(input('Choose your next position: (1-9)'))
    return pos

            
def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):
    if board[1]==mark and board[2]==mark and board[3]==mark or board[4]==mark and board[5]==mark and board[6]==mark or board[7]==mark and board[8]==mark and board[9]==mark or board[1]==mark and board[4]==mark and board[7]==mark or board[2]==mark and board[5]==mark and board[8]==mark or board[3]==mark and board[6]==mark and board[9]==mark or board[1]==mark and board[5]==mark and board[9]==mark or board[3]==mark and board[5]==mark and board[7]==mark:
        return True


def choose_first():
    z=random.randint(1,2)
    if z==1:
        return True
    else:
        return False

def full_board_check(board):
    if board.count('O') + board.count('X')>=9:
        return True
    else:
        return False
    
def space_check(board, position):
    return board[position]==' '
    
def replay():
    r='wro'
    while r not in ['Y','N']:
        r=input('DO you want to continue Y/N')
    if r=='Y':
        return True
    else: return False
    