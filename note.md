end = ""
"添加后可以换行"

"print('%.1f 华氏温度 = %.1f 摄氏温度' % (huashi,sheshi))"
"免于更改数字 %d整数占位符 %f小数占位符 %%百分号"

"//是除完去除小数，%是余数"
'''
Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），代码如下所示。
str2 = 'abc123456'

CHAR
--------------------------------
--------------------------------
strip(chars = None)： 字符串左右不留空白 或给定char参数 单个字符串

lstrip(chars = None)： 字符串去除左侧空白 或给定char参数 单个字符串

rstrip(chars = None)： 字符串去除右侧空白 或给定char参数 单个字符串

removeprefix(prefix)： 字符串前缀 去除整个prefix字符串

removesuffix(suffix)： 字符串后缀 去除整个suffix字符串

### 拆分和拼接
partition(sep)： sep参数代表切割符 会返回从左到右 切割符左边 切割符本身 和切割符右边共同组成的三个元素的元组

rpartition(sep)：方向相反 sep参数代表切割符 会返回从右到左 切割符左边 切割符本身 和切割符右边共同组成的三个元素的元组

split(sep = None,maxsplit = -1): sep参数同上，默认为空格。maxsplit为-1代表只要有切割符就切割 1代表切一个 以此类推

rsplit(sep = None,maxsplit = -1): 方向相反 sep参数同上，默认为空格。maxsplit为-1代表只要有切割符就切割 1代表切一个 以此类推

splitlines(keepends = False):按行进行分割，最后输出列表 换行符

join(iterable):字符串拼接

LIST
--------------------------------
--------------------------------

removeprefix(prefix)

removesuffix(suffix)
    
Python中还有另外一种定义生成器的方式，
就是通过yield关键字将一个普通函数改造成生成器函数。
下面的代码演示了如何实现一个生成斐波拉切数列的生成器。
所谓斐波拉切数列可以通过下面递归的方法来进行定义：

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
    
装饰器可以用语法糖 @


'''
