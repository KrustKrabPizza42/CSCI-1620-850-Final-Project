from csv import *
import os

class DataLists:

    def __init__(self):

        self.filepaths = {'deck file': 'data/deck table.csv', 'game file': 'data/game table.csv',
                          'join file': 'data/join table.csv', 'player file': 'data/player table.csv'}

        self.player_fields = ['Player ID (PK)','First Name','Last Name']
        self.game_fields = ['Game Id (Pk)','Date','First Player Id','First Out Id','Total Turns','Friendship counters',
                            'Notes']
        self.join_fields = ['Game Id','Deck Id (Fk)','Player Id (Fk)','Turn 1 Sol Ring', 'Loss Reason']
        self.deck_fields = ['Deck ID (PK)','Player ID (FK)','Commander']

        if not os.path.isfile('data/filepaths.csv'):
            self.create_file_paths()

        self.possible_players_dicts = []
        self.possible_players = []
        self.deck_lists = []
        self.loss_reasons = ['Combat Damage','Commander Damage','Deck Out','Infinite Combo','Drain',
                             'Alt win Con','Forfeit','Infect','Burn','Winner']
        self.game_table_dicts = []
        self.deck_lists_dicts = []
        self.join_table_dicts = []

        self.populate_player_lists()
        self.populate_game_lists()
        self.populate_deck_lists()
        self.populate_join_lists()

    def create_file_paths(self):

        with open('data/filepaths.csv', 'w') as csv_filepaths:
            writer = DictWriter(csv_filepaths,
                                fieldnames=['deck file', 'game file', 'join file', 'loss file', 'player file'])
            writer.writeheader()
            writer.writerow({'deck file': 'data/deck table.csv', 'game file': 'data/game table.csv',
                          'join file': 'data/join table.csv', 'loss file': 'data/loss table.csv',
                          'player file': 'data/player table.csv'})

    def get_file_paths(self):

        with open('data/filepaths.csv', 'r') as csv_filepaths:

            file_reader = DictReader(csv_filepaths)

            for dict in file_reader:
                self.filepaths = dict

    def populate_player_lists(self):

        if not os.path.isfile(self.filepaths['player file']):

            with open(self.filepaths['player file'], 'w', newline='') as csv_players:
                writer = DictWriter(csv_players, fieldnames=self.player_fields)
                writer.writeheader()

        else:
            with open(self.filepaths['player file'], 'r') as csv_players:

                csv_players.seek(0)

                self.possible_players_dicts = []
                self.possible_players = []

                reader = DictReader(csv_players)

                for row in reader:
                    self.possible_players_dicts.append(row)
                    self.possible_players.append(row['Last Name'] + ', ' + row['First Name'])

            self.possible_players.sort()


    def populate_game_lists(self):

        if not os.path.isfile(self.filepaths['game file']):

            with open(self.filepaths['game file'], 'w', newline='') as game_table:
                writer = DictWriter(game_table, fieldnames=self.game_fields)
                writer.writeheader()

        else:

            with open(self.filepaths['game file'], 'r') as game_table:
                game_table.seek(0)
                self.game_table_dicts = []
                reader = DictReader(game_table)

                for row in reader:
                    self.game_table_dicts.append(row)

    def populate_deck_lists(self):

        if not os.path.isfile(self.filepaths['deck file']):
            with open(self.filepaths['deck file'], 'w', newline='') as csv_decks:
                writer = DictWriter(csv_decks, fieldnames=self.deck_fields)
                writer.writeheader()

        else:
            with open(self.filepaths['deck file'], 'r') as csv_decks:

                csv_decks.seek(0)

                self.deck_lists_dicts = []
                self.deck_lists = []
                reader = DictReader(csv_decks)

                for row in reader:
                    self.deck_lists_dicts.append(row)
                    self.deck_lists.append(row['Commander'])

        self.deck_lists.sort()

    def populate_join_lists(self):
        if not os.path.isfile(self.filepaths['join file']):
            with open(self.filepaths['join file'], 'w', newline='') as csv_join_file:
                writer = DictWriter(csv_join_file, fieldnames=self.join_fields)
                writer.writeheader()

        else:

            with open(self.filepaths['join file'], 'r', newline='') as csv_join_file:

                csv_join_file.seek(0)

                self.join_table_dicts = []
                reader = DictReader(self.filepaths['join file'])

                for dict in reader:
                    self.join_table_dicts.append(dict)


data_lists = DataLists()