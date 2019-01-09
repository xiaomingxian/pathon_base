import socket
import gevent
from gevent import monkey

monkey.patch_all()


def main():
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('localhost', 8888))
    ser.listen(128)
    while True:
        clientSocket, clientMsg = ser.accept()

        gevent.joinall([

            gevent.spawn(response, clientSocket)

        ])


def response(clientSocket):
    url = clientSocket.recv(1024).decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
    if url:
        try:
            with open(url, 'rb') as f:
                clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('gbk'))
                clientSocket.send(f.read())
                clientSocket.close()
        except:
            clientSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode('gbk'))
            clientSocket.send('没有发现资源...'.encode('gbk'))
            clientSocket.close()
    else:
        clientSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode('gbk'))
        clientSocket.send('请求资源为空...'.encode('gbk'))
        clientSocket.close()


if __name__ == '__main__':
    main()
