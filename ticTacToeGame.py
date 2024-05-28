print('Welcome to Tic Tac Toe!')
game_on=True
p=''
test_board = list([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
while True:
    game_on=replay()
    if game_on==True:
        test_board = list([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
        marker=player_input()
        cf=choose_first()
        if cf==True:
            print('Player 1 will go first')
        else:
            print('Player 2 will go first')
        if marker=='O' and cf==True:
            p='X'
        elif marker=='X' and cf==True:
            p='O'
        elif marker=='O' and cf==False:
            marker='X'
            p='O'
        elif marker=='X' and cf==False:
            marker='O'
            p='X'
        while game_on:
            position=player_choice(test_board)
            test_board=place_marker(test_board,marker,position)
            display_board(test_board)
            p1=win_check(test_board,marker)
            y=full_board_check(test_board)
            if p1==True:
                print('Congratulations! You have won the game!')
                break
            elif y==True:
                print('Match is Draw')
                break
            position=player_choice(test_board)
            test_board=place_marker(test_board,p,position)
            display_board(test_board)
            p2=win_check(test_board,p)
            y=full_board_check(test_board)
            if p2==True:
                print('Player 2 Won the game')
                break
            elif y==True:
                print('Match is Draw')
                break
    else: break