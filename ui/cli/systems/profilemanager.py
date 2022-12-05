class Profile:
    def __init__(self):
        self.username = None
        self.password = None
        self.properties = {
            "username": None,
            "network name": None,
            "password": None,
        }
        self.sensitive = ["password", "user_ID"]

    def cli_display_profile(self):
        for entry in self.properties:
            if entry not in self.sensitive:
                print(entry, ": ", self.properties[entry])


class ProfileManager:
    def __init__(self):
        self.active_profile = None
        self.profiles = []

    def is_empty(self):
        # Returns if a profile exists in database or not
        pass

    def cli_list_profiles(self):
        print("Profiles")
        for i, profile in enumerate(self.profiles):
            print(i, ":")
            profile.cli_display_profile()

    def cli_new_profile(self):
        self.profiles.insert(-1, Profile())
        temp_profile = self.profiles[-1]
        for field in temp_profile.properties:
            user_input = input(field + ": ")
            if user_input == 'cancel':
                self.profiles.pop()
                return -1
            temp_profile.properties[field] = user_input
        return 1

    def cli_set_active(self, index: int):
        try:
            self.active_profile = self.profiles[index]
            return 1
        except IndexError as _:
            print("!Error: Profile at index", index, "does not exist!")
            return -1
