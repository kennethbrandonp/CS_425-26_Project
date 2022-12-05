class MainMenu:
    def __init__(self, profile_manager):
        print("Main Menu:")
        self.profileManager = profile_manager
        self.states = []

    def state_output(self):
        if self.profileManager:
            pass
        print("Options -")
        print("1: Create Profile")
        print("2: Select Profile")
        print("3: Exit Program")
        print("4: About")

    def state_input(self):
        choice = input("Input: ")
        response = self.action(choice)
        return response

    def action(self, user_choice):
        user_choice = int(user_choice)
        match user_choice:
            case 1:
                return self.create_profile()
            case 2:
                return self.select_profile()
            case 3:
                print("Goodbye!")
                return 0
            case 4:
                self.about()
                return -1
            case _:
                print("\n!Error: Input", user_choice, "is not a valid choice. Please enter")
                print("one of the options listed.\n")
                return -1

    def select_profile(self):
        print("Enter profile number to select that profile.")
        print("Enter 'cancel' to return to Main Menu.")
        self.profileManager.cli_list_profiles()
        user_input = input("Input: ")
        return -1 if user_input == 'cancel' else self.profileManager.cli_set_active(int(user_input))

    def create_profile(self):
        print("Enter profile information below.")
        print("Enter 'cancel' at any point to return to main menu.")
        response = self.profileManager.cli_new_profile()
        return response

    def about(self):
        print("""
Background: For this senior project, we attempt to tackle the beginning of a cybersecurity problem that user networks 
face when having a vast IoT environment that malicious software can manipulate and take advantage of by informing the 
user of the threats that are associated with the vulnerabilities of their network. In order to inform the user, first we 
need to identify connected IoT devices that are on a user’s network. Once those devices are detected and the data is 
compiled into a list or graph, there needs to be a simple and easy to understand way of displaying that information of 
the detected devices to the user so that the user can understand which devices are at risk of malicious software. As 
the user is informed of their at-risk devices, then the user can begin the steps towards improving their network 
security in order to prevent malicious software from attaching themselves to their network of IoT devices.

Purpose: Our project’s mission towards network security is to improve a user’s network. To improve the user’s network, a 
layer of security can be provided by supplying the user readable knowledge of their network’s vulnerabilities towards 
bad-agents that use malware and malicious software to access that user’s network. If that user is able to see their 
network, understand and utilize what information they have then the project has successfully completed its mission.

Mission: With the amount of IoT environments that are available to the non-technical public comes the great need for 
security and a way to monitor that environment. Our project will provide that peace of mind that users with 
non-technical knowledge will likely desire without taking a more expensive route for security measures on just detecting 
vulnerabilities and threats.
         
- Back-End Boys
""")
