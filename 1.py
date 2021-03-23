def function1(*str):

    char3 = ' '
    for each in str:
        digit = 0
        alpha = 0
        space = 0
        other = 0
        for idx in range(0, len(each)):
            if each[idx].isdigit():
                digit += 1
            elif each[idx].isalpha():
                alpha += 1
            elif each[idx] in char3:
                space += 1
        other = len(each) - digit - alpha - space
        print('%s 有 %d个数字，%d个字母， %d 个空格， %d个其他字符' % (each, digit, alpha, space, other))

function1('sadas', 'dasasfaf456565{} dasfd')
