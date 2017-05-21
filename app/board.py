class Board(object):
    def __init__(self, dimension=0):
        self.dimension = dimension
        self.cells = []
        for row in range(dimension):
            row = [''] * dimension
            self.cells.append(row)

    def render_headers(self, first_header_code=65):
        last_header_code = first_header_code + len(self.cells)
        headers = [chr(character) for character in range(first_header_code,
                                                         last_header_code)]
        return headers

    def render_rows(self):
        rows = []
        line_idx = 1
        for line in self.cells:
            rows.append([str(line_idx)] + line)
            line_idx += 1
        return rows

    def render(self):
        headers = self.render_headers()
        board = [[''] + headers]
        rows = self.render_rows()
        board += rows
        return board

    def read_cell(self, row, column):
        cells = self.cells
        cell = cells[row][column]
        return cell

    def read_column(self, column):
        board_column = []
        for row in self.cells:
            board_column.append(row[column])
        return board_column

    def read_row(self, row):
        return self.cells[row]

    def read_diagonal(self, main=True):
        diagonal = []
        column = 0 if main else (self.dimension - 1)
        for row in self.cells:
            diagonal.append(row[column])
            column = column + 1 if main else (column - 1)
        return diagonal
