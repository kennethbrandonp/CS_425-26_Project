import nmap, socket

class Network(object):
    def __init__(self, ip=''):
        #These two lines grab router ip address
        #hostname = socket.gethostname()
        #ip = socket.gethostbyname(hostname)

        #However 192.168.0.1 and 192.168.1.1 are default gateways

        ip = '192.168.1.1' 
        self.ip = ip
        self.host_list_size = None

    def networkCheck(self):
        if(self.host_list_size == 0):
            if (self.ip == '192.168.1.1'):
                self.ip = '192.168.1.0'

            elif(self.ip == '192.168.1.0'):
                self.ip = '192.168.1.1'

    def networkCounter(self, host):
        self.host_list_size = len(host) #Counts the amount of connected devices in a network.

    def networkScanner(self):
        if len(self.ip) == 0:
            print("No IP address given")  #If there's no ip given

        else:
            network = self.ip + '/24'
            print("Scanning IPs") #this takes awhile.

            nm = nmap.PortScanner() #nm is used to scan the network
            nm.scan(hosts = network, arguments = '-sn')
            
            #Stores a list of every ip address on the network into host_list
            host_list = [(x, nm[x] ['status'] ['state']) for x in nm.all_hosts()]

            self.networkCounter(host_list)

            self.networkCheck()

            for host, up in host_list:
                if(host == self.ip):
                    print("\n List of connected devices:  ")
                    print("_______________________________")
                else:
                    print(host)

if __name__ == "__main__":
    network = Network()
    network.networkScanner()