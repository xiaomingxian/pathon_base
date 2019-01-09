import socket
# import DynmiacSource
# import WSGI
import sys


class App(object):

    def __init__(self):
        pass

    def main(self, port, application):
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser.bind(('', port))
        ser.listen(128)

        while True:
            talk_client, msg_client = ser.accept()
            # print('accept:', msg_client)

            while True:
                try:
                    rec = talk_client.recv(1024).decode('utf-8').split('\r\n')[0].split('/')[1].split(' ')[0]
                    # print(rec)

                    if not rec.endswith('.py'):

                        try:
                            with open(rec, 'rb') as f:
                                # 读取文件信息
                                con = f.read()
                                talk_client.send("HTTP/1.1 200 OK\r\n\r\n".encode('gbk'))
                                talk_client.send(con)
                        except Exception as e:
                            print('exception:', e)
                            talk_client.send("HTTP/1.1 200 OK\r\n\r\n".encode('gbk'))
                            talk_client.send('静态资源...'.encode('gbk'))

                        talk_client.close()
                        break
                    else:
                        # 动态资源
                        # 1.自定义简单类型
                        # talk_client.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
                        # talk_client.send(DynmiacSource.application(rec).encode('utf-8'))
                        # talk_client.close()
                        # 2.WSGI协议
                        print('--------------------------')
                        dic = dict()
                        dic["PATH-INFO"] = rec
                        # body = WSGI.application(dic, self.method)
                        body = application(dic, self.method)
                        print('body:', body)
                        response = "HTTP/1.1 " + self.status + " \r\n"
                        # 服务端的信息应该放在  服务端返回
                        self.heads += ('server', 'my_server_min1.0')
                        for i in self.heads:
                            response += i[0] + '=' + i[1]
                        talk_client.send((response + "\r\n\r\n" + body).encode('gbk'))
                        talk_client.close()
                        break

                except Exception as e:
                    print("exception:", e)
                    talk_client.close()
                    break
                    pass

    def method(self, status, heads):
        # print('method:', status, heads)
        self.status = status
        self.heads = heads
        pass


def main():
    if sys.argv.__len__() == 3:
        try:
            port = int(sys.argv[1])
            app = sys.argv[2].split(':')
            mod = __import__(app[0])
            application = getattr(mod, app[1])
        except Exception as e:
            print('参数格式错误...',e)
            return
        app = App()
        app.main(port, application)


if __name__ == '__main__':
    main()
