# video2txt

[TOC]

> - version : 1.0
> - author : ZhengYinloong
> - githubRep-url : [video2txt](https://github.com/zhengyinloong/video2txt)
> - requirements : cv2, os
> - environment : python3 on Windows10

## 简介

video2txt包由我原来一时兴起写的的ImgToTxt模块发展而来，经过多次完善，形成了由三个功能模块(captureImg.py, putTxt2File.py, display.py)，一个初始化文件(\__init__.py)和一个主程序执行文件(main.py)组成的比较完善的视频转字符画工具包。

## 各模块/文件功能概览

|             模块/文件             |                       功能                       |                        包含的类或函数                        |
| :-------------------------------: | :----------------------------------------------: | :----------------------------------------------------------: |
|   [\__init__.py](#__init__py)    |                    初始化参数                    |                       class：Video2Txt                       |
|  [captureImg.py](#captureimgpy)  |              提取视频帧并保存为图片              | function：capPosFrame(), captureImgs(), do(), frameResize(), getTotalFrames(), saveImg(), showPosFrame() |
| [putTxt2File.py](#puttxt2filepy) |  识别图片像素灰度并用字符代替，并存放在txt文件中  | function：do(), getOneRowChar(), getText(), gray2Char(), imgResize(), putTxt2File() |
|     [display.py](#displaypy)     |             将txt文件依次输出在终端              |              function：clear(), do(), showTxt()              |
|        [main.py](#mainpy)        | 包含一个do()函数，在终端使用do() |                        function：do()                        |

## 详细说明

### \__init__.py

该文件中定义了一个`Video2Txt`类用来初始化参数，包含以下属性：

| 属性           | 默认值                                                       | 说明                                                         |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| FPS            | 24                                                           | \< float ＞0 > txt文件“播放”的“帧率”                         |
| GRAY_SCALE_STR | r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`. ' | \< str > 灰度等级字符                                        |
| IMG_FOLDER     | 'imgs_default'                                               | \< str > img文件要存放的文件夹                               |
| IMG_FORMAT     | 'bmp'                                                        | \< str > 图片保存格式                                        |
| IMG_HEIGHT     | 100                                                          | \< int > 图片重新设置 高                                     |
| IMG_WIDTH      | 100                                                          | \< int > 图片重新设置 宽                                     |
| RATIO          | 4 / 9                                                        | \< float > 根据cmd终端字符比例（属性->字体）调整字符画（宽 / 高） |
| SCALE          | 1.0                                                          | \< float > 转字符画时对图片缩放                              |
| STEP           | 10                                                           | \< int > 跳帧，默认每十帧取一帧                              |
| TXT_FOLDER     | 'txts_default'                                               | \< str > txt文件要存放的文件夹                               |
| VIDEO_NAME     | 'video/video_default.mp4'                                    | \< str > 视频文件                                            |

### captureImg.py

该模块的功能是提取视频帧并保存为图片。

包含的函数：

- getTotalFrames()：获取视频总帧数。
- capPosFrame()：获取视频特定帧。
- frameResize()：重设获取到的帧宽和高。
- saveImg()：对cv2.imwrite()重新封装，将像素矩阵保存为图片。
- showPosFrame()：显示视频指定帧，默认彩色,不进行缩放。
- captureImgs()：获取并保存视频所有帧，当然也可以指定帧间隔。

###  putTxt2File.py

该模块功能是识别图片像素灰度并用字符代替，并存放在txt文件中。 

包含的函数：

- 

### display.py

该模块功能是将txt文件依次输出在终端。

包含的函数：

- do()：将txt文件依次输出在终端。引用该函数的程序需要直接在终端执行。

### main.py

包含一个do()函数，在终端执行该do()函数将直接输出转换成功的“字符画”视频（可能需要几分钟时间）

## 安装与使用

> 由于本人是在Windows10的python3环境下开发和应用的该工具包，其他环境本人没有条件实验😂

1. `安装前提`：先安装cv2包 `pip install opencv-python`

2. 安装好cv2后，直接下载或clone该仓库到你的设备上python解释器所在文件夹下 `Lib>site-packages` 中（如下图所示），即可在你的设备上任何IDE的.py文件中调用该包中任何模块、类和函数。

   <img src='./README.assets/image-20220131000208929.png' alt='安装'>

## BUG

该工具包目前有一个已知bug：

由于`captureImg.saveImg()`中调用了`cv2.imwrite()`函数，会出现内存中一直加载文件目录无法释放的问题，这会导致调用后无法对相关文件夹进行移动，重命名等操作。这个问题我也是在调试与使用中发现的，一直没有解决的办法😑，欢迎各位多多发pull request啊😀😀

[TOP](#video2txt)

