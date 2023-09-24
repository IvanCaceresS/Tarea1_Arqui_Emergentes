from mininet.topo import Topo

class CustomTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Crear los switches
        switch1 = self.addSwitch('switch1')
        switch2 = self.addSwitch('switch2')
        switch3 = self.addSwitch('switch3')
        switch4 = self.addSwitch('switch4')

        # Conectar hosts a switches
        host1 = self.addHost('host1')
        host2 = self.addHost('host2')

        self.addLink(host1, switch1)
        self.addLink(host2, switch4)

        # Conectar los switches con las especificaciones dadas
        self.addLink(switch1, switch2, bw=250, delay='150ms', loss=5)
        self.addLink(switch2, switch3, bw=100, delay='70ms', loss=4)
        self.addLink(switch3, switch4, bw=150, delay='200ms', loss=3)

# Crear una instancia de la topología y asignarle un nombre
topos = {'mytopo': CustomTopo}
