
class DeckModel():

    def __init__(self, deck_id, owner, commander):

        self.deck_id = deck_id
        self.owner = owner
        self.commander = commander

    def __str__(self):

        return f'Deck ID: {self.deck_id}\nOwner: {self.owner}\nCommander: {self.commander}'