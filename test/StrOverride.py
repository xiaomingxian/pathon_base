class A():
    sex=1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)


def main():
    a=A('tom', 10)
    print(a)


if __name__ == '__main__':
    main()
