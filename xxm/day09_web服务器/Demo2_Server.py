import socket
import re


def server():
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口重用
    ser.setsockopt(socket.SOL_SOCKET, socket.SOCK_STREAM, 1)
    ser.bind(('localhost', 9090))
    ser.listen(128)
    while True:
        sock_client, client_msg = ser.accept()
        s = sock_client.recv(1024)

        # sock_client.close()
        # 中文乱码未解决...
        source = s.decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
        if source:
            try:
                with open(source, 'rb') as f:
                    print("资源存在.......")
                    sock_client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
                    sock_client.send(f.read())
                    sock_client.close()
                    pass
            except:
                sock_client.send('HTTP/1.1 404 NOT FOUND\r\n\r\n'.encode('utf-8'))
                sock_client.send("您访问的资源不存在...".encode('gbk'))
                sock_client.close()
                print('资源不存在...')


# 进程(父子close) 线程(共享全局变量只需关闭一个)  携程  来做
if __name__ == '__main__':
    server()
    # test()
