from tkinter import *
from tkinter import ttk
from frontend.scenes.objects.scene import Scene

class TitleScreen(Scene):
    def __init__(self, parent, root_frame):
        super().__init__(parent, root_frame)
        self.parent = parent
        self.root = root_frame
