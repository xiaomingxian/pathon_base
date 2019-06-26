# orm思路:
# orm特点：类名 和 属性  映射到 表名 和字段名

# 自定义元类  对类 结构进行改变
# 删除 args中原来的属性(key,value)
# 增加映射    属性(key,value)  table(key,value)


class OrmUtil(type):

    def __new__(cls, lName, fNames, args):
        # 思路:用 id = ('id', 'int') 后面的元组  替换原有的 id属性  将表名也存储为对应的属性
        mapping = {}
        tableName = lName

        for k, v in args.items():
            if isinstance(v, tuple):
                mapping[k] = v
        # 删除属性中原有的简单对应关系
        for key in mapping.keys():
            args.pop(key)

        # 将映射关系和表名存入属性列表
        args['__mapping__'] = mapping
        args['__tableName__'] = tableName

        # 返回类引用
        return type(lName, fNames, args)

        pass


class Brand(metaclass=OrmUtil):
    id = ('id', 'int')

    name = ('name', 'varchar')
    age = ('age', 'varchar')
    address = ('address', 'varchar')
    sex = ('sex', 'varchar')
    hobbi = ('hobbi', 'varchar')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        tableName = self.__tableName__
        kv = {}
        for k, v in self.__mapping__.items():
            value = getattr(self, k, None)
            kv[v[0]] = """'%s'""" % value
        sql = 'insert into %s (%s) values (%s)' % (
            tableName, ",".join(kv.keys()), ','.join([str(i) for i in kv.values()]))
        print(sql)

    def __str__(self):
        return '[id=%s,name=%s]' % (str(self.name), str(self.name))


def main():
    b = Brand(id=1, name=10, age=20, address='China')
    print(b)
    b.save()


if __name__ == '__main__':
    main()
