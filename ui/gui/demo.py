from tkinter import *
import constants as preset


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
        self.title_label = Label(self.frame, text="SpyOT",
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

def main():
    demo = SpyOT()
    demo.set_title("SpyOT Demo")
    demo.mainloop()


if __name__ == '__main__':
    main()
