import redis
import threading

r = redis.Redis(host="192.168.2.63", port="7111", db=0)

x = 1


def keys():
    s = r.keys("*")
    for i in s:
        print(i)
        x=x+1


def main():
    t1 = threading.Thread(target=keys())
    t2 = threading.Thread(target=keys())
    t3 = threading.Thread(target=keys())

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()
    print("====",x)
