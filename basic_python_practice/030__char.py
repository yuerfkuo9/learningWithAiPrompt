'''#0. 请问下面三行代码的执行结果分别是什么？
ilovefishc.com
www.ilovefishc
ilovefishc
#1. 请问下面代码打印的内容是什么？
wwilovefishc.com
2. split() 方法常常被应用于对数据的解析处理，
那么考考大家，如果要从字符串 "https://ilovefishc.com/html5/index.html" 中提取出 "ilovefishc.com"，使用 split() 方法应该如何实现呢？'''
instant1 = "https://ilovefishc.com/html5/index.html"
instant1 = instant1.split("/")
print(instant1[2])
#3. 如果要求按换行符来分割字符串，小甲鱼推荐使用 splitlines() 方法，而非 split("\n")，你觉得小甲鱼的依据是什么？
# 因为split如果遇到使用不同换行符的时候没有使用splitlines的时候更好用，splilines是统一格式

#4. 下面代码使用加号运算符（+）进行字符串拼接，现在看起来有点太 low 了，请将它改为使用 join() 方法来拼接吧~!?