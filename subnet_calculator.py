import ipaddress 

class subnet_calculator:
    def __init__(self, network):
        self.network = network
        self.net = ipaddress.IPv4Network(network)
    
    def ip_in_net(self, ip):
        b = False
        if ipaddress.IPv4Address(ip) in self.net.hosts():
            b = True
        return b
    
    def my_net_to_another(self, network):
        b = False
        if self.net.overlaps(ipaddress.IPv4Network(network)):
            b = True
        return b
    
    def ip_to_ptr(self, ip):
        return ipaddress.ip_address(ip).reverse_pointer


ip = '192.168.1.10'
network = '192.168.1.0/24'
cal = subnet_calculator(network)
another_network = '192.168.2.0/24'
print('the network is %s: '% cal.network)
print('is ip:{0} is in range:{1}? {2}'.format(ip,network,cal.ip_in_net(ip)))
print('ptr for ip:{0} is: {1}'.format(ip, cal.ip_to_ptr(ip)))
print('is network:{0} is overlapping with network:{1}? {2}'.format(network, another_network, cal.my_net_to_another(another_network)))