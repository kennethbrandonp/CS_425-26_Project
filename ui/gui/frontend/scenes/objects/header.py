from tkinter import ttk
import constants as preset


class Header(ttk.Frame):
    def __init__(self, root_frame):
        super().__init__(master=root_frame)
        self.root = root_frame
        self.header_style = ttk.Style()
        self.header_style.configure('header.TFrame', background='grey')
        self.configure(padding=preset.padding, style='header.TFrame')

    def get_style(self):
        return self.header_style
