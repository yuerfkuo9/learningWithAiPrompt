#0. 请问下面变量 d 是一个字典吗？
'''d = {}
不是'''

#1. 字典中，同样一个值是否可以出现两次？
'''可以 键不可以出现两次一样的'''

#2. 请问下面代码创建的字典中，键和值分别是什么？
'''d = {}.fromkeys("吕布", 999)
吕999 布999'''

#3. 请问下面代码中，del d 这个语句，是单独删除 d 变量还是将 d 变量和其指定的字典一起干掉呢？
'''d = dict.fromkeys("Fish", 250)
del d
一起'''

#4. 请问下面创建字典的 8 种方法中，哪几种是正确的
'''>>> a = {99:"吕布", 90:"关羽", 60:"刘备"}
>>> b = dict(99:"吕布", 90:"关羽", 60:"刘备")
>>> c = dict(99="吕布", 90="关羽", 60="刘备")
>>> d = dict([(99, "吕布"), (90, "关羽"), (60, "刘备")])
>>> e = dict({99:"吕布", 90:"关羽", 60:"刘备"})
>>> f = dict({99="吕布", 90="关羽", 60="刘备"})
>>> h = dict({99:"吕布", 90:"关羽"}, 60="刘备")
>>> i = dict(zip([99, 90, 60], ["吕布","关羽","刘备"]))
a,c,d,f,i'''

#5. 请问下面代码执行之后，变量 b 中的内容是？
'''>>> a = {"小甲鱼":"You are my super star."}
>>> b = a
>>> a.clear()
{}'''

#1. 请编写一个电话簿程序
print("电话薄打开中.....")
tele_record = dict()
while True :
    inpu = input("请输入指令：（1.录入 / 2.查询 / 3.删除 / 4.打印 / 5.推出）:")
    print(inpu)
    print(type(inpu))
    print(inpu == 1)
    if inpu == '1' :
        print("录入模式-------")
        con = 1
        while con :
            name = input("请输入姓名：")
            if
            tele = input("请输入电话：")
            if tele == 
            tele_record[name] = tele
            decide = input("是否继续录入（Y/N）")
            if decide == "N" :
                break

    elif inpu == '2' :
        pass
    elif inpu == '3' :
        pass
    elif inpu == '4' :
        pass
    elif inpu == '5' :
        pass
    else :
        print("指令错误，请重新输入")