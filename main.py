# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
huashi = float(input("华氏温度是 "))

sheshi = (huashi - 32)/18
print('%.1f 华氏温度 = %.1f 摄氏温度' % (huashi,sheshi))

radius = int(input("圆的半径是 "))
zhou = 2*radius*3.1416
mian = 3.1416*radius*radius
print('%.1f 华氏温度 = %.1f 摄氏温度' % (zhou,mian))

y = int(input("年份是 "))
k = y % 100 and y % 4 == 0 or y % 400 == 0
print(k)

a = int(input())
unit = input("单位是")
if unit == "英寸":
    y = a/2.54
else:
    y = a*2.54
print(y)

grade = int(input())
if grade >= 90 :
    print("成绩是A")
elif grade >= 80:
    print("成绩是B")
elif grade >= 70:
    print("成绩是C")
elif grade >= 60:
    print("成绩是D")
else:
    print("成绩是E")

edge1 = int(input("请输入第一条边的长度： "))
edge2 = int(input("请输入第二条边的长度： "))
edge3 = int(input("请输入第三条边的长度： "))
if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge2 + edge3 > edge1 :
    peri = edge1 + edge2 + edge3
    p = 1/2 * peri
    area = p*(p-edge1)*(p-edge2)*(p-edge3)**0.5
    print('三角形的面积是%d，周长是%d' % (area,peri))
else:
    print("输入条件不符合三角形的形成条件")

value = int(input())
count = 1
if value > 1 :
    for i in range(2,value):
        print(i)
        if value % i == 0 :
            print(i)
            count = 0
            break
    print(count)
    if count  :
        print("该数为素数")
        print(count)
    else :
        print("该数不为素数")
        print(count)
else :
    print("该数字不为素数")

for i in range(1,6):
    print("")
    for j in range(1,i+1):
        print("*",end='')
for i in range(5):
    print("")
    for j in range(5):
        if j < 5-i-1:
            print("i",end='')
        else:
            print("*", end='')

for i in range(5):
    print("")
    print("i")
    for j in range(5-i-1):
        print("i",end='')
    for j in range(2*i+1):
        print("*", end='')

for num in range(100,1000):
    ge = num % 10
    #print(ge)
    shi = num // 10 % 10
    #print(shi)
    bai = int(num // 100)
    #print(bai)
    if num == ge **3 + shi ** 3 + bai **3 :
        print('%d 是水仙花数' % (num))

from random import randint

money = 1000
#初始资金
bet = 0
#赌注
valid = True
while money > 0:
    if bet > 1000 :
        print("您没有那么多的筹码")
        valid = False
    while True:
        bet = int(input("请输入本局的筹码："))
        if 0 < bet <= 1000:
            break
        else :
            print("您没有那么多的筹码")
    dice = randint(1,6) + randint(1,6)
    print('您摇出了%d'%dice)
    if dice == 7 or dice == 11:
        print("玩家获胜")
        money += bet
        print('您还有%d' % money)
    elif dice == 2 or dice == 3 or dice == 12 :
        print("玩家失败")
        money -= bet
        print('您还有%d' % money)
    else:
        while True:
            d2 = randint(1,6) + randint(1,6)
            print('您摇出了%d' % d2)
            if d2 == dice :
                print("玩家获胜")
                money += bet
                print('您还有%d' % money)
                break
            elif d2 == 7:
                print("玩家失败")
                money -= bet
                print('您还有%d' % money)
                break

print("您破产了")

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

#跑马灯文字
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
'''
#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
'''import random
import string

def veri_code (veri_code_length):
    random_str = ''.join(random.sample(string.ascii_letters + string.digits,20))
    return random_str
print(veri_code(20))
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ''
    for _ in range(code_len):
        a = random.randint(0,last_pos)
        code += all_chars[a]
    return code

print(generate_code(20))
#设计一个函数返回给定文件名的后缀名。
def give_file_extension(file_name):
    index = file_name.find('.')
    if 0< index <len(file_name) :
        return file_name[index+1:]
    else:
        return ''

print(give_file_extension("text."))

#设计一个函数返回传入的列表中最大和第二大的元素的值
def max_andmin_value(list):
    max = 0
    max2 = 0
    for index in range(len(list)):
        if list[index] > max :
            max2 = max
            max = list[index]
        elif max2 <= list[index] < max :
            max2 = list[index]
    return max,max2
print(max_andmin_value([11,22,21,10,6,7,8,9,100,98]))

#计算指定的年月日是这一年的第几天。
def is_leap(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0

def set_day():
    a = "2012年12月06日"
    month = (31,28,31,30,31,30,31,31,30,31,30,31)
    leap_month = (31,29,31,30,31,30,31,31,30,31,30,31)
    year = int(a[0:4])
    month_index = int(a[5:7])
    day = int(a[8:10])
    thday = 0
    if is_leap(year) :
        for index in range(month_index):
            thday += leap_month[index]
    else :
        for index in range(month_index):
            thday += month[index]
    return thday + day
#print(set_day(input("请输入年月日：")))
print(set_day())
'''
def joseph (num):
    people_num = [x for x in range(1, num+1)]
    count = 0
    i = 0
    while len(people_num) > 15:
        count += 1
        if count == 9:
            people_num.pop(i)
            i -= 1
            count = 0
        if i >= len(people_num) :
            i = 0
        i += 1
    return people_num
print(joseph(30))
