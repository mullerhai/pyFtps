
from ftpLogin import client
from beehive import muHive

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 4200
  username = 'zhuzheng'
  auth = 'LDAP'
  password = "abc123."
  database = 'fkdb'
  table = 'tab_client_label'
  paramDict = {'client_nmbr': 'AA75', 'batch': 'p1'}

  filedlist = ['gid', 'realname', 'card']
  mu = muHive(host, username, password, port)
  conn = mu.connhive(database, auth)
  cursor = conn.cursor()
  limit = 1000
  df2 = mu.query_selectFileds_Dataframe(conn, table, filedlist, paramDict, 1000)
  print(df2.shape)
  print(df2.head())
  print(df2.columns())

def helloftp():
  host = 'ftps.baidu.com'
  port = '21'
  user = 'zh****eng'
  pwd = 'zz****mt.2'
  ip = '117.35.45.150'

  cli=client(host,user,pwd)
  fs= cli.login(2,True)

 # path='haining'
  #cli.ftplistDir(fs,path)


  # server_path='haining/upload/'
  # downlaod_Severfile='AA62p1_yl_v2.3_20180410.rar'
  # new_localfil='AA62p1_yl_20180410.rar'
  # cli.ftpDownloadSeverFile(fs,server_path,downlaod_Severfile,new_localfil)
  #

  upfile='/Users/geo/Downloads/AA62p1_yl_v2.3_20180410.rar'
  sever_path='upload/'
  new_severname='AA62p1_yl_20180410.rar'
  cli.ftpUploadLocalFile(fs,upfile,sever_path,new_severname)

  fs.quit()