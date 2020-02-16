import os
import pygame

chinese_dir = 'chinese'  # 存储图片的文件夹名字
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)
pygame.init()


def produceCharacter(codepoint):
    word = chr(codepoint)
    font = pygame.font.Font("msyh.ttc", 64)  # 复制找到的微软雅黑字体文件到工程文件夹即可 C:/Windows/Fonts
    rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, os.path.join(chinese_dir, word + ".png"))

    # Unicode 16进制码，重复的取一个


codepoint = [ 0x8d77, 0x767e, 0x5929, 0x5566]
for code in codepoint:
    produceCharacter(code)
