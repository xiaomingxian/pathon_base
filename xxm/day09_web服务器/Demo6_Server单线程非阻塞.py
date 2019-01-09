import socket
import time


def main():
    # 定义集合存储客户端socket
    clientSocketList = list()
    ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('localhost', 9999))
    # 并发数设置
    ser.listen(128)
    # 非阻塞设置...
    ser.setblocking(False)
    while True:
        # 设置不阻塞
        time.sleep(1)
        try:
            # 客户端到来
            clientSocket, clientMsg = ser.accept()
            clientSocket.setblocking(False)
            print('客户端到来：-----', clientMsg)
            clientSocketList.append(clientSocket)

        except Exception as e:
            print("客户端没来.....", e)
            pass

        # 查看是否有信息
        for cs in clientSocketList:
            try:
                # rec = cs.recv(1024)
                # print('url..', rec.decode('gbk').split('\r\n')[0].split('/')[1].split(' ')[0])
                response(cs)
            except Exception as e:
                cs.close()
                clientSocketList.remove(cs)
                print('len:', clientSocketList.__len__())
                print('接收信息异常/没有发送消息...', e)
            else:
                print('没有异常.....')


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


def test():
    list = [1, 2, 3, 4]
    for i in list:
        if i == 2:
            print("移除...")
            list.remove(i)
    print(list.__len__())


if __name__ == '__main__':
    main()
    # test()
