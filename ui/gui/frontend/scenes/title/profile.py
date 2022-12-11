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
        self.password_entry = ttk.Entry(self.body, textvariable=self.user_password,
                                        show='*')

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

        self.displayed_profiles = []
        self.temp_profiles = []
        self.profiles = StringVar(value=self.temp_profiles)
        self.widget_states = {0: "disabled", 1: "!disabled"}
        self.set_widgets()

    def set_frames(self):
        self.scene_frame.columnconfigure(0, weight=1)
        self.scene_frame.rowconfigure(0, weight=1)
        self.scene_frame.rowconfigure(1, weight=7)

        # TODO: Make header and body into own class
        #       Will reuse in every scene except title
        #           - Method for adding rows, columns in body
        #           - Method for adding frames in body
        #           - Setting widgets will remain in base scene
        #             class, but high-level frame setting should be abstracted
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
        self.body.columnconfigure(1, weight=1)
        self.body.rowconfigure(0, weight=1)
        self.body.rowconfigure(1, weight=2)
        self.body.rowconfigure(2, weight=2)
        self.body.rowconfigure(3, weight=1)

        options_style = ttk.Style()
        options_style.configure('options.TFrame', background='white')
        self.right_body_frames = {'options': ttk.Frame(self.body), 'login': ttk.Frame(self.body)}

        for frame in self.right_body_frames:
            curr_frame = self.right_body_frames[frame]
            curr_frame.configure(padding=preset.padding,
                                 style='options.TFrame',
                                 borderwidth=5,
                                 relief='raised')
            curr_frame.columnconfigure(0, weight=1)
            curr_frame.columnconfigure(1, weight=1)
            curr_frame.rowconfigure(0, weight=1)
            curr_frame.rowconfigure(1, weight=1)
        self.right_body_frames["login"].columnconfigure(0, weight=1)
        self.right_body_frames["login"].columnconfigure(1, weight=2)
        self.right_body_frames["login"].rowconfigure(2, weight=1)
        self.right_body_frames["login"].rowconfigure(3, weight=1)

    def set_widgets(self):
        self.scene_label = ttk.Label(self.header, text="Select Profile",
                                     background='grey')
        # FIXME: Make into own class - maybe better readability so don't have
        #       to have extra functions in this class
        self.set_option_widgets()
        self.set_login_widgets()

        self.profile_listbox = Listbox(self.body, height=10,
                                       listvariable=self.profiles,
                                       justify='center')
        lbox = self.profile_listbox
        lbox.bind("<<ListboxSelect>>", lambda x: self.selection())

        self.exit_button = ttk.Button(self.body,
                                      text="Return to title screen",
                                      command=lambda: self.exit_scene())

    def set_option_widgets(self):
        option_frame = self.right_body_frames['options']
        widget_state = self.widget_states[0]
        self.edit_profile_button = ttk.Button(option_frame, text="Edit Profile",
                                              state=widget_state)
        self.delete_profile_button = ttk.Button(option_frame, text="Delete Profile",
                                                state=widget_state)

    def set_login_widgets(self):
        login_style = ttk.Style()
        login_style.configure("TLabel", background='white')
        login_frame = self.right_body_frames['login']
        widget_state = self.widget_states[0]

        self.login_label = ttk.Label(login_frame, text="Profile Login")

        self.login_user = StringVar()
        self.enter_user = ttk.Label(login_frame, text="Enter Username",
                                    style='guide.TLabel')
        self.user_entry = ttk.Entry(login_frame, textvariable=self.login_user,
                                    state=widget_state)

        self.pass_user = StringVar()
        self.enter_password = ttk.Label(login_frame, text="Enter Password",
                                        style='guide.TLabel')
        self.password_entry = ttk.Entry(login_frame, textvariable=self.pass_user,
                                        show="*", state=widget_state)

        self.submit = ttk.Button(login_frame, text="Login", state=widget_state)

    def update_profiles(self):
        """
        backend call to generate list of saved profiles
        """

        # TODO: Change to a proper backend call
        db_path = "backend/tempdb.txt"
        with open(db_path) as profile_file:
            profiles = profile_file.readlines()
        for profile in profiles:
            profile = profile.strip('\n').split(',')
            if profile[0] not in self.temp_profiles:
                self.temp_profiles.append(profile[0])
        self.profiles.set(self.temp_profiles)

    def update_scene(self):
        self.update_profiles()

    def display_content(self):
        self.update_scene()
        self.display_frames()
        self.display_widgets()

    def display_frames(self):
        self.scene_frame.grid(column=0, row=0, sticky=N + E + S + W)
        self.header.grid(column=0, row=0, sticky=N + E + S + W)
        self.body.grid(column=0, row=1, sticky=N + E + S + W)
        r_body = self.right_body_frames
        r_body['options'].grid(column=1, row=1, sticky=N + E + S + W)
        r_body['login'].grid(column=1, row=2, sticky=N + E + S + W)

    def display_widgets(self):
        self.scene_label.grid(column=0, row=0)

        # Left Body
        self.profile_listbox.grid(column=0, row=1, rowspan=2, sticky=N+S)
        # Right Body
        self.display_options()
        self.display_login()

        self.exit_button.grid(column=0, row=3, columnspan=2)

    def display_options(self):
        self.edit_profile_button.grid(column=0, row=0, columnspan=2, sticky=E + W)
        self.delete_profile_button.grid(column=0, row=1, columnspan=2, sticky=E + W)

    def display_login(self):
        self.login_label.grid(column=0, row=0, columnspan=2)

        self.enter_user.grid(column=0, row=1)
        self.user_entry.grid(column=1, row=1, sticky=E+W)

        self.enter_password.grid(column=0, row=2)
        self.password_entry.grid(column=1, row=2, sticky=E+W)

        self.submit.grid(column=0, columnspan=2, row=3)

    def selection(self):
        self.toggle_profile_widgets(1)

    def toggle_profile_widgets(self, state):
        widget_state = self.widget_states[state]
        self.edit_profile_button.configure(state=widget_state)
        self.delete_profile_button.configure(state=widget_state)
        self.password_entry.configure(state=widget_state)
        self.user_entry.configure(state=widget_state)
        self.submit.configure(state=widget_state)

    def exit_scene(self):
        self.reset_widgets()
        self.base.change_scene("title")

    def reset_widgets(self):
        if self.profile_listbox.curselection():
            self.profile_listbox.select_clear(self.profile_listbox.curselection()[0])
        self.toggle_profile_widgets(0)

    def remove_content(self):
        self.scene_frame.grid_remove()
