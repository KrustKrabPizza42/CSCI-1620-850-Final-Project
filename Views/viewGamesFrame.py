from mainMenu import *

class ViewGamesFrame(Frame):
    """
    Frame that inherits the TK Frame class, used for viewing individual game details
    """

    def __init__(self, master = None, **kwargs) -> None:
        """
        Initializes the frame and puts it onto the root window
        :param root: the root window this frame is a part of
        :param kwargs: parameters for the TK frame
        """
        super().__init__(self, master, **kwargs)

    def populate_game_list(self) -> None:

        pass