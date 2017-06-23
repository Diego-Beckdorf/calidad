import board_writer
import console
from input_verifier import InputVerifier
from board import Board


class TicTacToe(object):
    def __init__(self):
        self.game_started = False
        self.online_flag = False
        self._opponent_found = False
        self.is_local_turn = False
        self._opponent_name = ''
        self.consecutive_flag = False
        self.expected_player = 'o'
        self.silent_flag = False
        self.console = console.Console()
        self.input_verifier = InputVerifier()
        self.board = None
        self.online_score = {'games': 0, 'won': 0, 'losts': {}, 'ties': {}}
        self.score = {'games': 0, 'o': 0, 'x': 0, 'tied': 0}

    def set_options(self, valid_options):
        if 'online' in valid_options:
            self.online_flag = True
        if 'consecutive' in valid_options:
            if self.online_flag:
                message = "can't start game online with consecutive mode"
                self.console.write_line(message=message)
                return False
            self.consecutive_flag = True
        if 'silent' in valid_options:
            self.silent_flag = True
        return True

    def start(self, user_input):
        options = self.input_verifier.check_start_options(
            user_input=user_input)
        verified_board_dimension = self.input_verifier.verify_board_dimension(
            user_input=user_input)
        if not verified_board_dimension:
            return False
        self.board = Board(dimension=verified_board_dimension)
        options_setted = self.set_options(valid_options=options)
        if not options_setted:
            return False
        if self.online_flag:
            self.online_score['games'] += 1
        else:
            self.score['games'] += 1
        self.game_started = True
        return True

    def on_opponent_found(self, name, local_moves_first):
        self._opponentFound = True
        self.is_local_turn = local_moves_first
        self._opponent_name = name

    def play(self, user_input):
        arguments = self.input_verifier.play_arguments(user_input=user_input,
                                                       online=self.online_flag)
        column = arguments[0]
        row = arguments[1]
        sign = 'x' if self.online_flag else arguments[2]
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
            if self.online_flag:
                self.expected_player = 'x'
                return True
            self.expected_player = 'o' if self.expected_player == 'x' else 'x'
        return True

    def row_winner(self, board):
        for row_index in range(board.dimension):
            row = board.read_row(row=row_index)
            if row.count('o') == board.dimension:
                return 'o'
            elif row.count('x') == board.dimension:
                return 'x'
        return None

    def column_winner(self, board):
        for column_index in range(board.dimension):
            column = board.read_column(column=column_index)
            if column.count('o') == board.dimension:
                return 'o'
            elif column.count('x') == board.dimension:
                return 'x'
        return None

    def diagonal_winner(self, board):
        main_diagonal = board.read_diagonal()
        anti_diagonal = board.read_diagonal(main=False)
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
        if board is None:
            return False
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
        if winner:
            self.console.show_winner(winner=winner)
            self.score[winner] += 1
            self.board = None
            self.game_started = False


def main():
    tic_tac_toe = TicTacToe()
    input_verifier = tic_tac_toe.input_verifier
    game_console = tic_tac_toe.console
    welcome_message = 'Hello! How about a game of TicTacToe?'
    game_console.write_line(message=welcome_message)
    while True:
        user_input = game_console.read_line()
        user_input = user_input.lower()
        verified_instruction = input_verifier.verify_instruction(
            user_input=user_input)
        if not verified_instruction:
            continue
        if verified_instruction == 'start' and not tic_tac_toe.game_started:
            tic_tac_toe.start(user_input=user_input)
            if tic_tac_toe.online_flag:
                from external_component import ExternalComponent
                ext_component = ExternalComponent()
                try:
                    ext_component.initialize_connection()
                    size = tic_tac_toe.board.dimension
                    ext_component.request_online_opponent(
                        size_of_board=size,
                        callback_func=tic_tac_toe.on_opponent_found)
                except RuntimeError as exception:
                    message = 'Unable to establish connection with opoonent.'
                    game_console.write_line(message=message)
                    continue
        elif verified_instruction == 'start':
            message = 'Game already started. GAME ON!'
            game_console.write_line(message=message)
            continue
        if verified_instruction == 'board' and not tic_tac_toe.game_started:
            message = 'There is no game started to display.'
            game_console.write_line(message=message)
        elif verified_instruction == 'board':
            game_console.show_board(board=tic_tac_toe.board)
        if verified_instruction == 'play' and not tic_tac_toe.game_started:
            message = 'There is no game started to play on.'
            game_console.write_line(message=message)
        elif verified_instruction == 'play':
            if not tic_tac_toe.play(user_input=user_input):
                continue
            tic_tac_toe.update_game_status()
        if verified_instruction == 'score':
            game_console.show_score(score=tic_tac_toe.score)
        if verified_instruction == 'exit':
            game_console.write_line(message='bye!')
            break
        if verified_instruction == 'help':
            game_console.write_line(message='help')


if __name__ == "__main__":
    main()
