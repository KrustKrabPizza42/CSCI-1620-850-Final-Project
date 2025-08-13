
from Views.MainMenuFrame import MainMenuFrame
from Views.NewPlayerFrame import *
from Views.NewDeckFrame import *
from Views.NewGameFrame import *
from data.DataLists import *

#makes the main window, uses the other frame classes to decide which frame to display
class MainMenu(Tk):

    def __init__(self, version):

        Tk.__init__(self)

        self.version = version

        self.title(version)
        self.geometry('300x250')


        #menu ribbon setup
        self.menu = Menu(self)
        self.config(menu=self.menu)

        #file menu options
        self.filemenu = Menu(self.menu)

        self.filemenu.add_separator()
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New Game', command=lambda: self.change_frame(NewGameFrame))
        self.filemenu.add_command(label='New Player', command=lambda: self.change_frame(NewPlayerFrame))
        self.filemenu.add_command(label='New Deck', command=lambda: self.change_frame(NewDeckFrame))
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.quit)

        #Meu to reurn to main menu
        self.menu.add_command(label='Main Menu', command=self.return_to_main)

        self.frame = MainMenuFrame(self)

        self.frame.pack()

    #Used for the menu ribbon's button to return to Main Menu
    def return_to_main(self):

        self.frame.pack_forget()
        self.frame = MainMenuFrame(self)
        self.frame.pack()

    def change_frame(self, frame):

        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()

    #Saves the game info to a CSV file
    def save_game(self, game_model):

        with open(data.DataLists.data_lists.filepaths['game file'], 'a', newline='') as csv_game_file:
            with open (data.DataLists.data_lists.filepaths['join file'], 'a', newline='') as csv_join_file:
                
                game_writer = DictWriter(csv_game_file, fieldnames=['Game Id (Pk)','Date','First Player Id',
                                                                    'First Out Id','Total Turns','Friendship counters',
                                                                    'Notes'])
                
                join_writer = DictWriter(csv_join_file, fieldnames=['Game Id','Deck Id (Fk)','Player Id (Fk)',
                                                                    'Turn 1 Sol Ring', 'Loss Reason'])

                game_writer.writerow({'Game Id (Pk)': game_model.game_id,'Date': game_model.date,
                                    'First Player Id': game_model.first_player,'First Out Id': game_model.first_out,
                                    'Total Turns': game_model.total_turns, 'Friendship counters': 20,'Notes': ''})
                
                for player in game_model.players_data:
                    
                    join_writer.writerow({'Game Id': game_model.game_id,'Deck Id (Fk)': player.deck_id,
                                        'Player Id (Fk)': player.player_id,'Turn 1 Sol Ring': player.turn_1_sol_ring,
                                        'Loss Reason': player.loss_reason})
                    
        data.DataLists.data_lists.populate_game_lists()

    def save_new_player(self, player_model):

        with open(data.DataLists.data_lists.filepaths['player file'], 'a', newline='') as csv_player_table:

            player_writer = DictWriter(csv_player_table, fieldnames=['Player ID (PK)','First Name','Last Name'])

            player_writer.writerow({'Player ID (PK)': player_model.player_id,'First Name': player_model.first_name,
                                    'Last Name': player_model.last_name})
            
        data.DataLists.data_lists.populate_player_lists()

    def save_new_deck(self, deck_model):

        with open(data.DataLists.data_lists.filepaths['deck file'], 'a', newline='') as csv_deck_table:

            deck_writer = DictWriter(csv_deck_table, fieldnames=['Deck ID (PK)','Player ID (FK)','Commander'])

            deck_writer.writerow({'Deck ID (PK)':deck_model.deck_id,'Player ID (FK)': deck_model.owner,
                                  'Commander': deck_model.commander})

        data.DataLists.data_lists.populate_deck_lists()