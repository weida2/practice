import  easygui as eg
import  random as rd

def function():
    guess = rd.randint(1,10)
    while True:
        str_input = eg.enterbox('不妨猜猜小甲鱼心中想的数字(1~10)', '数字小游戏')
        if str_input.isdecimal():
            input_num = int(str_input)
            if input_num == guess:
                eg.msgbox('猜对了，但没什么奖励', 'haha')
                break
            elif input_num > guess:
                eg.msgbox('猜大了，不妨调小试试', 'chungou')
                continue
            elif input_num < guess:
                eg.msgbox('猜小了，不妨调大试试', 'hahah')
                continue
        else:
            eg.msgbox('输入的类型不正确', 'fw')
            continue


function()