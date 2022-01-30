# -*- coding:utf-8 -*-
# display.py
# zhengyinloong
# 2022/1/26 21:06
"""display

该模块从TXT文件夹中按顺序读取txt文件，并输出到终端
"""
import os
import time

# 获取相关参数
from video2txt import Video2Txt


def showTxt(txt):
    with open(txt) as f:
        print(f.read())
        f.close()


def clear():
    i = os.system("cls")


def do():
    # 获取txt文件夹里所有文件的数量
    TXT_LIST = os.listdir(Video2Txt.TXT_FOLDER)  # 用该方法获取的列表顺序是打乱的，所以需要重置
    COUNT = len(TXT_LIST)
    # 重置 TXT_LIST
    TXT_LIST = list(map(lambda n: '%s/%d.txt' % (Video2Txt.TXT_FOLDER, n), list(range(1, COUNT + 1))))

    for txt in TXT_LIST:
        showTxt(txt)
        time.sleep(1 / Video2Txt.FPS)
        clear()


if __name__ == "__main__":
    do()
