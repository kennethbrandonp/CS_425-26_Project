from tkinter import *
from tkinter import ttk
import constants as preset


class SpyOT:
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


    Scene: Window screens in our application
        - Title_Scene: Contains the title screen which prompts the user to select/create a profile
        - Create_Profile_Scene: Contains entry fields for the user to fill in their profile data
        - Select_Profile_Scene: Contains a list of saved profiles that the user may select
        - Profile_Main_Menu: Contains the main menu for a selected profile and displays their
            notifications and network summary
        - Profile_Security: Contains the security screen for a selected profile where the user's
            device summaries and configurations are available
        - Profile_Settings: Contains the settings screen with various options for the selected
            profile to choose and adjust
    """

    def __init__(self):
        self.root = Tk()
        self.configure_root()
        self.current_scene = None
        self.scenes = {
            "title": Title(self),
        }
        self.current_scene = self.scenes["title"]

    def mainloop(self):
        self.current_scene.display_frame()
        self.root.mainloop()

    def set_title(self, new_title):
        self.root.title(new_title)

    def configure_root(self):
        self.root.geometry(preset.default_geometry)
        self.root.title(preset.title)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
