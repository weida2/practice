import os

def f_keyword_l(f_path, keyword):
    f_list = os.listdir(f_path)

    for each in f_list:
        each_full_name = f_path + '\\' + each
        if os.path.isdir(each_full_name):
            f_keyword_l(each_full_name, keyword)

        elif each.endswith('.txt') and os.path.isfile(each_full_name):
            with open(each_full_name, 'r') as f_name:
                f_valid = 0
                lines_counts = 0
                for each_lines in f_name:
                    lines_counts += 1
                    keyword_counts = each_lines.count(keyword)
                    locs = list()
                    idx = 0
                    while keyword_counts != 0:
                        idx = each_lines.find(keyword, idx)
                        locs.append(idx)
                        idx += 1
                        keyword_counts -= 1
                    if len(locs) != 0:
                        f_valid = 1 if f_valid == 0 else 2

                        if f_valid == 1:
                            print('在文件【%s】中找到关键字【%s】' % (each_full_name, keyword))
                        print('关键字【%s】出现在第 %s行， 第【%s】的位置' % (keyword, lines_counts, locs))



f_keyword_l('E:\\视频', '玉子')



