from tkinter import ttk
import constants as preset


class Body(ttk.Frame):
    def __init__(self, root_frame):
        super().__init__(master=root_frame)
        body_style = ttk.Style()
        body_style.configure('body.TFrame')
        self.configure(padding=preset.padding, style='body.TFrame')
