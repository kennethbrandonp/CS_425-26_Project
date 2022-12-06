from tkinter import *
from tkinter import ttk
import constants as preset
import time


class SpyOT:
    def __init__(self):
        self.root = Tk()
        self.configure_root()

        self.frames = {
            "titleScreen": Title(self.root),
            "mainMenu": ttk.Frame(self.root, padding="3"),
            "createProfile": ttk.Frame(self.root, padding="3")
        }
        self.current_frame = self.frames["titleScreen"]

    def mainloop(self):
        self.current_frame.display_frame()
        self.root.mainloop()

    def set_title(self, new_title):
        self.root.title(new_title)

    def configure_root(self):
        self.root.geometry(preset.default_geometry)
        self.root.title(preset.title)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)


class Title:
    def __init__(self, root):
        self.root = root
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
        self.frame.grid(column=0, row=0, sticky=N+E+S+W)
        self.display_widgets()

    def remove_frame(self):
        self.frame.grid_remove()

    def display_widgets(self):
        self.label.grid(column=1, row=0)
        for i, button in enumerate(self.buttons):
            button.grid(column=1, row=i+1)

    def set_widgets(self):
        self.label = ttk.Label(self.frame, text=self.root.title(),
                               borderwidth=5, relief="raised")

        self.buttons.append(ttk.Button(self.frame, text="Create Profile",
                                       state="!disabled", command=self.remove_frame))
        self.buttons.append(ttk.Button(self.frame, text="Select Profile", state="disabled"))
        self.buttons.append(ttk.Button(self.frame, text="Exit",
                                       state="!disabled", command=self.root.quit))

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
