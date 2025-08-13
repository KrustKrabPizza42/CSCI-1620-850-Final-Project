

#model for Player data from one game
class GamePlayerInfo:

    def __init__(self, player_id, deck_id, turn_1_sol_ring, loss_reason):

        self.player_id = player_id
        self.deck_id = deck_id
        self.turn_1_sol_ring = turn_1_sol_ring
        self.loss_reason = loss_reason

    def __str__(self):

        return (f'Player: {self.player_id}\nDeck Id: {self.deck_id}\n'
                f'Turn 1 sol ring: {self.turn_1_sol_ring}\nLoss Reason: {self.loss_reason}')