import threading
import time
# 共享全局变量

a=0

class Thread1(threading.Thread):
    def run(self):
        global a
        a+=3
class Thread2(threading.Thread):
    def run(self):
        print("a:%d"%a)



def main():
    t1=Thread1()
    t2=Thread2()
    t1.start()
    time.sleep(1)
    t2.start()



if __name__=="__main__":
    main()