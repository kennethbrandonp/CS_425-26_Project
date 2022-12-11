from backend.networks import NetworkManager
from backend.profiles import ProfileManager
from networkIpAddresses import Network

class ModelManager:
    def __init__(self):
        self.profiles = ProfileManager()
        self.network = Network()

    def scan_network(self):
        self.network.networkScanner()

    def get_devices(self):
        return self.network.device_list