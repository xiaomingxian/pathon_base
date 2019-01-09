def out(fun):
    def inner():
        return "<td>" + fun() + "</td>"

    return inner


def out2(fun):
    def inner():
        return "<h1>" + fun() + "</h1>"

    return inner


@out
@out2
def test():
    return "xxx"


def main():
    print(test())


if __name__ == '__main__':
    main()
