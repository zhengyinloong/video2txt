# -*- coding:utf-8 -*-
# putTxt2File.py
# zhengyinloong
# 2022/1/26 18:42
"""putTxt2File

该模块将指定的IMG文件夹中的所有图片转化为字符画，并保存在指定的TXT文件夹中
"""
import os
import cv2
# 获取相关参数
from video2txt import Video2Txt


def imgResize(_img, scale, ratio):
    w = int(_img.shape[1] * scale)
    h = int(_img.shape[0] * scale * ratio)
    _img = cv2.resize(_img, (w, h))
    return _img


def gray2Char(gray, gray_scale_str):
    gs = len(gray_scale_str)
    lv = gray * gs // 255
    if lv < gs:
        char = gray_scale_str[lv]
    else:
        char = gray_scale_str[lv - 1]

    return char


def getOneRowChar(oneRowGray, gray_scale_str):
    oneRowChar = list(map(lambda gray: gray2Char(gray, gray_scale_str), oneRowGray))
    return oneRowChar


def getText(img_name, scale, ratio, gray_scale_str):
    """
    获取图像灰度矩阵对应的字符矩阵
    """
    img_gray = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

    img_gray = imgResize(img_gray, scale, ratio)

    _text = list(map(lambda oneRowGray: getOneRowChar(oneRowGray, gray_scale_str), img_gray))

    return _text


def putTxt2File(txt, file_name):
    """
    将得到的text像素矩阵写入文件，分行

    :param txt: 得到的txt像素二维矩阵
    :param file_name: txt文件名（没有则创建，存在则覆盖原内容），包含路径和扩展名，如 txts/1.txt
    :return: none
    """
    with open(file_name, 'w') as f:
        for row in txt:
            for char in row:
                f.write(char)
            f.write('\n')
        f.close()


def do():
    # 获取图片文件夹里图片列表和数量
    IMG_LIST = os.listdir(Video2Txt.IMG_FOLDER)  # 用该方法获取的列表顺序是打乱的，所以需要重置
    COUNT = len(IMG_LIST)
    # 重置 IMG_LIST
    IMG_LIST = list(
        map(lambda n: '%s/%d.%s' % (Video2Txt.IMG_FOLDER, n, Video2Txt.IMG_FORMAT), list(range(1, COUNT + 1))))

    i = 1
    for img in IMG_LIST:
        text = getText(img, scale=Video2Txt.SCALE, ratio=Video2Txt.RATIO, gray_scale_str=Video2Txt.GRAY_SCALE_STR)
        putTxt2File(text, '%s/%d.txt' % (Video2Txt.TXT_FOLDER, i))
        i += 1
    print('图片转字符画完成，共%d项，%s' % (COUNT, Video2Txt.TXT_FOLDER))


# text = getText('imgs/doraemon.png',scale=SCALE/2,ratio=RATIO)
# putTxt2File(text,'TXT/test.txt')
if __name__ == "__main__":
    do()
