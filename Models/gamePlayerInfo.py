

#model for Player data from one game
class GamePlayerInfo:
    """
    Model for Player information from and individual game to be added to the appropriate CSV file
    """

    def __init__(self, player_id, deck_id, turn_1_sol_ring, loss_reason) -> None:
        """
        Initializes player id, deck id, turn 1 sol ring, and loss reason
        :param player_id: ID of the player
        :param deck_id: Id of the deck the player used
        :param turn_1_sol_ring: 0 or 1 if a turn 1 sol ring was played
        :param loss_reason: loss reason
        """

        self.player_id = player_id
        self.deck_id = deck_id
        self.turn_1_sol_ring = turn_1_sol_ring
        self.loss_reason = loss_reason

    def __str__(self) -> str:
        """
        Returns a string of all the class variables
        :return: String of class variables
        """

        return (f'Player: {self.player_id}\nDeck Id: {self.deck_id}\n'
                f'Turn 1 sol ring: {self.turn_1_sol_ring}\nLoss Reason: {self.loss_reason}')