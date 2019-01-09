# try catch
try:
    1 / 2
    # 1 / 0
    # 1 / ''
except ZeroDivisionError:
    print("除0异常")
except TypeError:
    print("除数格式不对")
except Exception as result:
    # 未知异常
    print(result)
else:
    print("没有异常时执行的代码")
finally:
    print("一定会被执行的代码")


# 异常传递---抛异常?
def demo():
    1 / 0


# 只需在主程序中捕获
try:
    demo()
except Exception as result:
    print(result)

# 主动抛出异常
x = 1


def demo2():
    if x != 2:
        raise Exception("主动抛出...")


try:
    demo2()
except Exception as result:
    print(result)
