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
'''
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end='')
    print("\n")


