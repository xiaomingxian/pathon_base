# with open('...')  as f:
# ...
# 在打开或者读写的时候发生过异常会自动关闭---前提:可以打开
import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',8899))
    server.listen(128)
    while True:
        # 一直保持监听
        withClientSocket, ipAndAddress = server.accept()
        while True:
            #  一直为同一个客户端服务
            filename = withClientSocket.recv(1024)
            print("文件名%s："%filename)

            try:
                context = open(filename,'rb').read()
                if context:
                    print("发送数据...")
                    withClientSocket.send(context)
                    # break
                else:
                    # withClientSocket.send(False)
                    print("文件没有内容")
                    # break

            except Exception as result:
                withClientSocket.send(b'1')
                print("捕获到的异常%s" % str(result))
                # break

        withClientSocket.close()
    #关闭服务端
    server.close()

def test():
    try:
        open('aaa')
    except Exception as result:
        print(result)


if __name__ == "__main__":
    pass
    # test()
    main()
