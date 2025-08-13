from tkinter import *
from tkinter import ttk
from Views.newGameFrame import *
from data.DataLists import *
from mainMenu import *


# frame for the main menu with 6 options so far
class MainMenuFrame(Frame):
    """
    Frame that inherits the TK Frame class, used for the main menu
    """

    def __init__(self, root=None, **kwargs) -> None:
        """
        Initializes the frame and puts it onto the root window
        :param root: the root window this frame is a part of
        :param kwargs: parameters for the TK frame
        """

        Frame.__init__(self, root, **kwargs)

        self.root: MainMenu = root

        self.root.geometry('700x500')

        # first frame for greeting and title
        self.frame0: Frame = Frame(self)
        self.greetings_banner: Label = Label(self.frame0, text='MTG Game Tracker')
        self.greetings_banner.pack(pady=20)
        self.frame0.pack(pady=10)

        self.frame1: Frame = Frame(self)
        self.game_list_box: Listbox = Listbox(self.frame1, width=75, height=15)
        self.list_box_index = 0
        for game in data_lists.game_table_dicts:
            self.game_list_box.insert(self.list_box_index+1,
                                      f'Game Id (Pk): {game['Game Id (Pk)']}    Date: {game['Date']}    Total Turns: {game['Total Turns']}')

        self.game_list_box.pack()
        self.frame1.pack()


    def new_game_frame(self) -> None:

        self.root.change_frame(NewGameFrame)