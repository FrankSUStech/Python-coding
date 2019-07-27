# !/usr/bin/python3

# -*- coding: utf-8 -*-

# @Author   : Wu Jing

# @FILE     : tools.py

# @Time     : 2019/7/14 22:30

# @Software : PyCharm

# 记录所有信息的字典列表
card_list = []


def show_menu():
    """显示菜单模块"""
    print('\033[1;31m%s\033[0m' % "*" * 65)
    # print('\033[1;31m%s\033[0m' % '\t\t\t\t【欢迎来到学生管理系统】\n')
    # print('\033[1;31m%s\033[0m' % '【1】.学生信息录入')
    # print('\033[1;31m%s\033[0m' % '【2】.学生成绩查询')
    # print('\033[1;31m%s\033[0m' % '【3】.查找学生信息')
    # print('\033[1;31m%s\033[0m' % '【4】.录入学生成绩')
    # print('\033[1;31m%s\033[0m' % '【5】.课程成绩平均值')
    # print('\033[1;31m%s\033[0m' % '【6】.所有学生信息')
    # print('\033[1;31m%s\033[0m' % '【0】.退出系统')
    print('\033[1;31m%s\033[0m' % '''----------------------------------------------------------
|                    欢迎进入学生管理系统                  　 |
|                                                         |
| 1.学生信息录入      2.学生成绩查询     3.查找学生信息   　　　　|
| 4.录入学生成绩      5.课程平均值     　6.所有学生信息    　    |
| 0.退出系统
----------------------------------------------------------''')


def informationinput_card():
    """学生信息录入"""
    print('\033[1;31m%s\033[0m' % '-' * 65)
    print('\033[1;31m%s\033[0m' % '【学生信息录入】')

    # 1.提示输入学生信息的详细内容
    name = input('\033[1;31m%s\033[0m' % '请输入学生的姓名:')
    phone = input('\033[1;31m%s\033[0m' % '请输入学生的电话号码:')
    ch_score = input('\033[1;31m%s\033[0m' % '请输入学生的语文成绩:')
    math_score = input('\033[1;31m%s\033[0m' % '请输入学生的数学成绩:')
    en_score = input('\033[1;31m%s\033[0m' % '请输入学生的英语成绩:')

    # 2.使用输入的学生信息 放入一个信息字典中
    card_dict = {
        "姓名": name,
        "电话": phone,
        "语文成绩": ch_score,
        "数学成绩": math_score,
        "英语成绩": en_score
    }

    # 3.将信息字典添加到列表中
    card_list.append(card_dict)

    # 4.提示学生信息添加成功
    print('\033[1;31m%s\033[0m' % '添加 %s 的信息成功!' % name)


def searchscore_card():
    """学生成绩查询"""
    print('\033[1;31m%s\033[0m' % '-' * 65)
    print('\033[1;31m%s\033[0m' % '【学生成绩查询】')
    find_name = input('\033[1;31m%s\033[0m' % '请输入要搜索的学生姓名:')
    for card_dict in card_list:
        if card_dict["姓名"] == find_name:
            print('\033[1;31m%s\033[0m' % "姓名\t\t\t语文成绩\t\t\t数学成绩\t\t\t英语成绩")
            print('\033[1;31m%s\033[0m' % "=" * 65)
            print('\033[1;31m%s\033[0m' % "%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["姓名"],
                                                                          card_dict["语文成绩"],
                                                                          card_dict["数学成绩"],
                                                                          card_dict["英语成绩"]))
        break
    else:
        print('\033[1;31m%s\033[0m' % "抱歉，没有找到%s" % find_name)


def searchinformation_card():
    """查找学生信息"""
    print('\033[1;31m%s\033[0m' % '-' * 65)
    print('\033[1;31m%s\033[0m' % '搜索学生信息')
    find_name = input('\033[1;31m%s\033[0m' % '请输入要搜索的姓名:')
    for card_dict in card_list:
        if card_dict["姓名"] == find_name:

            print('\033[1;31m%s\033[0m' % "找到了！")
            print()
            print('\033[1;31m%s\033[0m' % "姓名\t\t\t电话\t\t\t语文成绩\t\t\t数学成绩\t\t\t英语成绩")
            print('\033[1;31m%s\033[0m' % "=" * 65)
            print('\033[1;31m%s\033[0m' % "%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["姓名"],
                                                                                  card_dict["电话"],
                                                                                  card_dict["语文成绩"],
                                                                                  card_dict["数学成绩"],
                                                                                  card_dict["英语成绩"]))
            # 针对找到的名片记录执行修改和删除的操作
            # deal_card(card_dict)
            break
        else:
            print("抱歉，没有找到%s" % find_name)


def addsocre_card():
    """录入学生信息"""
    print('\033[1;31m%s\033[0m' % "-" * 65)
    print('\033[1;31m%s\033[0m' % "录入学生信息!")
    find_name = input('\033[1;31m%s\033[0m' % '请输入的录入信息的学生姓名:')
    for card_dict in card_list:
        if card_dict["姓名"] == find_name:
            card_dict["语文成绩"] = input('\033[1;31m%s\033[0m' % "请该学生的输入语文成绩:")
            card_dict["数学成绩"] = input('\033[1;31m%s\033[0m' % "请该学生的输入数学成绩:")
            card_dict["英语成绩"] = input('\033[1;31m%s\033[0m' % "请该学生的输入英语成绩:")
            break
    print("%s的学生成绩录入成功！" % find_name)


def socrearrage_card():
    """课程平均值"""
    print('\033[1;31m%s\033[0m' % "-" * 65)
    print('\033[1;31m%s\033[0m' % "查询课程平均值!")
    find_name = input('\033[1;31m%s\033[0m' % '请输入要搜索的姓名:')
    for card_dict in card_list:
        if card_dict["姓名"] == find_name:

            print('\033[1;31m%s\033[0m' % "找到了！")
            print()
            print('\033[1;31m%s\033[0m' % "姓名\t\t\t平均成绩")
            print('\033[1;31m%s\033[0m' % "=" * 65)
            print('\033[1;31m%s\033[0m' % "%s\t\t\t%d" % (card_dict["姓名"], int(eval(card_dict["语文成绩"])
                                                                               + eval(card_dict["数学成绩"])
                                                                               + eval(card_dict["英语成绩"]))/3))
            break
        else:
            print("抱歉，没有找到%s" % find_name)


def showallstudent_card():
    """所有学生信息"""
    print('\033[1;31m%s\033[0m' % "-" * 65)
    print('\033[1;31m%s\033[0m' % "显示所有学生的信息")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print('\033[1;31m%s\033[0m' % "当前没有记录任何学生的信息！")
        # return 可以返回一个函数的结果
        # 下方的代码不会被执行
        # 如果return后面没有任何内容，表示会返回到调用函数的位置
        # 可以不返回任何结果
        return
    # 打印表头
    for name in ["姓名", "电话", "语文成绩", "数学成绩", "英语成绩"]:
        print('\033[1;31m%s\033[0m' % name, end="\t\t\t")
    print("")
    # 打印分割线
    print('\033[1;31m%s\033[0m' % "=" * 65)
    # 遍历名片列表依次输出字典
    for card_dict in card_list:
        print('\033[1;31m%s\033[0m' % "%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["姓名"],
                                                                              card_dict["电话"],
                                                                              card_dict["语文成绩"],
                                                                              card_dict["数学成绩"],
                                                                              card_dict["英语成绩"]))
