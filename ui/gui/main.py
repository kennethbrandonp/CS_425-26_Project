import constants as preset
from frontend.sceneManager import SceneManager
from backend.modelManager import ModelManager
from tkinter import Tk

"""
sources:
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/widgets/
https://www.pythontutorial.net/tkinter/tkinter-grid/
"""


class SpyOT(Tk):
    """
    Structure:
        Controller (class SpyOT):
            - Contains the calls to the frontend and back-end methods
            - Instantiates all program scenes and initiates the frontend with them
            - Handles the communication between the frontend and back-end

            Back-end (class modelManager) :
                - Updates the internal data models and program state in response to the users input
                - Handles the processing of stored data and responds to frontend requests for that data

            Front-end (class sceneManager):
                - Displays the current scene
                - Reads input from the user
                - Requests data from the back-end according to the current scenes needs
                - Reads input from the user and, if necessary, sends that input to the back-end
                - Updates the current scene depending on user input and back-end updates

    Scene: Screens in our application
        - Title_Scene: Contains the title screen which prompts the user to select/create a profile
        - Profile_Main_Menu: Contains the main menu for a selected profile and displays their
            notifications and network summary
        - Profile_Security: Contains the security screen for a selected profile where the user's
            device summaries and configurations are available
        - Profile_Settings: Contains the settings screen with various options for the selected
            profile to choose and adjust
    """
    def __init__(self, title=preset.title):
        super().__init__()
        self.title(title)
        self.backend = ModelManager()
        self.frontend = SceneManager(self)


def main():
    demo = SpyOT("SpyOT Demo")
    demo.mainloop()


if __name__ == '__main__':
    main()
