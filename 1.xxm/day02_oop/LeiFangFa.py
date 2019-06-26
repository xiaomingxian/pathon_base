class Tool:
    count = 1

    @classmethod
    def myMethod(cls):
        print("类属性:%d" % cls.count)


# Tool.myMethod()
# 对象读类方法
# Tool().myMethod()


# 静态方法--不需要访问类属性/实例属性--不需要self,不需要调用属性
class Dog:
    @staticmethod
    def run():
        print("run...")


Dog.run()


# 案例
class Game:
    # 类属性
    historyCount = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def help():
        print("游戏帮助信息")

    @classmethod
    def showScore(cls):
        print("历史最高分%d" % cls.historyCount)

    def start(self):
        print("%s开始游戏了" % self.name)

# 帮助信息
Game.help()
Game.historyCount
Game("Tom").start()