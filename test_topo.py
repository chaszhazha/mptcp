from time import sleep, time
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import CPULimitedHost

class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addHost('h3')
        rightSwitch = self.addHost('h4')
        
        leftSwitch.cmd('sysctl -w net.ipv4.ip_forward=1')
        rightSwitch.cmd('sysctl -w net.ipv4.ip_forward=1')

        link1 = self.addLink(leftHost,leftSwitch)
        link2 = self.addLink(leftSwitch, rightSwitch)
        link3 = self.addLink(rightHost, rightSwitch)
        print dir(link1)

topos = {'testTopo': (lambda :TestTopo() )}

if __name__ == '__main__':
    net = Mininet(topo = TestTopo())
    net.start()

    sleep(5)

    net.stop()
