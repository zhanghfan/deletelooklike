# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: zf
"""

import mysql.connector  #导入mysql包
 
mydb = mysql.connector.connect(
  host="127.0.0.1",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="root",   # 数据库密码
  database="test"# 数据库名
)
 
# print(mydb)
for m in range(1,73): # m为计数器，有多少行数据后面的数+1
    p = "SELECT C3 FROM test12 WHERE C1 = "+str(m) #为拼接sql语句，取出关键词数据sql语句
    print(p)
    mycursor = mydb.cursor() # 初始化数据库游标
    mycursor.execute(p)      #执行sql语句，完成关键词数据提取
    i = mycursor.fetchone() # 取得数据库返回结果，数据库输出传回python
    j = ""+i[0]   #拼接sql语句
    h = "%".join(j)
    k = "%"+h+"%"   #把关键词用%隔开
    print(k)
    x = "\""+k+"\""
    g = "SELECT count(*) FROM test12 where C2 like "+x #求得和C3相似的C2总数
    print(g)
 #  mycursor = mydb.cursor()
    mycursor.execute(g)
    d = mycursor.fetchone()  
    print(d)
    b = d[0]
    print(b)
    a = "UPDATE test12 SET C4 = "+str(b)+" WHERE C1 = "+str(m)
    print(a)
    mycursor.execute(a) #把重复量写回数据库，不是1的即为有重复
