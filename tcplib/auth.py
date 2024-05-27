from .create import s , createServer

def auth_login(host : str,port : int,username : str, password : str):
  #testSer = createServer(hostname=host,port=port,authUser=username,authPassword=password)
  s.connect((host,port))
  userFormat = f"AUTH-USER {username}"
  pwFormat = f"AUTH-PW {password}"
  s.send(userFormat.encode("utf-8"))
  s.send(userFormat.encode("utf-8"))
  return s.recv(1024)
