import multiprocessing


def p1():
    while True:
        print('1...')

def p2():
    while True:
        print('2--')

def main():
    pp1=  multiprocessing.Process(target=p1)
    pp2=  multiprocessing.Process(target=p2)
    pp1.start()
    pp2.start()
    pass


if __name__ == '__main__':
    main()