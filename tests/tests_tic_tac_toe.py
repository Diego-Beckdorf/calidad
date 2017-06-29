import unittest

import app.tic_tac_toe
import coverage


class TicTacToeTest(unittest.TestCase):
    def test__check_game_result__none_board__expecting_False(self):
        #Arrange
        game = app.tic_tac_toe.TicTacToe()
        #Act
        winer = game.check_game_result()
        #Assert
        self.assertFalse(expr=winer)

    def test__start__with_online_option_and_dimension_3__resturns_True(self):
        #Arrange
        game = app.tic_tac_toe.TicTacToe()
        #Act
        result = game.start(user_input='start -online Beckdorf 3')
        #Assert
        self.assertTrue(expr=result)

    def test__set_options__with_online_and_consecutive_options__return_False(self):
        #Arrange
        game = app.tic_tac_toe.TicTacToe()
        #Act
        result = game.set_options(valid_options='onlineconsecutive')
        #Assert
        self.assertFalse(expr=result)

    def test__set_options__with_silente_option__return_True(self):
        #Arrange
        game = app.tic_tac_toe.TicTacToe()
        #Act
        result = game.set_options(valid_options='silente')
        #Assert
        self.assertTrue(expr=result)
