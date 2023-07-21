'''0. 装饰器的作用是什么？
简洁化代码，可以插入代码 防止因为需求过多或者需求冲突产生错误
###########################装饰器本质上也是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能。
1. 装饰器必须是由嵌套函数实现吗？
是的
2. 如果使用装饰器去装饰一个函数，那么是否需要改动到该函数的内容呢？
不需要
3. 所以说，装饰器本身也是一个函数，它的功能是将目标函数进行打包，并返回一个加工后的新函数对象，对吗？
对的
4. 请问下面代码中，@add、@cube、@square 三个装饰器的执行顺序是？
square cube add'''


'''def add(func):
    def inner():
        x = func()
        return x + 1

    return inner


def cube(func):
    def inner():
        x = func()
        return x * x * x

    return inner


def square(func):
    def inner():
        x = func()
        return x * x

    return inner


@add
@cube
@square
def test():
    return 2
answer = add(cube(square(test)))

print(answer())
'''
import time


def fib():
    back1, back2 = 0, 1
    @fib_time
    def func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ')
        return back1

    return func


def fib_time(func):
    def sleep():
        time.sleep(1)
        func()
    return sleep

def get_fib(n):
    f = fib()
    for i in range(n):
        f()


n = int(input("请输入需要获取的斐波那契数："))
get_fib(n)

