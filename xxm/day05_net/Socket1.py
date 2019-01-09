import socket


# 网络调试助手

def main():
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 字节类型，元组类型
    # 绑定端口
    socket1.bind(('', 8888))
    # socket1.sendto(b'fa-song', ('localhost', 8080))
    socket1.sendto('fa-song    '.encode('utf-8'), ('localhost', 8080))

    socket1.close()
    print("---run---")


def receive():
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket2.bind(('', 8889))#''默认绑定的是自己的ip
    #     接收
    rec=socket2.recvfrom(1024)
    # print(rec)#(b'11111', ('127.0.0.1', 8880))
    print(rec[0].decode('utf-8'))


def sendAndReceive():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('',8888))
    while True:
        s.sendto("收发测试".encode('gbk'),('localhost',8082))
        #接收
        r=s.recvfrom(1024)
        print(r[0].decode('gbk'))

if __name__ == "__main__":
    # main()
    # while True:
        # receive()
        sendAndReceive()
