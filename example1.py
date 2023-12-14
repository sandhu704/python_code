from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def customTopology():
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController('c0',controller=Controller,ip='0.0.0.0',port=6633)

    # Add switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    # Add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')

    # Add links (bidirectional by default)
    net.addLink(s1, s2)
    net.addLink(s1, s4)
    net.addLink(s2, s3)
    net.addLink(s2, s5)
    net.addLink(s3, s4)
    net.addLink(s3, s5)
    net.addLink(s4, h1)
    net.addLink(s4, h2)
    net.addLink(s3, h3)
    net.addLink(s3, h4)
    net.addLink(s5, h5)
    net.addLink(s5, h6)

    # Start the network
    net.start()

    # Run CLI
    CLI(net)

    # After the user exits the CLI, stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
