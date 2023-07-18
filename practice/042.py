#0. 如果一个函数要求传递位置参数，那么颠倒实参的顺序，肯定会报错，是吗？
"""也不一定。比如 min() 或者 max() 函数，参数顺序没有要求"""
#1. 默认参数跟关键字参数有啥区别？
'关键字参数必须传递实参，默认参数可以传递实参和形参'
#2. 任何支持传递位置参数的函数，都可以使用关键字参数吗？
'也不全是'
#2.1 位置参数和关键字参数的区别是什么
#3. 请问下面代码是否会报错，为什么？
'''def abc(a, /, b, c):
    print(a, b, c)

abc(3, b=2, c=1)'''
'////////////          会 斜杠左侧不能使用关键字参数 只能使用位置参数 '
# 4.请问这里会报错吗,为什么？
'''def abc(a, *, b, c):
    print(a, b, c)
abc(c=3, b=2, a=1)'''
'不会,因为*号右边需要位置参数，左边不需要'
'''def myfunc(s, vt, o):
    print("".join((o, vt, s)))
    return "".join((o, vt, s))'''


'''import pypinyin
class Decide_word_reverse(object):
    def __init__(self,word):
        self.word = word
    def convert_pinyin(self):
        self. pinyin = pypinyin.pinyin(self.word,style=pypinyin.NORMAL)
        return self.pinyin
    def decide_word(self):
        dec = 1
        for i in range(int(len(self.pinyin) / 2)):
            print(self.pinyin[i])
            print(self.pinyin[len(self.pinyin) - 1 - i])
            if self.pinyin[i] != self.pinyin[len(self.pinyin) - i - 1]:
                dec = 0
                break
        if dec :
            print("这句话为回文")
        else :
            print("这句话不是回文")
def main():
    decide = Decide_word_reverse("小甲鱼")
    decide.convert_pinyin()
    decide.decide_word()

if __name__ == "__main__":
    main()'''

class Stack(object):
    def __init__(self,list):
        self.list = list
    def pop(self):
        self.list.pop(-1)
    def push(self,value):
        self.list.append(value)
        pass
    def show(self):
        print(self.list)
        pass
def main():
    stack = Stack([6,9,10,2,3,5])
    stack.push(10)
    stack.show()


if __name__ == "__main__":
    main()