# __new__为实例分配内存空间
class Music(object):
    instance = None

    chushi = False

    # new是创建实例
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Music.chushi:
            return
        print("初始化")
        Music.chushi = True


m1 = Music()
m2 = Music()
print(m1, "\n", m2)

c = tuple([1, 2, 3])
print(c)
