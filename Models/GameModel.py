

class GameModel:

    def __init__(self):

        self.game_id = 0
        self.players_data = []
        self.date = ''
        self.first_out = ''
        self.first_player = ''
        self.total_turns = 0

    def __str__(self):

        return (f'Game Id: {self.game_id}\nPlayers: {self.players_data}\n Date: {self.date}\n'
                f'First Out: {self.first_out}\n First Player: {self.first_player}\nTotal Turns: {self.total_turns}')