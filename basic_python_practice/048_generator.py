#0. 迭代器可以看作是一种特殊的生成器吗？
'''是'''
#. 生成器是否支持下标索引？
'''不支持'''
#2. 生成器可以看作是 Python 对于 “延迟执行” 提供的技术支持，这种说法正确吗？
'''正确把 延迟执'''
#3. 你觉得生成器通常应用在什么场景会比较合适？4. 请问下面代码会打印 “YES” 吗？
'''def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
    print("YES")
for each in counter():
    print(each)'''
'''不会'''
#5. 生成器表达式和列表推导式的最大区别是什么？
'''生成器表达式是递归，列表表达式是生成器'''
#6. 下面这个列表推导式是不是有什么问题？为什么一直不出结果，你有什么办法解决这个问题么？
[x ** 2 for x in range(1000000)]
'''a = [x ** 2 for x in range(1000000)]
print(a)
因为没有列表print出来'''
#7. 请将下面的 map() 函数实现改为使用生成器表达式实现。
#list(map(abs, (-1, 2, -3, 4, -5)))
'''a = (abs(i) for i in range(1,6))
print(list(a))'''
#8. 请将下面的生成器表达式实现改为使用 filter() 函数实现。
#"".join(x for x in "FishC" if x.isupper())
'''l = "FishC" if x.isupper()
l.isupper()
a = filter(lambda x: "".join(x if x.isupper()),"FishC")'''
#9.利用生成器定义一个支持浮点数的 frange() 函数，其功能与 range() 函数相仿。
def frange(iteration,end = 0,precision = 0.1):
    if end :
        #print(0)
        while iteration <= end:
            yield iteration
            iteration += precision
    else:
        #print(1)
        while end <= iteration:
            yield end
            end += precision
for i in frange(1):
     print(i)