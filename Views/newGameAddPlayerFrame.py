from tkinter import *
from tkinter import ttk
from csv import *
from mainMenu import *
import data.DataLists
from Models.gamePlayerInfo import GamePlayerInfo


#Frame for the NewGameFrame only to add a player frame allowing for a variable of players per game
#Each sub frame is for each section of data in the GamePlayerInfo class
class AddPlayerFrame(Frame):
    """
    Frame that inherits the TK Frame class, used as a sub frame added to the new game menu
    """


    def __init__(self, root=None, **kwargs) -> None:
        """
        Initializes the frame and puts it onto the root window
        :param root: the root window this frame is a part of
        :param kwargs: parameters for the TK frame
        """
        Frame.__init__(self, root, **kwargs)

        self.deck_lists: list = []
        self.deck_lists_dicts: list = []
        self.turn_1_sol_ring: IntVar = IntVar()

        self.frame1: Frame = Frame(self)
        self.player_label: Label = Label(self.frame1, text='Player:')
        self.player_label.pack(pady=5, padx=5)
        self.frame1.pack(pady=5, padx=5)

        self.frame2: Frame = Frame(self)
        self.player_id_label: Label = Label(self.frame2, text='Player: ')
        self.player_id_box: ttk.Combobox = ttk.Combobox(self.frame2, state='readonly', values=data.DataLists.data_lists.possible_players)
        self.player_id_label.pack(side='left')
        self.player_id_box.pack(side='right', pady=5, padx=5)
        self.frame2.pack(pady=5, padx=5)

        self.frame3: Frame = Frame(self)
        self.deck_label: Label = Label(self.frame3, text='Deck: ')
        self.deck_id_box: ttk.Combobox = ttk.Combobox(self.frame3, state='readonly', values=data.DataLists.data_lists.deck_lists)
        self.deck_label.pack(side='left')
        self.deck_id_box.pack(side='right', pady=5, padx=5)
        self.frame3.pack(pady=5, padx=5)

        self.frame4: Frame = Frame(self)
        self.turn_1_sol_ring_label = Label(self.frame4, text='Turn 1 sol ring: ')
        self.turn_1_sol_ring_yes: Radiobutton = Radiobutton(self.frame4, text='Yes', variable=self.turn_1_sol_ring, value=1)
        self.turn_1_sol_ring_no: Radiobutton = Radiobutton(self.frame4, text='No', variable=self.turn_1_sol_ring, value=0)
        self.turn_1_sol_ring_label.pack(side='left')
        self.turn_1_sol_ring_yes.pack(side='left')
        self.turn_1_sol_ring_no.pack(side='right')
        self.frame4.pack(pady=5, padx=5)

        self.frame5: Frame = Frame(self)
        self.loss_reason_label: Label = Label(self.frame5, text='Loss Reason: ')
        self.loss_reason_box: ttk.Combobox = ttk.Combobox(self.frame5, state='readonly', values=data.DataLists.data_lists.loss_reasons)
        self.loss_reason_label.pack(side='left')
        self.loss_reason_box.pack(side='right', pady=5, padx=5)
        self.frame5.pack(pady=5, padx=5)

    #Method to get the player info packaged into a player object and return it
    def get_player(self) -> GamePlayerInfo:
        """
        Gets the appropriate info from this sub frame and returns a GamePlayerInfo model
        :return: GamePlayerInfo
        """

        self.player: GamePlayerInfo = GamePlayerInfo(self.player_id_box.get(), 0,
                                                        self.turn_1_sol_ring.get(), self.loss_reason_box.get())

        if self.player.player_id == '' or self.player.deck_id == '' or self.player.loss_reason == '':

            self.player_label.config(text='Error: Please fill in all sections', bg='Red')

        else:
            for dict in data.DataLists.data_lists.deck_lists_dicts:

                if self.deck_id_box.get() == dict['Commander']:

                    self.player.deck_id = dict['Commander']

            for dict in data.DataLists.data_lists.possible_players_dicts:

                if self.player.player_id == (dict['Last Name'] + ', ' + dict['First Name']):

                    self.player.player_id = dict['Player ID (PK)']

            return self.player
