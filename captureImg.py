# -*- coding:utf-8 -*-
# captureImg.py
# zhengyinloong
# 2022/1/26 22:17
"""captureImg

该模块提取video文件夹中的指定视频的每一帧，并保存在指定的IMG文件夹中
"""
import cv2

from video2txt import Video2Txt


def getTotalFrames(video_name):
    """
    获取视频总帧数

    :param video_name: 视频文件名（包括路径）
    :return: _count: float类型，视频总帧数
    """
    cap = cv2.VideoCapture(video_name)
    _count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    return _count


def capPosFrame(video_name, frame_number, frame_w=None, frame_h=None, isgray=True, ):
    """
    获取视频特定帧

    :param frame_h:
    :param frame_w:
    :param video_name: 视频文件名（包括路径）
    :param frame_number: 指定的某帧序号
    :param isgray: bool值，是否为灰度图,这里为了方便我将它默认为是
    :returns: ret,frame:
        ret: bool值，是否获取到指定帧
        frame: ndarry类型，图片矩阵
    """
    cap = cv2.VideoCapture(video_name)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    h = len(frame) if frame_h is None else (frame_h | 1)
    w = len(frame[0]) if frame_w is None else (frame_w | 1)
    frame = frameResize(frame, w, h)
    if isgray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return ret, frame


def frameResize(frame, width, height):
    frame = cv2.resize(frame, (width, height))
    return frame


def saveImg(file_name, img):
    """
    对cv2.imwrite()重新封装，将像素矩阵保存为图片

    :param file_name: 图片路径，如 imgs/1.bmp，图片原文件不存在则创建
    :param img: 图片矩阵 ,a numpy array
    :return: retval: bool值，图片保存成功则返回True
    """
    retval = cv2.imwrite(file_name, img)
    return retval


# saveImg拓展
def showPosFrame(winname, video_name, frame_number, last_time, isgary=False):
    """
    显示视频指定帧，默认彩色,不进行缩放

    :param isgary: 是否转为灰度图像
    :param winname: 窗口名称,String类型
    :param video_name: 视频文件名（包括路径）
    :param frame_number: 指定帧
    :param last_time: 显示持续时间 /ms , last_time=0,持续显示
    :return: none
    """
    ret, img = capPosFrame(video_name, frame_number, isgray=isgary)
    cv2.imshow(winname, img)
    cv2.waitKey(last_time)
    # cv2.destroyAllWindows()  # 对于想要在固定窗口播放连续帧的不太友好，可以最后加上
    return ret


def captureImgs(video_name, img_folder, img_formate, img_width=None, img_height=None, isgray=True, step=1):
    """

    :param video_name: 视频文件名（包括路径）
    :param img_folder: imgs要保存到的IMG文件夹
    :param img_formate: img的格式
    :param img_width: 重置图片宽度，不输入该参数则默认原视频帧宽
    :param img_height:
    :param isgray:
    :param step: 抽帧间隔，默认
    :return:
    """
    cap = cv2.VideoCapture(video_name)

    if cap.isOpened():
        FRAMES_COUNT = int(getTotalFrames(video_name))
        ret, frame = capPosFrame(video_name, 0, img_width, img_height, isgray)

        i = step
        while ret:
            ret = saveImg('%s/%d.%s' % (img_folder, i / step, img_formate), frame)
            if not ret:
                print('文件保存失败', i)
                return
            else:
                ret, frame = capPosFrame(video_name, i, img_width, img_height, isgray)
                if i >= FRAMES_COUNT - step:
                    print('获取视频帧完成，共%d项' % int(i / step))
                    return
                i += step
    else:
        print('读取视频失败')


def do():
    captureImgs(Video2Txt.VIDEO_NAME, Video2Txt.IMG_FOLDER, Video2Txt.IMG_FORMAT,
                isgray=True, step=Video2Txt.STEP)
    # captureImgs(Video2Txt.VIDEO_NAME, Video2Txt.IMG_FOLDER, Video2Txt.IMG_FORMAT, Video2Txt.IMG_WIDTH,
    #             Video2Txt.IMG_HEIGHT, isgray=True, step=30)


if __name__ == "__main__":
    do()
