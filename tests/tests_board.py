import unittest

import app.board


class BoardTest(unittest.TestCase):
    def test__render_headers__with_10_x_10_board__expecting_list_from_A_to_J(self):
        #Arrange
        board = app.board.Board(dimension=10)
        #Act
        headers = board.render_headers()
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        #Assert
        self.assertEqual(first=headers, second=expected)

    def test__render_rows__with_5_x_5_empty_board__expecting_list_of_5_lists_with_6_single_strings(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        rows = board.render_rows()
        expected = [['1', '', '', '', '', ''],
                    ['2', '', '', '', '', ''],
                    ['3', '', '', '', '', ''],
                    ['4', '', '', '', '', ''],
                    ['5', '', '', '', '', '']]
        #Assert
        self.assertEqual(first=rows, second=expected)

    def test__render__with_5_x_5_empty_board__expecting_list_of_6_lists_with_6_single_strings(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        rendered_board = board.render()
        expected = [['', 'A', 'B', 'C', 'D', 'E'],
                    ['1', '', '', '', '', ''],
                    ['2', '', '', '', '', ''],
                    ['3', '', '', '', '', ''],
                    ['4', '', '', '', '', ''],
                    ['5', '', '', '', '', '']]
        #Assert
        self.assertEqual(first=rendered_board, second=expected)

    def test__read_cell__from_empty_5_x_5_board_in_valid_coordinate_C2__expecting_empty_string(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        board_cell = board.read_cell(row=1, column=2)
        expected = ''
        #Assert
        self.assertEqual(first=board_cell, second=expected)

    def test__read_column__from_empty_board_5_x_5_column_C__expecting_5_empty_string_list(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        board_column = board.read_column(column=2)
        expected = ['', '', '', '', '']
        #Assert
        self.assertEqual(first=board_column, second=expected)

    def test__read_row__from_empty_board_5_x_5_row_4__expecting_5_empty_string_list(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        board_row = board.read_row(row=3)
        expected = ['', '', '', '', '']
        #Assert
        self.assertEqual(first=board_row, second=expected)

    def test__read_diagonal__from_o_main_diagonal_winer_board_5_x_5__expecting_5_o_string_list(self):
        #Arrange
        board = app.board.Board(dimension=5)
        for index in range(5):
            board.cells[index][index] = 'o'
        #Act
        board_main_diagonal = board.read_diagonal()
        expected = ['o', 'o', 'o', 'o', 'o']
        #Assert
        self.assertEqual(first=board_main_diagonal, second=expected)

    def test__read_diagonal__with_main_False_from_empty_board_5_x_5__expecting_5_empty_string_list(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        board_anti_diagonal = board.read_diagonal(main=False)
        expected = ['', '', '', '', '']
        #Assert
        self.assertEqual(first=board_anti_diagonal, second=expected)
