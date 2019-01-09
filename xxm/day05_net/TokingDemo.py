import socket


def main():
    p1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    p1.bind(('',10086))#绑定到任何ip
    while True:
        t=input("p1:")
        p1.sendto(t.encode('utf-8'),('localhost',10010))
        r=p1.recvfrom(1024)
        print(r[0].decode('UTF-8'))


if __name__ =="__main__":
    main()