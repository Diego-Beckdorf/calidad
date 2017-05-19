import unittest
import mock

import app.board_reader


class BoardReaderTest(unittest.TestCase):
    def test__read_cell__from_empty_5_x_5_board_on_valid_coordinates_B3__expecting_empty_string(self):
        #Arrange
        board_stub = mock.MagicMock()
        board_row_stub = mock.MagicMock()
        board_row_stub.__getitem.return_value = ['', '', '', '', '']
        board_cells_stub = mock.MagicMock()
        board_cells_stub.__getitem.return_value = board_row_stub
        board_stub.cells.return_value = board_cells_stub[1][2]
        #Act
        cell_value = app.board_reader.read_cell(board=board_stub, row=1, column=2)
        #Assert
        self.assertEqual(first=cell_value, second='')
