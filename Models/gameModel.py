

class GameModel:
    """
    Model for Game information to be added to the appropriate CSV file
    """

    def __init__(self) -> None:
        """
        Intializes a game model with empty variables
        """

        self.game_id = 0
        self.players_data = []
        self.date = ''
        self.first_out = ''
        self.first_player = ''
        self.total_turns = 0

    def __str__(self) -> str:
        """
        Returns a string of all the class variables
        :return: String of class variables
        """

        return (f'Game Id: {self.game_id}\nPlayers: {self.players_data}\n Date: {self.date}\n'
                f'First Out: {self.first_out}\n First Player: {self.first_player}\nTotal Turns: {self.total_turns}')