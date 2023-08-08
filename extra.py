from ase.io import read,write
import random
import os
import sys
N=int(sys.argv[1])
strs=read("out.xyz",index=":")   #读入out.xyz包含很多frame
list=random.sample(range(0,len(strs)),N)   #产生N个不同的随机数, 用来随机抽取N个结构
os.system("if [ -f extra.xyz ]; then rm extra.xyz;fi") 
for i in list:
    write("extra.xyz",strs[i],append=True)
