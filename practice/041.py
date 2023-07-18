#请至少说出使用函数的两个显著优势？

#避免重复构筑相同代码，易复用易维护  //////避免代码重用，将不同功能的代码进行封装，分解，降低结构的复杂度 提高可读性

#1. 如果定义的函数不需要接收任何参数，可以不写小括号吗（像下面代码这样）？
'''def myfunc:
    pass'''
#不行
# 2.形参x，y实参a，b
# 3.否 会返回none值
'''def myfunc():
...     pass
...
>>> print(myfunc())
None'''
# 4。可以
# 5.会报错 不会调用funcb
# 6.想使用外界的变量可以使用global来改变全局变量 ////通过参数和返回值与外界沟通 隔离函数对外界的依赖
print("欢迎来到论坛")
def main():
    print("=====================\n1.注册 \n2.登录\n3.退出\n=====================\n请输入指令：")
    get_int(input())
def get_int(inp):
    if inp == '1':
        a = input("请输入用户名：")
        b = input("请输入密码：")
        register(encrypt(a),encrypt(b))
        main()
    elif inp == '2':
        a = input("请输入用户名：")
        b = input("请输入密码：")
        login(encrypt(a),encrypt(b))
    elif inp == '3':
        return
    else:
        print("输入的指令有误，请重新输入")
database = {}
def register(user,password):
    database[user] = password
    return database

def login(user,password):
    judge = 1
    while  judge:
        if database[user] == password:
            print("恭喜登陆成功")
            print(database[user])
            print(password)
            print(database[user] == password)
            judge = 0
            main()
        else:
            print("密码错误\n请重新输入密码:")
            password = encrypt(input("请输入密码："))

def encrypt(arg):
    return arg

main()