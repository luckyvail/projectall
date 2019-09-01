"""
Chat room
env:python 3.6
socket fork 练习
"""
from socket import *
import os,sys
#服务器地址
server_addr=("0.0.0.0",8888)
user={}


def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        # print(data.decode())
        msg=data.decode().split(" ")
        if msg[0]=="L":
            do_login(s,msg[1],addr)
        elif msg[0]=="C":
            text=" ".join(msg[2:])
            do_chat(s,msg[1],text)
        elif msg[0]=="Q":
            do_quit(s.msg[1],addr)

def do_login(s,name,addr):
    if name in user or "管理员" in name:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b"OK",addr)

    #通知其他人
    msg= "欢迎%s大神进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])

    #将用户加入
    user[name]=addr

def do_chat(s,name,text):
    msg="%s : %s"%(name,text)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])

#退出
def do_quit(s,name):
    msg="%s退出了聊天室"%name
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"EXIT",user[i])

    # 将用户删除
    del user[name]

#创建网络连接
def main():
    #套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(server_addr)

    pid = os.fork()
    if pid < 0:
        return

    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息"+msg
            s.sendto(msg.encode(),server_addr)
    else:
        #请求处理
        do_request(s) #处理客户端请求


if __name__=="__main__":
    main()





