import socket


def main():
    # 创建套接字
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    client.connect(('localhost',7788))
    while True:
        i=input("我：")
        if i=="exit":
            break
        else:
            #发送数据
            client.send(i.encode('utf-8'))
            # 接收数据
            rec_data=client.recv(1024)
            print("服务器："+rec_data.decode('utf-8'))
    # #关闭连接
    client.close()



if __name__=="__main__":
    main()