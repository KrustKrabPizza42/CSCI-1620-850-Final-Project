from string import whitespace
from tkinter import *
from tkinter import ttk
from mainMenu import *
import Views.mainMenuFrame
import Views.newGameAddPlayerFrame
import data.DataLists
from Models.deckmodel import *

#Frame for a new game entry form; includes methods to retrieve the data
class NewDeckFrame(Frame):
    """
    Frame that inherits the TK Frame class, used for the new deck menu
    """

    def __init__(self, root=None, **kwargs) -> None:
        """
        Initializes the frame and puts it onto the root window
        :param root: the root window this frame is a part of
        :param kwargs: parameters for the TK frame
        """
        Frame.__init__(self, root, **kwargs)

        self.root = root

        root.geometry('500x250')

        self.deck_id = 0
        self.get_deck_id()

        self.frame1: Frame = Frame(self)
        self.new_deck_label: Label = Label(self.frame1, text='Add a new Deck')
        self.deck_id_label: Label  = Label(self.frame1, text=f'Deck Id: {self.deck_id}')
        self.new_deck_label.pack()
        self.deck_id_label.pack()
        self.frame1.pack()

        self.frame2: Frame = Frame(self)
        self.player_id_label: Label = Label(self.frame1, text='Deck Owner')
        self.player_id_entry: ttk.Combobox = ttk.Combobox(self.frame2, state='readonly',
                                                          values=data.DataLists.data_lists.possible_players)
        self.player_id_label.pack()
        self.player_id_entry.pack()
        self.frame2.pack(pady=5, padx=5)

        self.frame3: Frame = Frame(self)
        self.commander_label: Label = Label(self.frame3, text='Commander')
        self.commander_box: Entry = Entry(self.frame3)
        self.commander_label.pack()
        self.commander_box.pack()
        self.frame3.pack(pady=5, padx=5)

        self.frame5: Frame = Frame(self)
        self.save_player_button: Button = Button(self.frame5, text='SAVE', command=self.get_form_data)
        self.save_player_button.pack()
        self.frame5.pack()

    def get_form_data(self) -> None:
        """
        When called gets the information from the form and saves it to a Deck Model that is passed back to the root
        window to be saved to a CSV file
        """

        new_deck: DeckModel = DeckModel(self.deck_id, self.player_id_entry.get(), self.commander_box.get())

        for player in data.DataLists.data_lists.possible_players_dicts:
            if new_deck.owner == player['Last Name'] + ', ' + player['First Name']:
                new_deck.owner = player['Player ID (PK)']

        if new_deck.owner =='' or new_deck.commander == '':
            self.new_deck_label.config(text='Error: Please fill out all sections', bg='Red')

        else:
            self.root.save_new_deck(new_deck)
            self.return_to_main()



    def get_deck_id(self) -> None:
        """
        Sets the class' deck id to the next appropriate ID with proper format
        """

        self.deck_id = f'D-{len(data.DataLists.data_lists.deck_lists) + 1}'

    #method to return to main menu
    def return_to_main(self) -> None:
        """
        Returns to the main menu frame
        """
        self.root.change_frame(Views.mainMenuFrame.MainMenuFrame)