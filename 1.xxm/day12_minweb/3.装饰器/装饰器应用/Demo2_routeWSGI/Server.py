import socket
import Application


class Server(object):
    def __init__(self):
        pass

    def server(self):
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser.bind(('localhost', 7777))
        ser.listen()
        while True:
            talk_cli, msg_cli = ser.accept()
            while True:
                urly = talk_cli.recv(1024).decode('utf-8').split('\r\n')[0].split('/')
                print('原:', urly)
                url = urly[1].split(' ')[0]
                if urly.__len__() > 3:
                    url = ''
                    for i in range(1, urly.__len__() - 1):
                        url += urly[i].split(' ')[0]
                        if not urly[i].__contains__('HTTP'):
                            url += '/'
                if url.__contains__('js/jquery-1.11.3.min.js'):
                    url = 'js/jquery-1.11.3.min.js'

                if url.endswith('/'):
                    # print('uuu:', url.__len__() - 1)

                    url = url[0: int(url.__len__() - 1)]
                print('url:', url)
                if url.endswith('.py'):
                    # 动态
                    env = dict()
                    env['PATH-INF'] = url
                    body = Application.application(env, self.myMethod)
                    response = self.status + '\r\n'
                    for i in self.heads:
                        response += i[0] + "=" + i[1] + "\r\n"
                        response += '\r\n'
                    talk_cli.send((response + body).encode('utf8'))
                else:

                    try:
                        with open(url, 'rb') as f:
                            con = f.read()
                            # heads
                            talk_cli.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf8'))
                            # talk_cli.send("静态资源...\r\n\r\n".encode('utf8'))
                            talk_cli.send(con)
                    except Exception as e:
                        # print("eee:", e)

                        talk_cli.send('HTTP/1.1 404 NOT FOUND\r\n\r\n'.encode('utf8'))
                        talk_cli.send("资源不存在...\r\n\r\n".encode('utf8'))

                talk_cli.close()
                break

    def myMethod(self, status, heads):
        self.status = status
        self.heads = heads
        pass


def main():
    ser = Server()
    ser.server()


if __name__ == '__main__':
    main()
