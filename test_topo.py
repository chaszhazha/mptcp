from mininet.topo import Topo

class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftswitch = self.addSwitch('s1')
        rightswithc = self.addSwitch('s2')

        self.addLink(leftHost,leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightHost, rightSwitch)

topos = {'testTopo': (lambda :TestTopo() )}