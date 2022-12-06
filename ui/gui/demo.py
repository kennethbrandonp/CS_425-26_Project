from tkinter import *
from tkinter import ttk
import constants as preset


class SpyOT:
    """
    Structure:
        Controller (class SpyOT):
            - Contains the calls to the front-end and back-end methods
            - Instantiates all program scenes and initiates the front-end with them
            - Handles the communication between the front-end and back-end

            Back-end (class modelManager) :
                - Updates the internal data models and program state in response to the users input
                - Handles the processing of stored data and responds to front-end requests for that data

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
        self.current_scene = Title(self)

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


class Title:
    def __init__(self, SpyOT):
        self.SpyOT = SpyOT
        self.root = SpyOT.root
        style = ttk.Style()
        style.configure('Danger.TFrame', background='grey', borderwidth=5)
        self.frame = ttk.Frame(self.root, padding=3, style='Danger.TFrame')
        self.set_frame()
        self.buttons = []
        self.label = None
        self.set_widgets()

    def set_frame(self):
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)

    def display_frame(self):
        self.frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.display_widgets()

    def display_widgets(self):
        self.label.grid(column=1, row=0)
        for i, button in enumerate(self.buttons):
            button.grid(column=1, row=i + 1)

    def remove_frame(self):
        self.frame.grid_remove()

    def set_widgets(self):
        self.label = ttk.Label(self.frame, text=self.root.title(),
                               borderwidth=5, relief="raised")

        self.buttons.append(ttk.Button(self.frame, text="Create Profile",
                                       state="!disabled",
                                       command=lambda: self.change_scene("createProfile")))
        self.buttons.append(ttk.Button(self.frame, text="Select Profile", state="disabled"))
        self.buttons.append(ttk.Button(self.frame, text="Exit",
                                       state="!disabled", command=self.root.quit))

    def change_scene(self, next_scene):
        self.remove_frame()
        if next_scene == "createProfile":
            self.SpyOT.current_scene = CreateProfile(self.SpyOT)
            self.SpyOT.current_scene.display_frames()


class CreateProfile:
    def __init__(self, SpyOT):
        self.root = SpyOT.root
        self.set_frames()

        self.buttons = []
        self.label = None
        self.set_widgets()

    def set_frames(self):
        style = ttk.Style()
        style.configure('Danger.TFrame', background='grey', borderwidth=5)

        self.state_frame = ttk.Frame(self.root, padding=3, style="Danger.TFrame")
        self.state_frame.columnconfigure(0, weight=1)
        self.rows = 9
        for i in range(self.rows):
            self.state_frame.rowconfigure(i, weight=1)

        self.header = ttk.Frame(self.state_frame, padding=3, style="Danger.TFrame")
        self.header.columnconfigure(0, weight=1)
        self.header.rowconfigure(0, weight=1)

        self.body = ttk.Frame(self.state_frame, padding=3)
        self.body.columnconfigure(0, weight=1)
        self.body.rowconfigure(0, weight=1)

    def set_widgets(self):
        pass

    def display_frames(self):
        self.state_frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.header.grid(column=0, row=0, sticky=N+E+W+S)
        self.body.grid(column=0, row=1, rowspan=self.rows, sticky=N+E+W+S)

"""
class SpyOT(Frame):
    # root = Tk()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky=N + S + W + E)
        self.create_widgets()
        self.set_title(preset.title)
        self.set_geometry(preset.default_geometry)

    def create_widgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        ButtonManager(self)
        LabelManager(self)

    def set_title(self, new_title):
        self.master.title(new_title)

    def set_geometry(self, new_geometry):
        self.master.geometry(new_geometry)


class LabelManager:
    def __init__(self, frame):
        self.frame = frame
        self.create_labels()

    def create_labels(self):
        self.title_label = Label(self.frame, text=preset.title,
                                 font=(preset.default_font,
                                       preset.default_text_size,
                                       "bold"))
        self.title_label.grid(row=0, column=0, sticky=N + E + W)


class ButtonManager:
    def __init__(self, frame):
        self.frame = frame
        self.create_buttons()

    def create_buttons(self):
        # Create Profile Button
        self.create_profile_button = Button(self.frame, text="Create Profile",
                                            font=(preset.default_font,
                                                  preset.default_text_size,
                                                  "bold"),
                                            command="Hello",
                                            relief="raised")
        self.create_profile_button.grid(row=0, column=0)
        # Select Profile Button
        self.select_profile_button = Button(self.frame, text="Select Profile",
                                            font=(preset.default_font,
                                                  preset.default_text_size,
                                                  "bold"),
                                            command="Hello",
                                            relief="raised")
        self.select_profile_button.grid(row=1, column=0)

        # Quit Button
        self.quit_button = Button(self.frame, text="EXIT",
                                  font=(preset.default_font,
                                        preset.default_text_size,
                                        "bold"),
                                  command=self.frame.quit,
                                  relief="raised")
        self.quit_button.grid(row=2, column=0)

"""


def main():
    demo = SpyOT()
    demo.set_title("SpyOT Demo")
    demo.mainloop()


if __name__ == '__main__':
    main()
