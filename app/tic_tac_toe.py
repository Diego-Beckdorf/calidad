import board_reader
import board_writer
import console
from input_verifier import InputVerifier
from board import Board


class TicTacToe(object):
    def __init__(self):
        self.game_started = False
        self.consecutive_flag = False
        self.expected_player = 'o'
        self.silent_flag = False
        self.console = console.Console()
        self.board = None
        self.score = {'games': 0, 'o': 0, 'x': 0, 'tied': 0}

    def set_options(self, valid_options):
        if 'consecutive' in valid_options:
            self.consecutive_flag = True
        if 'silent' in valid_options:
            self.silent_flag = True

    def start(self, user_input):
        options = input_verifier.check_start_options(user_input=user_input)
        verified_board_dimension = input_verifier.verify_board_dimension(
            user_input=user_input)
        if not verified_board_dimension:
            return False
        self.board = Board(dimension=verified_board_dimension)
        self.set_options(valid_options=options)
        self.game_started = True
        self.score['games'] += 1
        return True

    def play(self, user_input):
        arguments = input_verifier.play_arguments(user_input=user_input)
        column = arguments[0]
        row = arguments[1]
        sign = arguments[2]
        if not self.consecutive_flag and sign != self.expected_player:
            message = 'Not your turn! waiting for player {0} to play'
            parsed_message = message.format(self.expected_player)
            self.console.write_line(message=parsed_message)
            return False
        if not board_writer.write_cell(board=self.board, row=row,
                                       column=column, sign=sign):
            self.console.write_line(message='Try again!')
            return False
        if not self.consecutive_flag:
            self.expected_player = 'o' if self.expected_player == 'x' else 'x'
        return True

    def row_winner(self, board):
        for row_index in range(board.dimension):
            row = board_reader.read_row(board=board, row=row_index)
            if row.count('o') == board.dimension:
                return 'o'
            elif row.count('x') == board.dimension:
                return 'x'
        return None

    def column_winner(self, board):
        for column_index in range(board.dimension):
            column = board_reader.read_column(board=board, column=column_index)
            if column.count('o') == board.dimension:
                return 'o'
            elif column.count('x') == board.dimension:
                return 'x'
        return None

    def diagonal_winner(self, board):
        main_diagonal = board_reader.read_diagonal(board=board)
        anti_diagonal = board_reader.read_diagonal(board=board, main=False)
        if (main_diagonal.count('o') == board.dimension or
                anti_diagonal.count('o') == board.dimension):
            return 'o'
        elif (main_diagonal.count('x') == board.dimension or
                anti_diagonal.count('x') == board.dimension):
            return 'x'
        return None

    def tied(self, board):
        free_cells = sum([row.count('') for row in board.cells])
        if free_cells > 0:
            return None
        return 'tied'

    def check_game_result(self):
        board = self.board
        if self.row_winner(board=board):
            return self.row_winner(board=board)
        if self.column_winner(board=board):
            return self.column_winner(board=board)
        if self.diagonal_winner(board=board):
            return self.diagonal_winner(board=board)
        if self.tied(board=board):
            return self.tied(board=board)
        return False

    def update_game_status(self):
        winner = self.check_game_result()
        self.console.show_winner(winner=winner)
        if winner:
            self.score[winner] += 1
            self.board = None
            self.game_started = False


def main():
    input_verifier = InputVerifier()
    tic_tac_toe = TicTacToe()
    game_console = tic_tac_toe.console
    welcome_message = 'Hello! How about a game of TicTacToe?'
    console.write_line(message=welcome_message)
    options = ''
    while True:
        user_input = console.read_line()
        user_input = user_input.lower()
        verified_instruction = input_verifier.verify_instruction(
            user_input=user_input)
        if not verified_instruction:
            continue
        if verified_instruction == 'start' and not tic_tac_toe.game_started:
            board = tic_tac_toe.start(user_input=user_input)
        elif verified_instruction == 'start':
            game_console.write_line(message='Game already started. GAME ON!')
            continue
        if verified_instruction == 'board' and not tic_tac_toe.game_started:
            game_console.write_line(message='There is no game started to display.')
        elif verified_instruction == 'board':
            game_console.show_board(board=board)
        if verified_instruction == 'play' and not tic_tac_toe.game_started:
            game_console.write_line(message='There is no game started to play on.')
        elif verified_instruction == 'play':
            if not tic_tac_toe.play(user_input=user_input):
                continue
            board = tic_tac_toe.update_game_status()
        if verified_instruction == 'score':
            game_console.show_score(score=tic_tac_toe.score)
        if verified_instruction == 'exit':
            game_console.write_line(message='bye!')
            break
        if verified_instruction == 'help':
            game_console.write_line(message='help')


if __name__ == "__main__":
    main()
