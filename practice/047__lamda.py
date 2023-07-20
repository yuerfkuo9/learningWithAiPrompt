'''def cal (x,y,z):
    return x + y + z
print(cal(1,2,3))'''
#请问下面代码会返回 True 还是 False 呢？ false true
#3.不可以
'''[x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''
#5. 请将下面的闭包函数成 lambda 表达式的实现形式？
'''a = map(lambda x: x ** 2 % 2, range(10))
print(list(a))
b = filter(lambda k: k ** 2 % 2  , range(10))
print(list(b))
def test1 (exp):
    k = lambda x : x ** exp
    return k
square = test1(2)
cube = test1(3)
print(square(2))
print(cube(3))'''

#6. 请将下面三个装饰器函数写成 lambda 表达式的实现形式？
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


print(test())'''

'''a1 = lambda x : x + 1
a2 = lambda x : x * x * x
a3 = lambda x : x * x
def test():
    return 2
print(a1(a2(a3(test()))))'''

power = {"a": 999, "b": 888, "c": 666, "d": 900, "e": 789, "f": 999}

# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
greater = []
for k, v in power.items():
    if v > 800:
        greater.append((k, v))
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码

print(greater)
[('a', 999), ('b', 888), ('c', 900), ('d', 999)]
print(power.item[1])

power = {"a": 999, "b": 888, "c": 666, "d": 900, "e": 789, "f": 999}
greater = filter(lambda x : x > 800,range(power))
b = filter(lambda k: k ** 2 % 2  , range(10))

members = {
    "apex" : {"loba":83, "robot":89, "seer":64, "ghost":75, "angel":96},
    "avenger" : {"iron_man":85, "spider_man":39, "capitan":82, "doctor":73, "thunder":99},
    "hero" : {"superman":99, "batman":84, "sea":63, "witch":78, "speed":78}}

# 请在此处添加一行代码，完成题目要求，并将结果保存在变量 x 中
x = filter(for each in members (if lambda k : x > ,range(members)))
print(x)
#['鱼C工作室:二师兄', '复仇者联盟:绿巨人', '奥特曼家族:泰罗']