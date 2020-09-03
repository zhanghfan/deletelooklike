import mysql.connector  #导入mysql包
 
mydb = mysql.connector.connect(
  host="127.0.0.1",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="root",   # 数据库密码
  database="test"# 数据库名
)
 
# print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM zz605 where A2 like '%天%安%财%产%保%险%股%份%有%限%公%司%四%川%省%分%公%司%'")
a = mycursor.fetchall()
print(a)
print(a[0][0])
mycursor.execute("SELECT * FROM zz605 where A2 like '%天%安%财%产%保%险%股%份%有%限%公%司%四%川%省%分%公%司%'")