import multiprocessing
import socket


# multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。


def main():
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('localhost', 7070))
    ser.listen(128)
    while True:
        clientSocket, clientMsg = ser.accept()
        p = multiprocessing.Process(target=clientResponse, args=(clientSocket,))
        p.start()
        # 子进程会拷贝一份父进程---把两个socket都关闭才算是真正的关闭--可参见说明
        clientSocket.close()


def clientResponse(clientSocket):
    url = clientSocket.recv(1024).decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
    if url:
        try:
            clientSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
            with open(url, 'rb')  as f:
                r = f.read()
                clientSocket.send(r)
                clientSocket.close()
        except Exception as e:
            clientSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
            clientSocket.send('找不到资源了...'.encode('gbk'))
            clientSocket.close()

    else:
        clientSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n".encode('utf-8'))
        clientSocket.send('请求为空....'.encode('gbk'))
        clientSocket.close()


if __name__ == '__main__':
    main()
