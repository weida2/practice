import os
import easygui as eg

def function1():
    f_full_path = eg.fileopenbox(msg = None, title = None, default = '*.txt', filetypes = None, multiple = False)
    if f_full_path == None:
        eg.msgbox('未选中任何txt文件')
    else:
        f_obj = open(f_full_path, 'r')
        f_all_contxt = f_obj.read()
        f_obj.close()
        local_msg = '文本【%s】内容显示如下:' % (f_full_path.split(os.sep)[-1])
        local_title = '显示文件内容'
        f_new_context = eg.textbox(local_msg, local_title, f_all_contxt)
        if not f_new_context == None:
            if f_new_context == f_all_contxt:
                print('Match')
            else:
                w_msg = '检测到文件内容发生变化， 请选择以下操作'
                w_title = '警告'
                w_choice = ['覆盖保存', '放弃保存', '另存为...']
                choice = eg.choicebox(w_msg, w_title, w_choice, preselect = 0, callback = None, run = True)

                if choice == w_choice[0]:
                    f_obj = open(f_full_path, 'w')
                    f_obj.write(f_new_context[:-1])
                    f_obj.close()
                    eg.msgbox('文件覆盖完毕')

                elif choice == w_choice[1]:
                    pass

                elif choice == w_choice[2]:
                    new_f_name = eg.filesavebox(msg = None, title = '另存为', default = f_full_path.split(os.sep)[-1], filetypes = '.txt')
                    f_obj = open(new_f_name, 'w')
                    f_obj.write(f_new_context[:-1])
                    f_obj.close()
                    eg.msgbox('文件另存成功')




function1()