import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class createServer(object):
  def __init__(self,hostname,port,authUser=None,authPassword=None):
    self.hostname = hostname
    self.port = port
    self.authUser = authUser
    self.authPassword = authPassword
    self.serverSocket = s
  def run(self):
    s.bind((self.hostname,self.port))
    s.listen(5)
    while True:
      if self.authUser == None and self.authPassword == None:
        cs,address = s.accept()
        return cs , address
      else:
        cs,address = s.accept()
        user = cs.recv(1024).decode("utf-8")
        pw = cs.recv(1024).decode("utf-8")
        u = user.split(" ")
        p = pw.split(" ")
        if u[0] == "AUTH-USER" and p[0] == "AUTH-PW":
          if u[1] == self.authUser and p[1] == self.authPassword:
            print("ok")
          else:
            print("Cannot assign the user detail")
        else:
          print("Not the wtps format")
  def stop(self):
    self.serverSocket.close()
  def send(self,things : bytes):
    self.serverSocket.send(things)
