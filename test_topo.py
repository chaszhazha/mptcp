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
        leftSwitch = self.addSwitch('s1')
        rightSwitch = self.addSwitch('s2')
        

        link1 = self.addLink(leftHost,leftSwitch)
        link2 = self.addLink(leftSwitch, rightSwitch)
        link3 = self.addLink(rightHost, rightSwitch)
        print dir(link1)

topos = {'testTopo': (lambda :TestTopo() )}

if __name__ == '__main__':
    net = Mininet(topo = TestTopo())
    net.start()
    s1 = net.getNodeById('s1')
    s2 = net.getNodeById('s2')
    print net.hosts
    sleep(5)

    net.stop()
