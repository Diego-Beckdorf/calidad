import board_reader
import utilities

def is_cell_available(board, row, column):
    cell_value = board_reader.read_cell(board=board, row=row, column=column)
    if cell_value == '':
        return True
    return False


def write_cell(board, row, column, sign):
    if (utilities.is_coordinates_inside_bounds(board=board, row=row,
                                               column=column)
            and is_cell_available(board=board, row=row, column=column)):
        board.cells[row][column] = sign
        return True
    return False
