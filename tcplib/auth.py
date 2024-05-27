from .create import s , createServer

def auth_user(host : str,port : int,username : str, password : str):
  testSer = createServer(hostname=s.gethostname(),port="5090",authUser=username,authPassword=password)
