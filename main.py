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

for i in range(1,4):
    for j in range(1,i+1):
        print("*",end='')
    print("\n")

#斐波那契数列
a = 0
b = 1
for i in range(20):
    count += 1
    a , b = b , a + b
    print(a)

#一万以内的完美数
k = 0
while (k < 10000) :
    k += 1
    sum = 0
    for i in range(1,k-1):
        if k % i == 0 :
            sum += i
    if sum == k :
        print(k)

#一百以内所有素数
for i in range(2,101):
    wether = 1
    for j in range(2,i):
        if i % j == 0 :
            wether = 0
            break
    if wether == 1:
        print(i)

#实现计算求最大公约数和最小公倍数的函数。
def maxYueShu (a,b):
    yueShu = 0
    maxyue = 0
    if a > b :
        yueShu = a
    else :
        yueShu = b
    for i in range(1,yueShu+1):
        if a % i == 0 and b % i == 0 :
            maxyue = i
    return maxyue

def minBeiShu (a,b):
    maxYueS = a * b // maxYueShu(a,b)
    return maxYueS

print(maxYueShu(12,16))
print(type(minBeiShu(12,16)))
'''
#实现判断一个数是不是回文数的函数
def determine_reverse(origin):
    reverse_a = 0
    limit = origin
    while  limit > 0:
        reverse_a = reverse_a * 10 + limit % 10
        limit //= 10
    if reverse_a == origin:
        print("这个数是回文数")
        return True
    else:
        print("这个数不是回文数")
        return False


#实现判断一个数是不是素数的函数。
def determine_prime(value):
    for i in range(2, value):
        if value % i == 0:
            print("这个数不是素数")
            return False
    if value != 1:
        print("这个数是素数")
        return True
#写一个程序判断输入的正整数是不是回文素数
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if determine_reverse(num) and determine_reverse(num):
        print('%d是回文素数' % num)

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')