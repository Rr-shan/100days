import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import win32api
import win32con
import time


def up(x):
    win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)


def press(x):
    win32api.keybd_event(x, 0, 0, 0)


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
time.sleep(2)
threshold = 200
# imgfile = ["超.png", "宝.png", "宝.png", "和.png", "小.png", "扇.png", "子.png", "在.png", "一.png", "起.png", "一.png", "百.png",
           # "天.png", "啦.png"]
imgfile = [ "小.png",  "子.png", "在.png", "一.png", "天.png"]
for k in range(0, len(imgfile)):
    img = Image.open(imgfile[k]).convert('L')
    a_img = np.asarray(img, dtype="int64").copy()
    for i in range(0, a_img.shape[0]):
        for j in range(0, a_img.shape[1]):
            print(0 if a_img[i][j] < threshold else 1, end="")
        print()
    plt.imshow(img, cmap='gray')
