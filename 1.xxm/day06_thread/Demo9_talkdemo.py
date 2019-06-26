import socket
import threading


def send(soc):
    while True:
        my = input("我:")
        soc.sendto(my.encode('utf-8'), ('localhost', 8887))


def rec(soc):
    while True:
        r=soc.recvfrom(1024)
        print((r[0]).decode('gbk'))
        pass


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(('', 8888))
    # soc.connect(('', 8887))----udp不需要建立连接

    t1 = threading.Thread(target=send, args=(soc,))
    t2 = threading.Thread(target=rec, args=(soc,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
