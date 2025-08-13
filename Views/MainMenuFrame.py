from tkinter import *
from tkinter import ttk
from Views.NewGameFrame import *
from data.DataLists import *


# frame for the main menu with 6 options so far
class MainMenuFrame(Frame):

    def __init__(self, root=None, **kwargs):

        Frame.__init__(self, root, **kwargs)

        self.root = root

        self.root.geometry('700x500')

        # first frame for greeting and title
        self.frame0 = Frame(self)
        self.greetings_banner = Label(self.frame0, text='MTG Game Tracker')
        self.greetings_banner.pack(pady=20)
        self.frame0.pack(pady=10)

        self.frame1 = Frame(self)
        self.game_list_box = Listbox(self.frame1, width=75, height=15)
        self.list_box_index = 0
        for game in data_lists.game_table_dicts:
            self.game_list_box.insert(self.list_box_index+1,
                                      f'Game Id (Pk): {game['Game Id (Pk)']}    Date: {game['Date']}    Total Turns: {game['Total Turns']}')

        self.game_list_box.pack()
        self.frame1.pack()


    def new_game_frame(self):

        self.root.change_frame(NewGameFrame)