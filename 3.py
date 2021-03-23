def function1():

    save = dict()

    while True:
        string1 = """
                     |--- 新建用户：N/n ---|
                     |--- 登录账号：E/e ---|
                     |--- 退出程序：Q/q ---|
                     """;
        print(string1)
        n = input('请输入你要选择的服务:')

        if n == 'N' or n == 'n':
            name = input('请输入新建用户名:')
            while True:
                if not name in save:
                    pas  = input('请输入登录密码:')
                    save[name] = pas
                    print('注册成功， 赶紧登录试试^_^')
                    break
                else:
                    name = input('此用户名已被使用， 请重新输入:')

        elif n == 'E' or n == 'e':
            user = input('请输入登录的账户：')
            while True:
                if user in save:
                    user_pas = input('请输入登录密码:')
                    while True:
                        if user_pas == save[user]:
                            print('欢迎进入XXOO系统， 点击右上角x退出程序')
                            break
                        else:
                            user_pas = input('输入密码错误， 请重新输入:')
                    break
                else:
                    user = input('登录账户不存在， 请重新输入:')


        elif n == 'Q' or n == 'q':
            break




function1()
