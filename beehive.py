from pyhive import hive
import  numpy as  np
import pandas as  pd


class muHive:

  def __init__(self,host,user,pwd,port=10000,database='fkdb',auth='LDAP'):
    self.host=host
    self.user=user
    self.pwd=pwd
    self.port=port
    self.database=database
    self.auth=auth

  def connhive(self,database='fkdb',auth='LDAP'):
    conn = hive.Connection(host=self.host, port=self.port, username=self.user, auth=self.auth, password=self.pwd,
      database=self.database)
    print('connect sucessfully')
    return conn

  def query_AllFileds_Dataframe(self,conn,table,param_dict,limit=None):
    base_table = self.database + '.' + table
    query_part='select * from %s where '%base_table
    params = []
    for key, value in param_dict.items():
      params.append(' '+key + '= \'%s\' ' % value + 'and')
    paramstemp = ''.join(params)
    params = paramstemp[:-3]
    if limit==None:
      hsql = query_part + params
    else:
      hsql=query_part+params+' limit %d'%limit
    print(hsql)
    # cursor=conn.cursor()
    # cursor.execute(hsql)
    # dataframe=pd.DataFrame(cursor.fetchall())
    dataframe = pd.read_sql(hsql, conn)
    return dataframe

  def query_selectFileds_Dataframe(self,conn,table,filed_list,param_dict,limit=None):
    base_table = self.database + '.' + table
    fileds=','.join(filed_list)
    query_part='select %s  from %s where '%(fileds,base_table)
    params = []
    for key, value in param_dict.items():
      params.append(' '+key + '= \'%s\' ' % value + 'and')
    paramstemp = ''.join(params)
    params = paramstemp[:-3]
    if limit==None:
      hsql = query_part + params
    else:
      hsql=query_part+params+ ' limit %d'%limit
    print(hsql)
    cursor = conn.cursor()
    cursor.execute(hsql)
    dataframe=pd.DataFrame(cursor.fetchall())
  #  dataframe=pd.read_sql(hsql,conn)
    return dataframe



  def drop_partition(self,cursor,table,partition_param):
    base_table=self.database+'.'+table
    hsql_part='alter table %s drop if  exists  partition ( '%base_table
    params=[]
    for key, value in partition_param.items():
      params.append(key+'= \'%s\''%value+',')
    paramstemp=''.join(params)
    params=paramstemp[:-1]
    hsql=hsql_part+params+');'
    print(hsql)
    cursor.excute(hsql)


if __name__ == '__main__':
    host='127.0.0.1'
    port=4200
    username='zhuzheng'
    auth='LDAP'
    password="abc123."
    database='fkdb'
    table='tab_client_label'
    paramDict={'client_nmbr':'AA75','batch':'p1'}

    filedlist=['gid','realname','card']
    mu=muHive(host,username,password,port)
    conn=mu.connhive(database,auth)
    cursor=conn.cursor()
    limit=1000
    df2=mu.query_selectFileds_Dataframe(conn,table,filedlist,paramDict,1000)
    print(df2.shape)
    print(df2.head())
    print(df2.columns())

    # df=mu.query_AllFileds_Dataframe(conn,table,paramDict,limit)
    #
    # print(df.shape)
    # print(df.head())
    # print(df.columns())

    df2=mu.query_selectFileds_Dataframe(conn,table,filedlist,paramDict,1000)
    print(df2.shape)
    print(df2.head())
    print(df2.columns())
   # mu.drop_partition(cursor,table,paramDict)

