# -*- coding:utf-8 -*-
# main.py
# YINLONG_ZHENG
# 2022/1/27 13:27
"""main
初始化参数后在cmd运行该程序将直接达到目的（可能需要几分钟时间转化）
"""
# 导入各个模块
import captureImg
import display
import putTxt2File


def do():
    captureImg.do()
    putTxt2File.do()
    display.do()


if __name__ == "__main__":
    do()
