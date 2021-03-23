import easygui as eg

def function2():
    title = '账户中心'
    msg = '''
             【*真实姓名】为必填项
             【*E-mail】为必填项
             【*手机号码】为必填项
             
             '''
    inputs = ['*用户名', '*真实姓名', '电话号码', '*手机号码', 'QQ', '*E-mail']
    print(eg.multenterbox(msg, title, inputs))


function2()