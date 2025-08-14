from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from Models.gameModel import *
import Views.mainMenuFrame
import Views.newGameAddPlayerFrame
import data.DataLists
from mainMenu import *


#Frame for a new game entry form; includes methods to retrieve the data
class NewGameFrame(Frame):
    """
    Frame that inherits the TK Frame class, used for the new game menu
    """

    def __init__(self, root=None, **kwargs) -> None:
        """
        Initializes the frame and puts it onto the root window
        :param root: the root window this frame is a part of
        :param kwargs: parameters for the TK frame
        """
        Frame.__init__(self, root, **kwargs)

        self.player_frame_list = []
        self.game_id: str = ''
        self.num_of_players: int = 0

        self.root: MainMenu = root


        self.get_game_id()

        root.geometry('1000x600')


        self.frame1: Frame = Frame(self)
        self.new_game_label: Label = Label(self.frame1, text='Enter a new game')
        self.game_id_label: Label = Label(self.frame1, text=f'Game Id: {self.game_id}')
        self.game_id_label.pack()
        self.new_game_label.pack()
        self.frame1.pack()

        self.frame2: Frame = Frame(self)
        self.date_label: Label = Label(self.frame2, text='Date: ')
        self.date_entry: DateEntry = DateEntry(self.frame2, date_pattern ='yyyy-mm-dd')
        self.date_label.pack()
        self.date_entry.pack()
        self.frame2.pack(pady=5, padx=5)

        self.frame3: Frame = Frame(self)
        self.first_player_label: Label = Label(self.frame3, text='First player: ')
        self.first_player_box: ttk.Combobox = ttk.Combobox(self.frame3, state='readonly', values=data.DataLists.data_lists.possible_players)
        self.first_player_label.pack()
        self.first_player_box.pack()
        self.frame3.pack(pady=5, padx=5)

        self.frame4: Frame = Frame(self)
        self.first_out_label: Label = Label(self.frame4, text='First Out: ')
        self.first_out_box: ttk.Combobox = ttk.Combobox(self.frame4, state='readonly', values=data.DataLists.data_lists.possible_players)
        self.first_out_label.pack()
        self.first_out_box.pack()
        self.frame4.pack(pady=5, padx=5)

        self.frame5: Frame = Frame(self)
        self.total_turns_label: Label = Label(self.frame5, text='Total Turns: ')
        self.turn_count: Spinbox = Spinbox(self.frame5, from_=1, to=50)
        self.total_turns_label.pack()
        self.turn_count.pack()
        self.frame5.pack(pady=5, padx=5)

        self.frame6: Frame = Frame(self)
        self.date_input: Entry = Entry(self.frame6)
        self.add_player_button: Button = Button(self.frame6, text='Add Player', command=lambda: self.add_player(self.frame7))
        self.test_button: Button = Button(self.frame6, text='SAVE', command=self.get_form_data)
        self.add_player_button.pack(side='top')
        self.test_button.pack()
        self.frame6.pack(pady=5, padx=5)

        self.frame7: Frame = Frame(self)
        self.frame7.pack(pady=5, padx=5)

    #Method to add a frame for a new player
    def add_player(self, frame) -> None:
        """
        Used to add a player frame to the root frame
        :param frame: The root frame
        """

        self.num_of_players += 1
        self.player_frame_list.append(Views.newGameAddPlayerFrame.AddPlayerFrame(frame))

        for frame in self.player_frame_list:
            frame.pack(side='left')

    #method to retrieve info from the form; and save the data
    def get_form_data(self) -> None:
        """
        Gets the data from the form, saves it as a GameModel and sends it to be saved to CSV
        Gives an error if a section is not filled
        """

        new_game: GameModel = GameModel()

        new_game.game_id = self.game_id
        new_game.date = self.date_entry.get()
        new_game.players_data = self.get_players()

        for dict in data.DataLists.data_lists.possible_players_dicts:

            if self.first_out_box.get() == (dict['Last Name'] + ', ' + dict['First Name']):
                new_game.first_out = dict['Player ID (PK)']
            
            if self.first_player_box.get() == (dict['Last Name'] + ', ' + dict['First Name']):
                new_game.first_player = dict['Player ID (PK)']

        new_game.total_turns = self.turn_count.get()

        self.get_game_id()

        if new_game.date == '' or len(new_game.players_data) < self.num_of_players or new_game.first_out == '' or new_game.first_player == '':

            self.new_game_label.config(text='Error: Please fill out all fields', bg='Red')

        else:
                self.root.save_game(new_game)
                data.DataLists.data_lists.populate_game_lists()
                self.return_to_main()

    #method to return to main menu
    def return_to_main(self) -> None:
        """
        Returns to the main menu frame
        """
        self.root.change_frame(Views.mainMenuFrame.MainMenuFrame)

    #Method to retrieve the info from the pl
    def get_players(self)  -> list:
        """
        Gets the information from each player frame and adds it to a list to be added to the GameModel
        :return: List of individual player info
        """

        players: list = []

        for frame in self.player_frame_list:

            if frame.get_player() is not None:
                players.append(frame.get_player())

        return players

    #Method to get the last game ID and to make the next one (last ID + 1)
    def get_game_id(self) -> None:
        """
        Sets the game ID to be the next one in the sequence in proper format
        """

        self.game_id: str = f'G-{len(data.DataLists.data_lists.game_table_dicts) +1}'