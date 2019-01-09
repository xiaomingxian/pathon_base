# 客户端
import socket


def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',8899))
    while True:
        filename=input("filename:")
        client.send(filename.encode('utf-8'))
        rec=client.recv(1024)
        if rec!=b'1':
            print("....",rec)
            with open("新"+filename,'wb') as f:
                f.write(rec)
            print("下载成功...")
        else:

            print("没有接收到内容...")


if __name__ == "__main__":
    main()
