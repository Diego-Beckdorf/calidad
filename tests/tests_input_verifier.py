import unittest
import mock

from app.input_verifier import InputVerifier


class BoardWriterTest(unittest.TestCase):
    def test_verify_instruction__with_user_input_start_N__returns_start(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'start N'
        #Act
        instruction = input_verifier.verify_instruction(user_input=user_input)
        expected = 'start'
        #Assert
        self.assertEqual(first=instruction, second=expected)

    def test_verify_instruction__with_user_input_play__returns_play(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'play'
        #Act
        instruction = input_verifier.verify_instruction(user_input=user_input)
        expected = 'play'
        #Assert
        self.assertEqual(first=instruction, second=expected)

    def test_verify_instruction__with_user_input_board__returns_board(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'board'
        #Act
        instruction = input_verifier.verify_instruction(user_input=user_input)
        expected = 'board'
        #Assert
        self.assertEqual(first=instruction, second=expected)

    def test_verify_instruction__with_invalid_user_input__returns_False(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'invalid N'
        #Act
        instruction = input_verifier.verify_instruction(user_input=user_input)
        #Assert
        self.assertFalse(expr=instruction)

    def test_check_start_options__with_consecutive_flag__returns_consecutive_string(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'start N --consecutive'
        #Act
        options = input_verifier.check_start_options(user_input=user_input)
        expected = 'consecutive'
        #Assert
        self.assertEquals(first=options, second=expected)

    def test_check_start_options__with_invalid_flag__returns_empty_string(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'start N --invalid'
        #Act
        options = input_verifier.check_start_options(user_input=user_input)
        expected = ''
        #Assert
        self.assertEquals(first=options, second=expected)

    def test_verify_board_dimension__with_user_input_start_8__returns_True(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'start 8'
        #Act
        valid_dimension = input_verifier.verify_board_dimension(
            user_input=user_input)
        #Assert
        self.assertTrue(expr=valid_dimension)

    def test_verify_board_dimension__with_user_input_start_8000__returns_False(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'start 8000'
        #Act
        valid_dimension = input_verifier.verify_board_dimension(
            user_input=user_input)
        #Assert
        self.assertFalse(expr=valid_dimension)

    def test_play_arguments__with_user_input_play_o_B3__returns_list_1_2_o(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'play o B3'
        #Act
        playing_args = input_verifier.play_arguments(user_input=user_input)
        expected = [1, 2, 'o']
        #Assert
        self.assertEquals(first=playing_args, second=expected)

    def test_play_arguments__with_user_input_play_f_B3__returns_None(self):
        #Arrange
        input_verifier = InputVerifier()
        user_input = 'play f B3'
        #Act
        playing_args = input_verifier.play_arguments(user_input=user_input)
        #Assert
        self.assertIsNone(playing_args)
