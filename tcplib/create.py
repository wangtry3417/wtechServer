import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class createServer(object):
  def __init__(self,hostname,port,authUser=None,authPassword=None):
    self.hostname = hostname
    self.port = port
    self.authUser = authUser
    self.authPassword
    self.serverSocket = s
  def run(self):
    s.bind((self.hostname,self.port))
    s.listen(5)
    while True:
      cs,address = s.accept()
      return cs , address
  def stop(self):
    self.serverSocket.close()
