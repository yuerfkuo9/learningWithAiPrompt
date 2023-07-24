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
'''k = ' '.join(["I","love","Fishc"])
print(k)
print(",\n".join("FishC"))'''

#0. 编写一个生成凯撒密码的程序
'''origin = input("请输入需要加密的明文（只支持英文字母）：")
plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
place = int(input("请输入需要移动的位数："))
result = ''
for k in range(len(origin)):
    count = plaintext.find(origin[k])
    count += place
    if count > len(plaintext):
        count -= len(plaintext)
    if origin[k] == ' ':
        result += ' '
    else:
        result += plaintext[count]
print(result)'''

'''plain = list(input("请输入需要加密的明文（只支持英文字母）："))
key = int(input("请输入移动的位数："))

base_A = ord('A')
base_a = ord('a')

cipher = []
for each in plain:
    if each == ' ':
        cipher.append(' ')
    else:
        if each.isupper():
            base = base_A
        else:
            base = base_a
        cipher.append(chr((ord(each) - base + key) % 26 + base))

print(''.join(cipher))'''
#cipher.append(chr((ord(each) - base + key) % 26 + base)) 在027讲过

'''#1给定一个字符串数组 words，只返回可以使用在美式键盘同一行的字母打印出来的单词，键盘布局如下图所示
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
fir_line = "qwertyuiop"
sec_line = "asdfghjkl"
thi_line = "zxcvbnm"
for i in range(len(words)):
    count = 0
    f = 0
    s = 0
    t = 0
    clean_words = str.lower(words[i])
    for j in range(len(words[i])):
        if clean_words[j] in fir_line:
            f += 1
        elif clean_words[j] in sec_line:
            s += 1
        elif clean_words[j] in thi_line:
            t += 1
    print(f,s,t)
    if f== len(words[i]) or s == len(words[i]) or t == len(words[i]):
        print(words[i])'''

#使用strip方法
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]

res = []
for i in words:
    # 由于单词存在大小写，所以这里统一先转换为小写字母
    j = i.lower()
    # 灵活运用 strip() 方法，判断 j 是否所有字符都在键盘的同一行内
    if j.strip("qwertyuiop") == '' or j.strip("asdfghjkl") == '' or j.strip("zxcvbnm") == '':
        res.append(i)

print(res)

'''test = list(input("输入的都会变成单独的字符串值被储存在列表中，exp：ambition /a m b i t i o n "))
print(test)'''

