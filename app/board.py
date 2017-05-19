class Board(object):
    def __init__(self, dimension=0):
        self.dimension = dimension
        self.cells = []
        for row in range(dimension):
            row = [''] * dimension
            self.cells.append(row)

    def get_headers(self, first_header_code=65):
        last_header_code = first_header_code + len(self.cells)
        headers = [chr(character) for character in range(first_header_code,
                                                         last_header_code)]
        return headers

    def get_rows(self):
        rows = []
        line_idx = 1
        for line in self.cells:
            rows.append([str(line_idx)] + line)
            line_idx += 1
        return rows

    def render(self):
        headers = self.get_headers()
        board = [[''] + headers]
        rows = self.get_rows()
        board += rows
        return board
