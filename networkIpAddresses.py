import nmap, socket

class Network(object):
    def __init__(self, ip=''):
        #These two lines grab router ip address
        #hostname = socket.gethostname()
        #ip = socket.gethostbyname(hostname)

        #However 192.168.0.1 and 192.168.1.1 are default gateways

        ip = '192.168.1.1' #I use 1.1 instead of 0.1 because no lists are displayed using 0.1
        print(ip)
        self.ip = ip

    def networkscanner(self):
        if len(self.ip) == 0:
            print("No IP address given")  #If there's no ip given
        else:
            network = self.ip + '/24'
            print("Scanning IPs") #this takes awhile.

            nm = nmap.PortScanner() #nm is used to scan the network
            nm.scan(hosts = network, arguments = '-sn')
            
            #Stores a list of every ip address on the network into host_list
            host_list = [(x, nm[x] ['status'] ['state']) for x in nm.all_hosts()]

            for host in host_list:
                print("Host\t{}".format(host))

if __name__ == "__main__":
    network = Network()
    network.networkscanner()