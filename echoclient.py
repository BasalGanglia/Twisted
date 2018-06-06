from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("test".encode('utf-8'))
        
    def dataReceived(self, data):
        print("Served said:{0}".format(data))
        
class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed")
        reactor.stop()
        
    def clientConnectionLost(self, connector, reason):
        print("Connection Lost")
        
reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()