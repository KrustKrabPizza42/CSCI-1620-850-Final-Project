
#model for Player data
class PlayerModel:
    """
    Model for Player information to be added to the appropriate CSV file
    """

    def __init__(self, player_id, first_name, last_name) -> None:
        """
        Initializes player id, first and last name
        :param player_id: Player ID
        :param first_name: Player first name
        :param last_name: Player Last Name
        """

        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Returns a string of all the class variables
        :return: String of class variables
        """

        return f'Player Id: {self.player_id} \nFirst Name: {self.first_name} \nLast Name: {self.last_name}'