import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 7788))
    while True:
        server.listen(128)
        # 元组类型
        # 这里会阻塞 --直到下一个客户端连接上
        talk_socket, clientaddress = server.accept()
        print(clientaddress)
        # 当客户端关闭接收的值为NONE
        while True:
            rec_data = talk_socket.recv(1024)
            print("rec_data:%s" % rec_data.decode('utf-8'))

            if rec_data:
                # 回复
                talk_socket.send("这是回复".encode('utf-8'))
            else:
                break

        #关闭--talk-socket
        talk_socket.close()
    server.close()


if __name__ == "__main__":
    # x=4755-3520
    # x=4755-(1056+179+704)
    x=4755-(3520+179+704)
    print(x/2)
    print(176*21)

    # main()
