from console import Console
import utilities


class InputVerifier(object):
    def __init__(self):
        self.notifier = Console()
        self.columns_labels = 'abcdefghijklmnopqrstuvwxyz'
        self.instructions_set = ['start', 'board', 'play',
                                 'score', 'exit', 'help']

    def verify_instruction(self, user_input):
        user_input = user_input.split()
        instruction = user_input[0].lower()
        if instruction not in self.instructions_set:
            message = 'Error: Unrecognized instruction.'
            self.notifier.write_line(message=message)
            return False
        return instruction

    def check_start_options(self, user_input):
        options = ''
        user_input = user_input.split()
        for option in user_input[1:]:
            if option == '-consecutive':
                options += 'consecutive'
            if option == '-silent':
                options += 'silent'
            if option == '-online':
                options += 'online'
        return options

    def verify_board_dimension(self, user_input):
        user_input = user_input.split()
        dimension = user_input[-1]
        if utilities.is_integer(dimension):
            dimension = int(dimension)
            if dimension > 0 and dimension <=26:
                return dimension
            message = 'Error: Board dimension must be larger than zero.'
            self.notifier.write_line(message=message)
            return False
        message = 'Error: Board dimension must be an integer.'
        self.notifier.write_line(message=message)
        return False

    def play_arguments(self, user_input, online=False):
        user_input = user_input.lower()
        user_input = user_input.split()
        coordinates = user_input[-1]
        column_label = coordinates[0]
        column = self.columns_labels.find(column_label)
        if not utilities.is_integer(coordinates[1:]):
            message = 'Error: Coordinates not allow.'
            self.notifier.write_line(message=message)
            return None
        row = int(coordinates[1:]) - 1
        if row < 0:
            message = 'Error: Row outside board bounds.'
            self.notifier.write_line(message=message)
            return None
        sign = 'x' if online else user_input[1]
        if sign not in 'ox':
            message = 'Error: Player sign not valid.'
            self.notifier.write_line(message=message)
            return None
        return [column, row, sign]
