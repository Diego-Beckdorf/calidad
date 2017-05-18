def read_cell(board, row, column):
    return board.cells[row][column]


def read_column(board, column):
    board_column = []
    for row in board.cells:
        board_column.append(row[column])
    return board_column


def read_row(board, row):
    return board.cells[row]


def read_diagonal(board, main=True):
    diagonal = []
    column = 0 if main else (board.dimension - 1)
    for row in board.cells:
        diagonal.append(row[column])
        column = column + 1 if main else (column - 1)
    return diagonal
