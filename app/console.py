def read_line(message='TicTacToe> '):
    return raw_input(message)


def write_line(message):
    print message


def show_board(board):
    board_render = board.render()
    for line in board_render:
        print('\t'.join(line))


def show_winner(winner):
    if winner in 'xo':
        write_line(message='Player {0} Won!'.format(winner.upper()))
    elif winner == 'tied':
        write_line(message='Game Tied')


def show_score(score):
    write_line(message='Actual Score:')
    write_line(message='\t {0} games played'.format(score['games']))
    write_line(message='\t {0} games won by X'.format(score['x']))
    write_line(message='\t {0} games won by O'.format(score['o']))
    write_line(message='\t {0} games tied'.format(score['tied']))
