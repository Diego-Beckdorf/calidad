import unittest
import mock

import app.board


class BoardTest(unittest.TestCase):
    def test__get_headers__with_10_x_10_board__expecting_list_from_A_to_J(self):
        #Arrange
        board = app.board.Board(dimension=10)
        #Act
        headers = board.get_headers()
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        #Assert
        self.assertEqual(first=headers, second=expected)

    def test__get_rows__with_5_x_5_empty_board__expecting_list_of_5_lists_with_6_single_strings(self):
        #Arrange
        board = app.board.Board(dimension=5)
        #Act
        rows = board.get_rows()
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

