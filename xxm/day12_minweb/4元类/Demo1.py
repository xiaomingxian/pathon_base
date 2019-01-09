# coding=utf-8
def AA():
    pass


def main():
    a = 'xxx'
    g = globals()
    print(type(g))
    for i in g.items():
        print(i)
    print('----------------')
    print(type(g['__builtins__']))
    for i in g['__builtins__'].__dict__.keys():
        if 'print' in i:
            print('...........')
        print(i)
    p = g['__builtins__'].__dict__['print']
    p('kkkkkkkkkkkkk  print  test   not Chinese ??? ...')


if __name__ == '__main__':
    main()
