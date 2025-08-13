
class DeckModel():
    """
    Model for deck information to be added to the appropriate CSV file
    """

    def __init__(self, deck_id, owner, commander) -> None:
        """
        Initializes the deck id, owner, and commander

        :param deck_id: Deck Id
        :param owner: Owner of the Deck
        :param commander: Deck's Commander
        """

        self.deck_id = deck_id
        self.owner = owner
        self.commander = commander

    def __str__(self) -> str:
        """
        Returns a string of all the class variables
        :return: String of class variables
        """

        return f'Deck ID: {self.deck_id}\nOwner: {self.owner}\nCommander: {self.commander}'