'''
Guoqing Xiong
2021.1.8
'''

import os
import random
import shutil
import numpy as np
import re

data = []

f = open(r'C:\Users\lenovo\Desktop\model_devi.out', "r")  # 读入文件路径
min = 0
max = 1
for line in f.readlines():  # 遍历每一行
    if "#" in line:  # 寻找带“#”字符的行
        pass
    else:
        str = ' '.join(line.split())
        new_str = str.split(' ')
        num = float(new_str[4])
        if min < num < max:
            index = new_str[0]
            new_num = [index, num]
            new_num = np.array(new_num)
            data.append(new_num)
data = random.sample(data, 5)
data = np.array(data)

file = r'C:\Users\lenovo\Desktop\tra'  # 文件夹路径
target = r'C:\Users\lenovo\Desktop\skk' # 存放文件的文件夹路径
for root, dirs, files in os.walk(file):
    for file in files:
        number = re.findall(r"\d+\.?\d*", file)  # 取出该行的数字
        a = ''.join(number)[:-1]
        if a in data[:, 0]:
            source = root + '\\' + file
            # print(source)
            newdir = os.makedirs(target+'\\'+file)
            new = target+'\\'+file + '\\' + file
            shutil.copyfile(source, new)
