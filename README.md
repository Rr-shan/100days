## 思路
-  得到汉字点阵，转化成二维数组，得到图片像素点的信息，方便做按键映射（知道什么时候敲下哪个按键）
-  完成键盘的键值对（类似ASCII码和字母）数组的构建，模拟敲击键盘（要不然人的手可敲不来）
键盘各键对应键值
-  上面网站钢琴按键的瀑布流，可以用按下的时间长度来控制其形状，若比较短促，则可以形成矩形像素点

## 操作
1. 生成汉字图像
    1. utf-8 这个轮子来自博客https://blog.csdn.net/johinieli/article/details/76151247
    2. 想要什么字可以上这个网站找到Unicode码
http://www.dwenzhao.cn/cal/php/gbkunicode.php

2. 转化成二维数组，这里用到了一个图片二值化的操作
即：将图片转化为黑白图片，且是非黑即白，所以称为二值。黑：0 白：255 光亮度，这样可以丢弃颜色细节，方便映射到钢琴按键的按与不按两种状态
```python
threshold = 200 #用于对汉字图片进行简单二值化的阈值设置，小于则认为是黑色，大于则认为是白色
imgfile=["超.png", "宝.png", "宝.png", "和.png", "小.png", "扇.png", "子.png", "在.png", "一.png", "起.png", "一.png", "百.png",
           "天.png", "啦.png"]
for k in range(0,len(imgfile)):
    img = Image.open(imgfile[k]).convert('L')#调用函数，汉字图片转成灰度图
    a_img = np.asarray(img,dtype="int64").copy()#调用函数，得到灰度图的像素矩阵
```

3. 键盘的键值对（类似ASCII码和字母）数组的构建
```python
 tune = np.array([
     192, 49, 50, 51, 52, 53, 54, 55,
     56, 57, 48, 189, 187, 8, 81, 87,
     69, 82, 84, 89, 85, 73, 79, 80,
     219, 221, 220, 65, 83, 68, 70, 71,
     72, 74, 75, 76, 186, 222, 90, 88,
     67, 86, 66, 78, 77, 188, 190, 191,
     32, 38, 37, 40, 39, 111, 106, 109,
     103, 104, 105, 107, 100, 101, 102, 97,
 ], dtype="int64")      
```
百度文库提供的： https://wenku.baidu.com/view/08ae2600cc17552707220853.html
PianoCharacter.xkmp 放到网站上


ps: 二值化操作更好理解 ，pstest去测试一下
```python
 import matplotlib.pyplot as plt
 threshold = 200 #用于对汉字图片进行简单二值化的阈值设置，小于则认为是黑色，大于则认为是白色
 imgfile=[  "百.png",
           "天.png", "啦.png"]
 for k in range(0,len(imgfile)):
     img = Image.open(imgfile[k]).convert('L')#调用函数，汉字图片转成灰度图
     a_img = np.asarray(img,dtype="int64").copy()#调用函数，得到灰度图的像素矩阵
     for i in range(0, a_img.shape[0]):#得到灰度图的像素矩阵，实际上取值为0-255
         for j in range(0, a_img.shape[1]):
             print(0 if a_img[i][j] < threshold else 1, end="")#二值化打印，未作实际的二值化
         print()
     plt.imshow(img, cmap='gray')#展示汉字灰度图
```
灵感来自同学的说说