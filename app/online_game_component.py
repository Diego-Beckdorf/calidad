from datetime import datetime

import external_component


class OnlineGameComponent(object):
    def __init__(self):
        try:
            external_component.initialize_connection()
            self.initialized = True
            self._opponent_found = False
            self._is_local_turn = False
            self._opponent_name = ''
            self.connection_established = False
        except RuntimeError:
            self.initialized = False

    def on_opponent_found(self, name, local_moves_first):
        self._opponent_found = True
        self._is_local_turn = local_moves_first
        self._opponent_name = name

    def local_turn(self):
        return self._is_local_turn

    def establish_connection(self, board_dimension):
        try:
            request_datetime = datetime.today()
            external_component.request_online_oponent(
                size_of_board=board_dimension,
                callback_function=self.on_oponent_found)
            while True:
                if self._opponentFound:
                    break
                current_datetime = datetime.today()
                time_delta = current_datetime - request_datetime
                if time_delta.seconds > 30:
                    raise RuntimeError
            return True
        except RuntimeError:
            return False

    def send_local_move(self, position):
        external_component.set_my_last_move(posotion=position)

    def oponent_last_move(self):
        return external_component.get_opponent_last_move()

    def close_connection(self):
        external_component.close_connection()
        self._opponentFound = False
        self._is_local_turn = False
        self._opponent_name = ''
        self.connection_established = False
