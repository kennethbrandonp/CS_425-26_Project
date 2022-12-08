import constants as preset
from tkinter import *
from tkinter import ttk


class CreateProfile:
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
        self.rows = 4
        self.body.columnconfigure(0, weight=1)
        self.body.columnconfigure(1, weight=1)
        for i in range(self.rows + 1):
            self.body.rowconfigure(i, weight=1)

    def set_widgets(self):
        self.scene_label = ttk.Label(self.header, text="Create Profile",
                                     background='grey')
        self.set_left_widgets()
        self.set_right_widgets()

    def set_left_widgets(self):
        self.name_label = ttk.Label(self.body, text="Enter Profile Name")
        self.user_name = StringVar()
        self.name_entry = ttk.Entry(self.body, textvariable=self.user_name)

        self.network_label = ttk.Label(self.body, text="Enter Network Alias")
        self.network_alias = StringVar()
        self.network_entry = ttk.Entry(self.body, textvariable=self.network_alias)

        self.password_label = ttk.Label(self.body, text="Enter Profile Password")
        self.user_password = StringVar()
        self.password_entry = ttk.Entry(self.body, textvariable=self.user_password)

        self.submit_profile = ttk.Button(self.body, text="Finish",
                                         command=lambda: self.exit_scene())

    def set_right_widgets(self):
        self.configure_label = ttk.Label(self.body,
                                         text="Network Configuration")
        self.configure_button = ttk.Button(self.body,
                                           text="Run Automatic Configuration",
                                           command=None)

        """
        Call back-end to:
            1. scan network
            2. process contents
            3. identify metadata and devices
            4. summarize data
            5. return a dict
                {network_ip: value, devices:[device0, device1, ...]}
        """
        network_found = StringVar(value="TEST_NETWORK")
        self.found_label = ttk.Label(self.body, text="Detected Network:")
        self.network_name = ttk.Label(self.body,
                                      text=network_found.get())
        self.device_tree = ttk.Treeview(self.body,
                                        columns=("IP", "Security"))
        self.device_tree.column('#0', width=35)
        for data in self.device_tree['columns']:
            self.device_tree.column(data, width=55)
        self.device_tree.insert('', 'end', text='device0', values=('000.000.000.000', 'WK4P'))
        self.exit_button = ttk.Button(self.body,
                                      text="Return to title screen",
                                      command=lambda: self.exit_scene(True))

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
        self.name_label.grid(column=0, row=0, sticky=N)
        self.name_entry.grid(column=0, row=0, sticky=E + W)
        self.network_label.grid(column=0, row=1, sticky=N)
        self.network_entry.grid(column=0, row=1, sticky=E + W)
        self.password_label.grid(column=0, row=2, sticky=N)
        self.password_entry.grid(column=0, row=2, sticky=E + W)
        self.submit_profile.grid(column=0, row=4)

    def display_right_widgets(self):
        self.configure_label.grid(column=1, row=0, sticky=N)
        self.configure_button.grid(column=1, row=0, sticky=E + W)
        self.found_label.grid(column=1, row=1, sticky=W)
        self.network_name.grid(column=1, row=1)
        # TODO: Fix table headers not showing up
        self.device_tree.grid(column=1, row=2, rowspan=2, sticky=N + E + W)
        self.exit_button.grid(column=1, row=4)

    def remove_content(self):
        self.scene_frame.grid_remove()

    def exit_scene(self, is_exit=False):
        if is_exit:
            self.base.change_scene("title")
            return
        # run checks on values
        success = self.verify_entries()
        if success:
            self.set_profile()
            # TODO: Create a home page with user info
            #       Update SelectProfile class to include new profile
            self.base.change_scene("title")
        else:
            # Indicate errors
            pass

    def verify_entries(self):
        name = self.user_name.get()
        alias = self.network_alias.get()
        password = self.user_password.get()
        if not name or not alias or not password:
            return False
        if name:
            pass
        if alias:
            pass
        if password:
            pass
        return True

    def set_profile(self):
        database_path = "backend/tempdb.txt"
        database = open(database_path, 'a')
        database.write(self.user_name.get() + ',')
        database.write(self.network_alias.get() + ',')
        database.write(self.user_password.get())
        database.write('\n')
        database.close()


class SelectProfile:
    def __init__(self, base):
        self.base = base
        self.root = base.root

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
        self.body.columnconfigure(0, weight=1)
        self.body.rowconfigure(0, weight=1)

    def set_widgets(self):
        self.scene_label = ttk.Label(self.header, text="Select Profile",
                                     background='grey')
        self.exit_button = ttk.Button(self.body,
                                      text="Return to title screen",
                                      command=lambda: self.exit_scene())

    def display_content(self):
        self.display_frames()
        self.display_widgets()

    def display_frames(self):
        self.scene_frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.header.grid(column=0, row=0, sticky=N + E + S + W)
        self.body.grid(column=0, row=1, sticky=N + E + S + W)

    def display_widgets(self):
        self.scene_label.grid(column=0, row=0)
        self.exit_button.grid(column=0, row=0)

    def exit_scene(self):
        self.base.change_scene("title")

    def remove_content(self):
        self.scene_frame.grid_remove()
