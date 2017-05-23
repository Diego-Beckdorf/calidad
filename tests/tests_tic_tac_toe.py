import unittest

import app.tic_tac_toe


class TicTacToeTest(unittest.TestCase):
    def test__check_game_result__none_board__expecting_False(self):
        #Arrange
        game = app.tic_tac_toe.TicTacToe()
        #Act
        winer = game.check_game_result()
        #Assert
        self.assertFalse(expr=winer)
