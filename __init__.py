# -*- coding:utf-8 -*-
# __init__.py
# zhengyinloong
# 2022/1/27 11:21
"""
该包为视频文件转为字符画并可以在终端输出的加工包
"""


class Video2Txt:
    """
    该类用于初始化参数设置
    """
    # --------初始化参数设置----------- #
    # 注意：所有的路径最好不要有中文...
    # 视频文件
    VIDEO_NAME = 'video/video_default.mp4'
    # img文件要存放的文件夹
    IMG_FOLDER = 'imgs_default'  # 'imgs_default'
    # 保存图片的格式
    IMG_FORMAT = 'bmp'  # 'png' 'jpg'
    # 图片重新设置 宽 高
    IMG_WIDTH = 100
    IMG_HEIGHT = 100
    # 跳帧
    STEP = 10  # 默认每十帧取一帧

    # txt文件要存放的文件夹
    TXT_FOLDER = 'txts_default'
    # 灰度等级字符 #mn*+=-.
    GRAY_SCALE_STR = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`. '  # @%#*+=-:.

    # 转字符画时对图片缩放
    SCALE = 1.0
    # SCALE = 0.8
    # 根据cmd终端字符比例（属性->字体）调整字符画（宽/高）
    RATIO = 4 / 9

    # 播放帧率，请从原始视频文件属性中查找并修改,最好大一点，因为程序运行也需要时间
    FPS = 24
