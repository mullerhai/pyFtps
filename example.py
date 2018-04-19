
from ftpLogin import client

if __name__ == '__main__':
  host = 'ftps.baidu.com'
  port = 221
  user = 'zh****ng'
  pwd = 'zz****mt.2'
  ip = '117.24.135.150'

  cli=client(host,user,pwd)
  fs= cli.login(2,True)
  path='haining'
  cli.ftplistDir(fs,path)