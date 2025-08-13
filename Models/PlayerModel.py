
#model for Player data
class PlayerModel:

    def __init__(self, player_id, first_name, last_name):

        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):

        return f'Player Id: {self.player_id} \nFirst Name: {self.first_name} \nLast Name: {self.last_name}'