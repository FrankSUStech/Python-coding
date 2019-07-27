# !/usr/bin/python3

# -*- coding: utf-8 -*-

# @Author   : Wu Jing

# @FILE     : musicplay.py

# @Time     : 2019/7/19 20:35

# @Software : PyCharm
"""
音乐播放器
"""
import sys
import Day09.musicplay_tools as musicplay_tools


def welcome():
    """打印欢迎页面!"""
    print("*" * 70)
    print("\t\t\t\t\t\t\t欢迎来到音乐播放器!")
    print("*" * 70)


def select():
    print("*" * 70)
    print("\t\t1.播放\t\t\t\t\t\t\t\t\t\t\t2.停止\n\t\t3.下一曲"
          "\t\t\t\t\t\t\t\t\t\t\t4.上一曲\n\t\t5.增大音量\t\t\t\t\t\t\t\t\t\t6.减少音量\n\t\t0.退出")
    print("*" * 70)
    return input("请选择您要操作的选项:")


def judge_select():
    """判断输入的数字 选择对应的操作"""
    welcome()  # 调用欢迎界面模块
    index = 0
    path = r"C:\千锋\Notes\Day09\music"
    musiclist = musicplay_tools.getmusiclist(path)
    while True:
        inputnum = select()  # 打印操作说明的时候 同时接收输入的操作选项
        if inputnum == "0":
            print("已退出播放器！")
            sys.exit()  # 终止整个程序
        elif inputnum == "1":
            print("【播放】")
            musicplay_tools.playmusic(musiclist[index])
        elif inputnum == "2":
            musicplay_tools.pauseplay()
        elif inputnum == "3":
            print("【下一曲】")
            index = musicplay_tools.nextmusic(musiclist, index)
        elif inputnum == "4":
            print("【上一曲】")
            index = musicplay_tools.lastmusic(musiclist, index)
        elif inputnum == "5":
            musicplay_tools.turnup()
        elif inputnum == "6":
            musicplay_tools.turndown()
        else:
            choose = input("请重新输入 或 输入退出 退出播放器:")
            if choose == "退出":
                print("已退出播放器！")
                sys.exit()  # 终止整个程序


def main():
    """主函数"""
    judge_select()


if __name__ == '__main__':
    main()
