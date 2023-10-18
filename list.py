# 列出来当前目录文件名称
import os
import sys
path  = 'D:/学习/研究生/定位/室内定位书'
dirs = os.listdir(path)
for file in dirs:
    print(file)