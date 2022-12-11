import constants as preset
from tkinter import *
from tkinter import ttk
from frontend.scenes.objects.header import Header
from frontend.scenes.objects.body import Body

class Scene:
    def __init__(self, parent, root_frame):
        self.parent = parent
        self.root = root_frame

        self.scene_frame = ttk.Frame(self.root, padding=preset.padding)
        self.set_scene_frame()

        self.header = Header(self.scene_frame)
        self.body = Body(self.scene_frame)

    def set_scene_frame(self):
        self.scene_frame.columnconfigure(0, weight=1)
        self.scene_frame.rowconfigure(0, weight=1)
        self.scene_frame.rowconfigure(1, weight=7)

    def remove_content(self):
        self.scene_frame.grid_remove()

    def display_frames(self):
        self.scene_frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.header.grid(column=0, row=0, sticky=N + E + S + W)
        self.body.grid(column=0, row=1, sticky=N + E + S + W)

    def display_widgets(self):
        pass

    def display_content(self):
        self.update_content()
        self.display_frames()
        self.display_widgets()

    def update_content(self):
        pass