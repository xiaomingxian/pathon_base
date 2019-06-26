class Woman:
    """
    doc
    """

    def __init__(self, name, age):
        self.name = name
        self.__age = age


wm = Woman("tom", 18)
# 私有属性的访问--对象名._类名__私有属性名
print(wm._Woman__age)
print(wm.__dict__)
print(wm.__doc__)

# 私有属性---名字重整    _类名__私有属性名
