def out(fun):
    def inner():
        # fun()
        return fun()

    return inner


@out
def test():
    print('....test')
    return "xxx"


def main():
    print(test())


if __name__ == '__main__':
    main()
