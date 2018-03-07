#/usr/bin/python
# _*_ coding:UTF-8 _*_

from twisted.internet import protocol,reactor
from time import ctime

PORT=21570

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt=self.Clnt=self.transport.getPeer().host
        print '...connected from:',clnt
    def dataReceived(self,data):
        clnt=self.Clnt=self.transport.getPeer().host
        print '...received data, from:%s,data:%s' % (clnt,data)
        self.transport.write('[%s] %s' %(ctime(),data))

factory=protocol.Factory()
factory.protocol=TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT,factory)
reactor.run()