import constants as preset
from tkinter import *
from tkinter import ttk


class Settings:
    """
    Resolution -
    Font: Size, Style, Theme
    Color: Dark mode
    """

    def __init__(self, base):
        self.base = base
        self.root = self.base.root
        self.scene_frame = ttk.Frame(self.root,
                                     padding=preset.padding)
        self.set_frames()
        self.set_widgets()

    def set_frames(self):
        self.scene_frame.columnconfigure(0, weight=1)
        self.scene_frame.rowconfigure(0, weight=1)
        self.scene_frame.rowconfigure(1, weight=7)

        header_style = ttk.Style()
        header_style.configure('header.TFrame', background='grey')
        self.header = ttk.Frame(self.scene_frame,
                                padding=preset.padding,
                                style='header.TFrame')
        self.header.rowconfigure(0, weight=1)
        self.header.columnconfigure(0, weight=1)

        body_style = ttk.Style()
        body_style.configure('body.TFrame')
        self.body = ttk.Frame(self.scene_frame,
                              padding=preset.padding,
                              style='body.TFrame')
        self.rows = 20
        self.body.columnconfigure(0, weight=1)
        self.body.columnconfigure(1, weight=1)
        for i in range(self.rows + 1):
            self.body.rowconfigure(i, weight=1)

    def set_widgets(self):
        self.scene_label = ttk.Label(self.header, text="Settings",
                                     background='grey')
        self.set_left_widgets()
        self.set_right_widgets()

    def set_left_widgets(self):
        r = IntVar()
        self.res_label = ttk.Label(self.body, text = "Resolution")
        self.rad_1 = ttk.Radiobutton(self.body, text="800x600", variable=r, value=1, command=lambda:self.clicked(r.get()))
        self.rad_2 = ttk.Radiobutton(self.body, text="1366x768", variable=r, value=2)
        self.rad_3 = ttk.Radiobutton(self.body, text="1920x1080", variable=r, value=3)
        t = IntVar()
        self.style_label = ttk.Label(self.body, text = "Font Styles")
        self.rad_4 = ttk.Radiobutton(self.body, text="Helvetica", variable=t, value=1)
        self.rad_5 = ttk.Radiobutton(self.body, text="Oswald", variable=t, value=2)
        s = IntVar()
        self.size_label = ttk.Label(self.body, text = "Font Sizes")
        self.rad_6 = ttk.Radiobutton(self.body, text="Small", variable=s, value=1)
        self.rad_7 = ttk.Radiobutton(self.body, text="Medium", variable=s, value=2)
        self.rad_8 = ttk.Radiobutton(self.body, text="Large", variable=s, value=3)

        self.submit_profile = ttk.Button(self.body, text="Finish",
                                         command=lambda: self.exit_scene())

    def clicked(self, value):
        pass


    def set_right_widgets(self):
        pass

    def display_content(self):
        self.display_frames()
        self.display_widgets()

    def display_frames(self):
        self.scene_frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.header.grid(column=0, row=0, sticky=N + E + S + W)
        self.body.grid(column=0, row=1, sticky=N + E + S + W)

    def display_widgets(self):
        self.scene_label.grid(column=0, row=0)
        self.display_left_widgets()
        self.display_right_widgets()

    def display_left_widgets(self):
        self.res_label.grid(column=0, row=0, sticky=N + W)
        self.rad_1.grid(column=0, row=1, sticky=N + W)
        self.rad_2.grid(column=0, row=2, sticky=N + W)
        self.rad_3.grid(column=0, row=3, sticky=N + W)

        self.style_label.grid(column=0, row=5, sticky=N + W)
        self.rad_4.grid(column=0, row=6, sticky=N + W)
        self.rad_5.grid(column=0, row=7, sticky=N + W)

        self.size_label.grid(column=0, row=9, sticky=N + W)
        self.rad_6.grid(column=0, row=10, sticky=N + W)
        self.rad_7.grid(column=0, row=11, sticky=N + W)
        self.rad_8.grid(column=0, row=12, sticky=N + W)
        self.submit_profile.grid(column=0, row=18, sticky=N + W)
    def display_right_widgets(self):
        pass