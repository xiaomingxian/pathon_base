import json


class Person():
    def __init__(self, a, b):
        self.name = a
        self.age = b
        pass


list = [1, {'a': [2, 3, 4], 'b': 5}, Person('Tom', 20)]

# json_str = json.dumps(list, default=lambda o: o.__dict__, sort_keys=True, indent=4)
json_str = json.dumps(list, default=lambda o: o.__dict__, sort_keys=False, indent=4)

if __name__ == '__main__':
    print(json_str)

# 序列化--也是json
# from django.core import serializers
# jsondata = serializers.serialize('json', 对象)
