# !/usr/bin/python3

# -*- coding: utf-8 -*-

# @Author   : Wu Jing

# @FILE     : lottery.py

# @Time     : 2019/7/13 13:57

# @Software : PyCharm


import random
import time


def _random():
    """系统产生随机六位数"""
    one = random.randint(0, 1)
    two = random.randint(0, 1)
    three = random.randint(0, 1)
    four = random.randint(0, 1)
    five = random.randint(0, 1)
    six = random.randint(0, 1)
    randomstr = str(one) + str(two) + str(three) + str(four) + str(five) + str(six)
    return randomstr


def main():

    """主函数"""
    print("欢迎来到双色球彩票系统！")
    while 1:
        lucknum = _random()
        start = input("开始游戏:【是】 退出游戏【否】:")
        if start == "是":
            print("游戏开始！")
            # money()  # money 函数用来计算金额 可购买彩票次数
            moneys = int(input("请输入您要充值的金额【存入金额为整数且为偶数】:"))
            times = moneys / 2
            print("您的余额为%d" % moneys)
            if times < 1:
                print("您的余额不足以购买一次彩票！")
                while 1:
                    chose = input("您可以选择【充值】或【退出】:")
                    if chose == "充值":
                        addmoney = int(input("请输入您要充值的金额:"))
                        moneys += addmoney
                        print("您的余额为%d:" % moneys)
                        times = moneys / 2
                        break
                    elif chose == "退出":
                        print("退出游戏中！")
                        time.sleep(2)
                        print("欢迎下次光临！")
                        return  # return 直接结束函数
                        # sys.exit()  # 执行该语句会直接退出程序
                    else:
                        print("输入错误!")
                    break
            print("您还可购买%d张彩票:" % times)  # TODO(Wu Jing) 购买彩票次数模块
            while 1:
                count = int(input("您想购买几张彩票:"))
                if count <= times:
                    print("您购买了%d 张彩票" % count)
                    break
                else:
                    print("您的余额不足以购买%d张彩票" % count)

            while 1:
                inputstr = input("输入六位数字 数字仅限于 【0】 和 【1】 如购买多张彩票请用空格分开:")

                inputstrlist = inputstr.split(" ")
                # print(len(inputstrlist))
                if len(inputstrlist) == count:

                    for i in range(len(inputstrlist)):
                        for j in range(6):
                            if (inputstrlist[i][j] == '0' or inputstrlist[i][j] == '1') and len(inputstrlist[i]) == 6:
                                pass
                            else:
                                print("输入错误，请重新输入！")
                                break
                    else:
                        print("输入正确！")
                        print(">>>正在抽奖中<<<")
                        time.sleep(2)
                        for k in range(len(inputstrlist)):
                            moneys = moneys - 2
                            if inputstrlist[k] == lucknum:
                                print("恭喜您中奖了!")
                                moneys += 100
                                print("您的余额为%d" % moneys)
                                print()
                            else:
                                print("很遗憾没有中奖!")
                                print("您的余额为%d" % moneys)
                                print()
                        print("本期号码为:", end="")
                        print(lucknum)
                        break  # 结束输入数字 while循环
                else:
                    print("输入无效！【输入彩票号码次数 超出购买彩票次数应输入的次数!】")
                    print("请重新", end="")
            a = input("是否继续游戏 【是】或【否】:")
            if a == "是":
                pass
            elif a == "否":
                print("欢迎下次光临!")
                break
        elif start == "否":
            print("退出游戏！")
            break
        else:
            print("输入错误！请重新输入！")


if __name__ == '__main__':
    main()
