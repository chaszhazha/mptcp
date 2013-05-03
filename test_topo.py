from mininet.topo import Topo

class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('s1')
        rightSwitch = self.addSwitch('s2')

        self.addLink(leftHost,leftSwitch, bw=100)
        self.addLink(leftSwitch, rightSwitch, bw=100)
        self.addLink(rightHost, rightSwitch, bw=100)

topos = {'testTopo': (lambda :TestTopo() )}
