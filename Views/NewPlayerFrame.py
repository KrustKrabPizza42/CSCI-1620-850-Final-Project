from tkinter import *
from tkinter import ttk
from Main_Menu import *
import Views.MainMenuFrame
import Views.NewGameAddPlayerFrame
import Models.PlayerModel

#Frame for a new game entry form; includes methods to retrieve the data
class NewPlayerFrame(Frame):

    def __init__(self, root=None, **kwargs):
        Frame.__init__(self, root, **kwargs)

        self.root = root

        root.geometry('500x250')


        self.frame1 = Frame(self)
        self.new_player_label = Label(self.frame1, text='Add a new player')
        self.new_player_label.pack()
        self.frame1.pack()

        self.frame2 = Frame(self)
        self.player_id_label = Label(self.frame2, text='Player ID')
        self.player_id_entry = Entry(self.frame2)
        self.player_id_label.pack()
        self.player_id_entry.pack()
        self.frame2.pack(pady=5, padx=5)

        self.frame3 = Frame(self)
        self.first_name_label = Label(self.frame3, text='First Name')
        self.first_name_box = Entry(self.frame3)
        self.first_name_label.pack()
        self.first_name_box.pack()
        self.frame3.pack(pady=5, padx=5)

        self.frame4 = Frame(self)
        self.last_name_label = Label(self.frame4, text='Last Name')
        self.last_name_box = Entry(self.frame4)
        self.last_name_label.pack()
        self.last_name_box.pack()
        self.frame4.pack(pady=5, padx=5)

        self.frame5 = Frame(self)
        self.save_player_button = Button(self.frame5, text='SAVE', command=self.get_form_data)
        self.save_player_button.pack()
        self.frame5.pack()

    def get_form_data(self):

        new_player = Models.PlayerModel

        new_player.player_id = self.player_id_entry.get()
        new_player.first_name = self.first_name_box.get()
        new_player.last_name = self.last_name_box.get()

        self.root.save_new_player(new_player)
        self.return_to_main()

    #method to return to main menu
    def return_to_main(self):
        self.root.change_frame(Views.MainMenuFrame.MainMenuFrame)