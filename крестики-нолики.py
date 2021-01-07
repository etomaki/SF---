game_board = list(range(1, 10))
copy_board = game_board.copy()

def allow_win():
    win = (copy_board[:3], copy_board[3:6], copy_board[6:9], copy_board[0:7:3], copy_board[1:8:3], copy_board[2:9:3], copy_board[0:9:4], copy_board[2:7:2])
    x_ = ['X','X','X']
    o_ = ['O','O','O']
    for i in win:
        if x_ == i:
            return 'x'
    for n in win:
        if o_ == n:
            return 'o'

def board_(board):
    print('')
    for i in range(3):
        print(str(board[i*3]) + ' | ' + str(board[i*3+1]) + ' | ' + str(board[i*3+2]))
        print('---------') if i < 2 else False
    print('')

def player_choice(token):
    allow_values = [str(i) for i in range(1,10)]
    if token % 2 != 0:
        player = input('Куда поставить X? ')
    else:                                               #X и O
        player = input('Куда поставить O? ')
    if player not in allow_values:
        print('Неверное значение, попробуйте снова...')     #Если значение не равно 1-9
        player_choice(token)
    elif copy_board[int(player) - 1] in ('X','O'):
        print('Клетка занята...')                           #Если клетка занята
        player_choice(token)
    else:
        if token % 2 != 0:
            copy_board[int(player) - 1] = 'X'
        else:                                               #Если все верно
            copy_board[int(player) - 1] = 'O'

def game():
    token = 1
    board_(game_board)
    while True:
        player_choice(token)
        board_(copy_board)
        token += 1
        allow_win()
        if allow_win() == 'x':
            print(' Победа X ')
            break
        if allow_win() == 'o':
            print(' Победа O ')
            break
        if token == 10:
            print('Ничья')
            break
    print('------------------------')
    
game()