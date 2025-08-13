from tkinter import *
from tkinter import ttk
from mainMenu import *
import Views.mainMenuFrame
import Views.newGameAddPlayerFrame
from Models.playerModel import  PlayerModel

#Frame for a new game entry form; includes methods to retrieve the data
class NewPlayerFrame(Frame):
    """
    Frame that inherits the TK Frame class, used for the new player menu
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


        self.frame1: Frame = Frame(self)
        self.new_player_label: Label = Label(self.frame1, text='Add a new player')
        self.new_player_label.pack()
        self.frame1.pack()

        self.frame2: Frame = Frame(self)
        self.player_id_label: Label = Label(self.frame2, text='Player ID')
        self.player_id_entry: Entry = Entry(self.frame2)
        self.player_id_label.pack()
        self.player_id_entry.pack()
        self.frame2.pack(pady=5, padx=5)

        self.frame3: Frame = Frame(self)
        self.first_name_label: Label = Label(self.frame3, text='First Name')
        self.first_name_box: Entry = Entry(self.frame3)
        self.first_name_label.pack()
        self.first_name_box.pack()
        self.frame3.pack(pady=5, padx=5)

        self.frame4: Frame = Frame(self)
        self.last_name_label: Label = Label(self.frame4, text='Last Name')
        self.last_name_box: Entry = Entry(self.frame4)
        self.last_name_label.pack()
        self.last_name_box.pack()
        self.frame4.pack(pady=5, padx=5)

        self.frame5: Frame = Frame(self)
        self.save_player_button: Button = Button(self.frame5, text='SAVE', command=self.get_form_data)
        self.save_player_button.pack()
        self.frame5.pack()

    def get_form_data(self) -> None:

        new_player = PlayerModel(self.player_id_entry.get(), self.first_name_box.get(), self.last_name_box.get())

        self.root.save_new_player(new_player)
        self.return_to_main()

    #method to return to main menu
    def return_to_main(self) -> None:
        self.root.change_frame(Views.mainMenuFrame.MainMenuFrame)