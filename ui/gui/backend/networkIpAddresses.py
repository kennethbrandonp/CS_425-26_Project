import nmap, socket
import sys
import socket
from datetime import datetime


class Network(object):
    def __init__(self, ip=''):
        # These two lines grab router ip address
        # hostname = socket.gethostname()
        # ip = socket.gethostbyname(hostname)

        # However 192.168.0.1 and 192.168.1.1 are default gateways

        ip = '192.168.1.1'
        self.ip = ip
        self.host_list_size = None
        self.host_list = None
        self.ip_list = []
        self.device_list = {"devices": []}

    def networkCheck(self):
        if (self.host_list_size == 0):
            if (self.ip == '192.168.1.1'):
                self.ip = '192.168.1.0'
                self.networkPatch()

            elif (self.ip == '192.168.1.0'):
                self.ip = '192.168.1.1'
                self.networkPatch()

    def networkPatch(self):
        network = self.ip + '/24'
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        self.host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    def networkCounter(self):
        self.host_list_size = len(self.host_list)  # Counts the amount of connected devices in a network.

    def networkScanner(self):
        if len(self.ip) == 0:
            print("No IP address given")  # If there's no ip given

        else:
            network = self.ip + '/24'
            print("Scanning IPs")  # this takes awhile.

            nm = nmap.PortScanner()  # nm is used to scan the network
            nm.scan(hosts=network, arguments='-sn')

            # Stores a list of every ip address on the network into host_list
            self.host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

            self.networkCounter()

            self.networkCheck()

            for host, up in self.host_list:
                if (host == self.ip):
                    self.device_list["host"] = socket.gethostbyaddr(host)
                    print("\n List of connected devices:  ")
                    print("_______________________________")
                else:
                    try:
                        print(socket.gethostbyaddr(host))
                        self.device_list["devices"].append(socket.gethostbyaddr(host))
                    except:
                        print("!Error.")
            # grabs ip addresses from host_list and adds to its list
            for i in self.host_list:
                self.ip_list.append(i[0])

    def P_Scanner(self):
        try:
            target = self.ip_list.copy()
            # Iterate through each ip address and return open ports
            for x in range(len(target)):
                print("-" * 50)
                print("Scanning Target: " + str(target[x]))
                print("Scanning started at:" + str(datetime.now()))
                for port in range(1, 5):  # Change number of sockets that will be scanned
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)

                    # returns an error indicator
                    result = s.connect_ex((str(target[x]), port))
                    if result == 0:
                        print("Port {} is open".format(port))  # print port number that is open
                    s.close()  # close port once done and iterate through to next ip address
                print("-" * 50)
        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()


if __name__ == "__main__":
    network = Network()
    IP_addresses = network.networkScanner()
    network.P_Scanner()