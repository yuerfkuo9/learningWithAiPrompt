'''
def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c
add函数可能会对0个或多个参数进行加法运算，在不确定参数个数的时候，使用可变参数,如下
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，
最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。
--module3.py
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

--test.py

import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
'''