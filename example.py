
from ftpLogin import client

if __name__ == '__main__':
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