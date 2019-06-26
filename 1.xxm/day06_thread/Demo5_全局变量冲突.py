import threading
import time

num=0

def t1(n):
    for i in range(n):
        global  num
        num+=1


def t2(n):
    for i in range(n):
        global  num
        num+=1



def main():
    tt1=threading.Thread(target=t1,args=(10000000,))
    tt2=threading.Thread(target=t1,args=(10000000,))
    tt1.start()
    tt2.start()


if __name__=="__main__":
    main()
    time.sleep(0.5)
    print(num)