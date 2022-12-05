from states.mainmenu import MainMenu
from systems.profilemanager import ProfileManager


class SpyOT:
    def __init__(self):
        print("Welcome to SpyOT! The IoT Network Manager.")
        self.profile_manager = ProfileManager()

        self.systems = {"profiles": self.profile_manager,
                        "networks": None,
                        "security": None}

        self.curr_state = MainMenu(self.systems["profiles"])

    def mainloop(self):
        while True:
            if not self.main_menu():
                break
            print("Hello", self.profile_manager.active_profile.properties["username"])
            break

    def main_menu(self):
        state_response = -1
        while not self.profile_manager.active_profile:
            self.curr_state.state_output()
            state_response = self.curr_state.state_input()
            # Responses:
            #  0 - Program Exit
            # -1 - Cancelled action, remain in main menu
            #  1 - Profile successfully set, exit main menu
            if state_response == 0:
                return 0
        return state_response


def main():
    root = SpyOT()
    root.mainloop()


if __name__ == '__main__':
    main()
