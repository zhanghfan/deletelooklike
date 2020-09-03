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
for m in range(1,533): # m为计数器，有多少行数据后面的数+1 m为ff605序号
    p = "SELECT A3 FROM ff605 WHERE A1 = "+str(m) #选出子表党组织名字，data改为新表名
    print(p)
    mycursor = mydb.cursor() # 初始化数据库游标
    mycursor.execute(p)      #执行sql语句，完成关键词数据提取
    i = mycursor.fetchone() # 取得数据库返回结果，数据库输出传回python
    j = ""+i[0]   #拼接sql语句
    h = "%".join(j)
    k = "%"+h+"%"   #把关键词用%隔开
    print(k)
    x = "\'"+k+"\'"
    g = "SELECT count(*) FROM zz605 where A2 like "+x #求得和C3相似的C2总数
    g1 = "SELECT A1 FROM zz605 where A2 like "+x
    print(g)
 #  mycursor = mydb.cursor()
    mycursor.execute(g)
    d = mycursor.fetchone()  
    print(d)
    b = d[0]
    print(b)
    if b == 0:
        a = "UPDATE ff605 SET A19 = 0"+" WHERE A1 = "+str(m) #没找到得在ff605标0
        print(a)
        mycursor.execute(a) #把重复量写回数据库，不是1的即为有重复
    elif b == 1:
        mycursor.execute(g1)
        ll = mycursor.fetchone()
        print(ll)
        kk = ll[0]
        print(kk)
        ss = "UPDATE zz605 SET A6 = "+str(b)+" WHERE A1 = "+str(kk) #找到得在zz605标数量
        mycursor.execute(ss)
    else:
        mycursor.execute(g1)
        lll = mycursor.fetchall()
        print(lll)
        kkk = lll[0][0]
        print(kkk)
        sss = "UPDATE zz605 SET A6 = "+str(b)+" WHERE A1 = "+str(kkk) #找到得在zz605标数量
        mycursor.execute(sss)