
class Console(object):
    def __init__(self):
        pass

    def read_line(self, message='TicTacToe> '):
        return raw_input(message)

    def write_line(self, message):
        print message

    def show_board(self, board):
        board_render = board.render()
        for line in board_render:
            print('\t'.join(line))

    def show_winner(self, winner):
        if winner in 'xo':
            self.write_line(message='Player {0} Won!'.format(winner.upper()))
        elif winner == 'tied':
            self.write_line(message='Game Tied')

    def show_score(self, score):
        self.write_line(message='Actual Score:')
        self.write_line(message='\t {0} games played'.format(score['games']))
        self.write_line(message='\t {0} games won by X'.format(score['x']))
        self.write_line(message='\t {0} games won by O'.format(score['o']))
        self.write_line(message='\t {0} games tied'.format(score['tied']))
