'''0. 为什么将闭包称之为 “工厂函数”？
因为就像工厂一样 给送进来的参数统一进行打包，通过镶嵌好的函数统一输出
####################能生产函数的函数
1. 实现闭包必须要用到嵌套函数吗？
是的
2. 请问下面代码会打印什么呢？
520'''
'''
                                                    >>> def funA(x):
                                                    ...     def funB(y):
                                                    ...         def funC(z):
                                                    ...             return x * y * z
                                                    ...         return funC
                                                    ...     return funB
                                                    ...
                                                    >>> funA(3)(4)(5)
60
                                                    >>> f = lambda n : lambda x : x ** n
                                                    >>> g = f(2)
                                                    >>> g(3)
                                                    9
                                                    >>> g(5)
                                                    25
def make_avg():
    num = 0
    sum = 0
    def cal(x):
        nonlocal num,sum
        sum += x
        num += 1
        print(sum/num)
    return cal
avg = make_avg()
avg(5)
avg(3)
avg(7)
avg(19)'''
'''def make_avg():
    values = []
    def averager(value):
        values.append(value)
        total = sum(values)
        return total / len(values)
    return averager'''

def fib():
    fir = 0
    sec = 1
    def cal():
        nonlocal fir,sec
        fir,sec = sec,fir + sec
        print(fir)
    return cal
f = fib()
f()
f()
f()
f()
f()
f()
f()
f()
f()
