from tkinter import *
from tkinter import ttk
from csv import *
from Main_Menu import *
import data.DataLists
from Models.GamePlayerInfo import GamePlayerInfo


#Frame for the NewGameFrame only to add a player frame allowing for a variable of players per game
#Each sub frame is for each section of data in the GamePlayerInfo class
class AddPlayerFrame(Frame):


    def __init__(self, root=None, **kwargs):
        Frame.__init__(self, root, **kwargs)

        self.turn_1_sol_ring = IntVar()

        self.frame1 = Frame(self)
        self.player_label = Label(self.frame1, text='Player:')
        self.player_label.pack(pady=5, padx=5)
        self.frame1.pack(pady=5, padx=5)

        self.frame2 = Frame(self)
        self.player_id_label = Label(self.frame2, text='Player: ')
        self.player_id_box = ttk.Combobox(self.frame2, state='readonly', values=data.DataLists.data_lists.possible_players)
        self.player_id_label.pack(side='left')
        self.player_id_box.pack(side='right', pady=5, padx=5)
        self.frame2.pack(pady=5, padx=5)

        self.frame3 = Frame(self)
        self.deck_label = Label(self.frame3, text='Deck: ')
        self.deck_id_box = ttk.Combobox(self.frame3, state='readonly', values=data.DataLists.data_lists.deck_lists)
        self.deck_label.pack(side='left')
        self.deck_id_box.pack(side='right', pady=5, padx=5)
        self.frame3.pack(pady=5, padx=5)

        self.frame4 = Frame(self)
        self.turn_1_sol_ring_yes = Radiobutton(self.frame4, text='Yes', variable=self.turn_1_sol_ring, value=1)
        self.turn_1_sol_ring_no = Radiobutton(self.frame4, text='No', variable=self.turn_1_sol_ring, value=0)
        self.turn_1_sol_ring_yes.pack(side='left')
        self.turn_1_sol_ring_no.pack(side='right')
        self.frame4.pack(pady=5, padx=5)

        self.frame5 = Frame(self)
        self.loss_reason_label = Label(self.frame5, text='Loss Reason: ')
        self.loss_reason_box = ttk.Combobox(self.frame5, state='readonly', values=data.DataLists.data_lists.loss_reasons)
        self.loss_reason_label.pack(side='left')
        self.loss_reason_box.pack(side='right', pady=5, padx=5)
        self.frame5.pack(pady=5, padx=5)

    #Method to get the player info packaged into a player object and return it
    def get_player(self):

        self.player = GamePlayerInfo(self.player_id_box.get(), 0,
                                                        self.turn_1_sol_ring.get(), self.loss_reason_box.get())

        for dict in data.DataLists.data_lists.deck_lists_dicts:

            if self.deck_id_box.get() == dict['Commander']:

                self.player.deck_id = dict['Commander']
                
        for dict in data.DataLists.data_lists.possible_players_dicts:

            if self.player.player_id == (dict['Last Name'] + ', ' + dict['First Name']):

                self.player.player_id = dict['Player ID (PK)']

        return self.player
    
    #Method to fill the the lists for the deck drop down options
    def populate_deck_lists(self):

        with open('data/game table - Deck Table.csv', 'r') as csv_decks:

            reader = DictReader(csv_decks)

            for row in reader:
                self.deck_lists_dicts.append(row)
                self.deck_lists.append(row['Commander'])
