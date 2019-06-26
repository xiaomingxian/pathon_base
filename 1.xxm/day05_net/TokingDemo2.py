import socket


def main():
    p1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    p1.bind(('',10010))#绑定到任何ip
    while True:

        r=p1.recvfrom(1024)
        print(r[0].decode('UTF-8'))
        t = input("p2:")
        p1.sendto(t.encode('utf-8'),('localhost',10086))


if __name__ =="__main__":
    main()