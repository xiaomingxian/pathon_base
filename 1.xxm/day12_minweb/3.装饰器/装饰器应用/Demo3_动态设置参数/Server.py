import socket
import sys


class Server(object):
    def __init__(self):
        pass

    def server(self, port, application):
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ser.bind(('localhost', 7777))
        ser.bind(('localhost', port))
        ser.listen()
        while True:
            talk_cli, msg_cli = ser.accept()
            while True:
                url = talk_cli.recv(1024).decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
                print('url : ', url)
                if url.endswith('.py'):
                    # 动态
                    env = dict()
                    env['PATH-INF'] = url
                    # body = Application.application(env, self.myMethod)
                    body = application(env, self.myMethod)
                    response = self.status + '\r\n'
                    for i in self.heads:
                        response += i[0] + "=" + i[1] + "\r\n"
                        response += '\r\n'
                    talk_cli.send((response + body).encode('gbk'))
                else:

                    try:
                        with open(url, 'rb') as f:
                            con = f.read()
                            # heads
                            talk_cli.send('HTTP/1.1 200 OK\r\n\r\n'.encode('gbk'))
                            # talk_cli.send("静态资源...\r\n\r\n".encode('gbk'))
                            talk_cli.send(con)
                    except Exception as e:
                        # print("eee:", e)
                        talk_cli.send('HTTP/1.1 404 NOT FOUND\r\n\r\n'.encode('gbk'))
                        talk_cli.send("资源不存在...\r\n\r\n".encode('gbk'))

                talk_cli.close()
                break

    def myMethod(self, status, heads):
        self.status = status
        self.heads = heads
        pass


def main():
    if sys.argv.__len__() == 3:
        # 端口号
        port = sys.argv[1]
        app = sys.argv[2].split(':')
        mod = __import__(app[0])
        # application中的核心函数
        method = getattr(mod, app[1])

        ser = Server()
        ser.server(int(port), method)


if __name__ == '__main__':
    main()
