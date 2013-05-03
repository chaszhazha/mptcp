from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import CPULimitedHost

class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('h3')
        rightSwitch = self.addSwitch('h4')

        self.addLink(leftHost,leftSwitch, bw=100)
        self.addLink(leftSwitch, rightSwitch, bw=100)
        self.addLink(rightHost, rightSwitch, bw=100)

topos = {'testTopo': (lambda :TestTopo() )}
