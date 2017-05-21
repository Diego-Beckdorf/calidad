import unittest
import mock

from app.board_writer import BoardWriter


class BoardWriterTest(unittest.TestCase):
    def test_is_cell_available__with_coordinates_B3_with_o_filled_board__expecting_False_return(self):
        #Arrange
        board_writer = BoardWriter()
        board_stud = mock.MagicMock()
        board_stud.read_cell.return_value = 'o'
        #Act
        is_cell_available = board_writer.is_cell_available(board=board_stud,
                                                           row=2, column=1)
        #Assert
        self.assertFalse(expr=is_cell_available)

    @mock.patch('app.board_writer.utilities')
    def test_write_cell__with_coordinates_B3_available_sign_x__expecting_False_return(self, fake_utilities):
        #Arrange
        board_writer = BoardWriter()
        board_stud = mock.MagicMock()
        board_stud.read_cell.return_value = ''
        fake_utilities.is_coordinates_inside_bounds.return_value = True
        #Act
        is_cell_available = board_writer.write_cell(board=board_stud, row=2,
                                                    column=1, sign='x')
        #Assert
        self.assertTrue(expr=is_cell_available)

    @mock.patch('app.board_writer.utilities')
    def test_write_cell__with_coordinates_B3_unavailable_sign_x__expecting_False_return(self, fake_utilities):
        #Arrange
        board_writer = BoardWriter()
        board_stud = mock.MagicMock()
        board_stud.read_cell.return_value = 'o'
        fake_utilities.is_coordinates_inside_bounds.return_value = True
        #Act
        is_cell_available = board_writer.write_cell(board=board_stud, row=2,
                                                    column=1, sign='x')
        #Assert
        self.assertFalse(expr=is_cell_available)
