import threading
import socket


def main():
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('localhost', 7777))
    ser.listen(128)
    while True:
        clientSocket, clientMsg = ser.accept()
        t = threading.Thread(target=response, args=(clientSocket,))
        t.start()


def response(clientSocket):
    url = clientSocket.recv(1024).decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
    if url:
        try:
            with open(url, 'rb') as f:
                clientSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode('gbk'))
                clientSocket.send(f.read())
                clientSocket.close()
        except:
            clientSocket.send("HTTP/1.1 404 NOT Found\r\n\r\n".encode('gbk'))
            clientSocket.send('没有此资源...'.encode('gbk'))
            clientSocket.close()
    else:
        clientSocket.send("HTTP/1.1 404 NOT Found\r\n\r\n".encode('gbk'))
        clientSocket.send('url为空...'.encode('gbk'))
        clientSocket.close()


if __name__ == '__main__':
    main()
