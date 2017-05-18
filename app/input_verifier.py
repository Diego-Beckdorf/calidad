import console
import utilities

COLUMNS = 'abcdefghijklmnopqrstuvwxyz'
INSTRUCTION_SET = ['start', 'board', 'play', 'score', 'exit', 'help']


def verify_instruction(user_input):
    user_input = user_input.split()
    instruction = user_input[0].lower()
    if instruction not in INSTRUCTION_SET:
        console.write_line(message='Error: Unrecognized instruction.')
        return False
    return instruction


def check_start_options(user_input):
    options = ''
    user_input = user_input.split()
    for option in user_input[1:]:
        if option == '--consecutive':
            options += 'consecutive'
        if option == '--silent':
            options += 'silent'
    return options


def verify_board_dimension(user_input):
    user_input = user_input.split()
    dimension = user_input[-1]
    if utilities.is_integer(dimension):
        dimension = int(dimension)
        if dimension > 0:
            return dimension
        console.write_line(message='Error: Board dimension must be larger than zero.')
        return False
    console.write_line(message='Error: Board dimension must be an integer.')
    return False


def play_arguments(user_input):
    user_input = user_input.split()
    coordinates = user_input[-1]
    column_label = coordinates[0]
    column = COLUMNS.find(column_label)
    if not utilities.is_integer(coordinates[1:]):
        console.write_line(message='Error: Coordinates not allow.')
        return None
    row = int(coordinates[1:]) - 1
    if row < 0:
        console.write_line(message='Error: Row outside board bounds.')
        return None
    sign = user_input[1]
    return [column, row, sign]
