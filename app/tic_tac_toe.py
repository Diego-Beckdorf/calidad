import board_reader
import board_writer
import console
import input_verifier
from board import Board

GAME_STARTED = False
CONSECUTIVE_FLAG = False
EXPECTED_PLAYER = 'o'
SILENT_FLAG = False


def set_options(valid_options):
    global CONSECUTIVE_FLAG
    global SILENT_FLAG
    if 'consecutive' in valid_options:
        CONSECUTIVE_FLAG = True
    if 'silent' in valid_options:
        SILENT_FLAG = True


def start(user_input):
    options = input_verifier.check_start_options(user_input=user_input)
    verified_board_dimension = input_verifier.verify_board_dimension(user_input=user_input)
    if not verified_board_dimension:
        return False
    board = Board(dimension=verified_board_dimension)
    set_options(valid_options=options)
    return board


def play(user_input, board):
    global EXPECTED_PLAYER
    arguments = input_verifier.play_arguments(user_input=user_input)
    column = arguments[0]
    row = arguments[1]
    sign = arguments[2]
    if not CONSECUTIVE_FLAG and sign != EXPECTED_PLAYER:
        console.write_line(message='Not your turn! waiting for player {0} to play'.format(EXPECTED_PLAYER))
        return False
    if not board_writer.write_cell(board=board, row=row, column=column, sign=sign):
        console.write_line(message='Try again!')
        return False
    if not CONSECUTIVE_FLAG:
        EXPECTED_PLAYER = 'o' if EXPECTED_PLAYER == 'x' else 'x'
    return True


def row_winner(board):
    for row_index in range(board.dimension):
        row = board_reader.read_row(board=board, row=row_index)
        if row.count('o') == board.dimension:
            return 'o'
        elif row.count('x') == board.dimension:
            return 'x'
    return False


def column_winner(board):
    for column_index in range(board.dimension):
        column = board_reader.read_column(board=board, column=column_index)
        if column.count('o') == board.dimension:
            return 'o'
        elif column.count('x') == board.dimension:
            return 'x'
    return None


def diagonal_winner(board):
    main_diagonal = board_reader.read_diagonal(board=board)
    anti_diagonal = board_reader.read_diagonal(board=board, main=False)
    if main_diagonal.count('o') == board.dimension or anti_diagonal.count('o') == board.dimension:
        return 'o'
    elif main_diagonal.count('x') == board.dimension or anti_diagonal.count('x') == board.dimension:
        return 'x'
    return None


def tied(board):
    free_cells = sum([row.count('') for row in board.cells])
    if free_cells > 0:
        return None
    return 'tied'



def check_game_result(board):
    if row_winner(board=board):
        return row_winner(board=board)
    if column_winner(board=board):
        return column_winner(board=board)
    if diagonal_winner(board=board):
        return diagonal_winner(board=board)
    if tied(board=board):
        return tied(board=board)
    return False


def update_game_status(board, score):
    winner = check_game_result(board=board)
    console.show_winner(winner=winner)
    if winner:
        score[winner] += 1
        return None
    return board


def main():
    console.write_line(message='Hello! How about a game of TicTacToe?')
    score = {'games': 0, 'o': 0, 'x': 0, 'tied': 0}
    options = ''
    board = None
    while True:
        user_input = console.read_line()
        user_input = user_input.lower()
        verified_instruction = input_verifier.verify_instruction(user_input=user_input)
        if not verified_instruction:
            continue
        if verified_instruction == 'start' and not board:
            board = start(user_input=user_input)
            score['games'] += 1
        elif verified_instruction == 'start':
            console.write_line(message='Game already started. GAME ON!')
            continue
        if verified_instruction == 'board' and not board:
            console.write_line(message='There is no game started to display.')
        elif verified_instruction == 'board':
            console.show_board(board=board)
        if verified_instruction == 'play' and not board:
            console.write_line(message='There is no game started to play on.')
        elif verified_instruction == 'play':
            if not play(user_input=user_input, board=board):
                continue
            board = update_game_status(board=board, score=score)
        if verified_instruction == 'score':
            console.show_score(score)
        if verified_instruction == 'exit':
            console.write_line(message='bye!')
            break
        if verified_instruction == 'help':
            console.write_line(message='help')


if __name__ == "__main__":
    main()
