"""
写数据库连接
增删改
"""
# import pymysql
#
# #链接数据库
# db=pymysql.connect(host="localhost",
#                    port=3306,
#                    user="root",
#                    password="123456",
#                    database="stu",
#                    charset="utf8")
#
# #创建游标
# cur=db.cursor()
#
# try:
#     sql="insert into interest values (6,'Abby','draw,sing','A','8888','还可以');"
#
#     cur.execute(sql)
#
#     #修改操作
#     sql="update interest set price=6666 where name = 'Abby';"
#
#     cur.execute(sql)
#
#     #删除操作
#     sql="delete from myclass where score < 88;"
#
#     cur.execute(sql)
#
#     db.commit()
#
# except Exception as e:
#     db.rollback()
#     print("出现异常,内容回滚")
#
# cur.close()
# db.close()



#链接数据库

# import pymysql
#
# db=pymysql.connect(host="localhost",
#                    port=3306,
#                    user="root",
#                    password="123456",
#                    database="stu",
#                    charset="utf8")
#
# #创建游标
# cur=db.cursor()
#
# sql="select * from myclass where age=12;"
#
# #执行语句 cur 拥有查询结果
#
# cur.execute(sql)

#获取查找结果的第一个
# one_row=cur.fetchone()
# print(one_row)

#获取查找结果前两个
# many_row=cur.fetchmany()
# print(many_row)

#获取全部查询结果
# all_row = cur.fetchall()
# print(all_row)

# while True:
#
#     one_row=cur.fetchone()
#     if not one_row:
#         break
#     print(one_row)

#
# cur.close()
# db.close()
import pymysql
import re

db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   password="123456",
                   database="dict",
                   charset="utf8")

cur=db.cursor()

with open("/home/tarena/桌面/dict.txt","r") as fd:
    data=fd.readlines()


for i in data:
    tmp = i.split(' ')
    word = tmp[0]  # 获取单词
    mean = ' '.join(tmp[1:]).strip()
    sql="insert into words (word,mean) values (%s,%s);"
    # print(sql)
    try:
        cur.execute(sql,[word,mean])

    except Exception as e:
        db.rollback()
        print(e)

db.commit()
cur.close()
db.close()










