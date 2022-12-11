import random

random.seed()


class Profile:
    def __init__(self, name, network, password):
        self.name = name
        self.network = network
        self.password = password

        self.user_id = None
        self.network_id = None

        self.generate_ids()

    def generate_ids(self):
        self.user_id = random.randint(1, 100)
        self.network_id = random.randint(1, 100)


class ProfileManager:
    def __init__(self):
        pass

    def add_profile(self):
        pass

    def edit_profile(self):
        pass

    def delete_profile(self):
        pass
