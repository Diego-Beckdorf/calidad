import utilities


class BoardWriter(object):
    def __init__(self):
        pass

    def is_cell_available(self, board, row, column):
        cell_value = board.read_cell(row=row, column=column)
        if cell_value == '':
            return True
        return False

    def write_cell(self, board, row, column, sign):
        if (utilities.is_coordinates_inside_bounds(
                board=board, row=row, column=column)
                and self.is_cell_available(
                board=board, row=row, column=column)):
            board.cells[row][column] = sign
            return True
        return False
