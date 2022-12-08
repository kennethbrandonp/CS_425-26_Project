from tkinter import *
from tkinter import ttk
from ui.gui.frontend.scenes.title.profile import *


class TitleScreen:
    def __init__(self, base):
        self.base = base
        self.root = self.base.root

        style = ttk.Style()
        style.theme_use('vista')
        self.scene_frame = ttk.Frame(self.root,
                                     padding=(3, 3, 12, 12))
        self.set_frames()
        self.set_widgets()

        self.current_scene = self
        self.scenes = {
            "title": self,
            "createprofile": CreateProfile(self),
            "selectprofile": SelectProfile(),
            "settings": None
        }

    def display_content(self):
        self.current_scene.display_frames()
        self.current_scene.display_widgets()

    def remove_content(self):
        self.scene_frame.grid_remove()

    def change_scene(self, new_scene):
        self.current_scene.remove_content()
        self.current_scene = new_scene

    def display_frames(self):
        self.scene_frame.grid(column=0, row=0, sticky=N + E + S + W)

    def display_widgets(self):
        self.title_label.grid(column=0, row=0)
        self.create_profile_button.grid(column=0, row=1)
        self.select_profile_button.grid(column=0, row=2)
        self.settings_button.grid(column=0, row=3)
        self.exit_button.grid(column=0, row=4)

    def set_frames(self):
        self.scene_frame.columnconfigure(0, weight=1)
        self.scene_frame.rowconfigure(0, weight=1)  # Program Title
        self.scene_frame.rowconfigure(1, weight=2)  # Button 1
        self.scene_frame.rowconfigure(2, weight=2)  # Button 2
        self.scene_frame.rowconfigure(3, weight=2)  # Button 3
        self.scene_frame.rowconfigure(4, weight=2)  # Button 4

    def set_widgets(self):
        self.title_label = ttk.Label(self.scene_frame,
                                     text=self.root.title())

        self.create_profile_button = ttk.Button(self.scene_frame,
                                                text="Create Profile")

        self.select_profile_button = ttk.Button(self.scene_frame,
                                                text="Select Profile")

        self.settings_button = ttk.Button(self.scene_frame,
                                          text="Settings",)

        self.exit_button = ttk.Button(self.scene_frame,
                                      text="Exit Program",
                                      command=self.root.quit)
