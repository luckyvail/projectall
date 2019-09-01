"""
dict 客户端
发起请求,展示结果
"""

from socket import *
from getpass import getpass


ADDR=('127.0.0.1',8008)
# 所有函数都用s
s = socket()
s.connect(ADDR)

def do_query(name):
    while True:
        word = input("单词,输入##退出:")
        if word == '##': #结束单词查询
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        data=s.recv(2048).decode()
        print(data)

def do_hist(name):
    msg = "H %s"%(name)
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data=='OK':
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print("还没有历史记录")

#二级界面
def login(name):
    while True:
        print("=========Query=========")
        print("**    1.查询单词      **")
        print("**    2.历史记录      **")
        print("**    3.注销          **")
        print("=======================")
        cmd=input("输入选项")
        if cmd=="1":
            do_query(name)
        elif cmd == "2":
            do_hist(name)
        elif cmd == "3":
            return
        else:
            print("请输入正确命令")

#注册
def do_register():
    while True:
        name = input("User:")
        passwd = getpass("请输入密码:")
        passwd1 = getpass("请再输入一次密码:")
        if (" " in name) or (" " in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码输入不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())
        #接收反馈
        data=s.recv(128).decode()
        if data=="OK":
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return

# 处理登录
def do_login():
    name = input("User:")
    passwd = getpass("请输入密码:")
    msg= "L %s %s"%(name,passwd)
    s.send(msg.encode())
    # 等待反馈
    data = s.recv(128).decode()
    if data == "OK":
        print("登录成功")
        login(name)
    else:
        print("登录失败")




#创建网络连接
def main():
    while True:
        print("========Welcome========")
        print("**      1.注册        **")
        print("**      2.登录        **")
        print("**      3.退出        **")
        print("=======================")
        cmd=input("输入选项")
        if cmd=="1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b"E")
            print("谢谢使用")
            return
        else:
            print("请输入正确命令!")

if __name__=="__main__":
    main()