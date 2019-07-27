# !/usr/bin/python3

# -*- coding: utf-8 -*-

# @Author   : Wu Jing

# @FILE     : studentmanagementsystem.py

# @Time     : 2019/7/14 22:18

# @Software : PyCharm


import tools


"""
写一个学生管理系统
----------------------------------------------------------
                     欢迎进入学生管理系统                   
                                                          
  1.学生信息录入      2.学生成绩查询     3.查找学生信息      
  4.录入学生成绩      5.课程平均值     6.所有学生信息        
----------------------------------------------------------

"""


def main():
    """主函数"""
    while True:
        # 显示功能菜单
        tools.show_menu()
        action_str = input('\033[1;31m%s\033[0m' % '您希望选择执行的操作:')
        print('\033[1;31m%s\033[0m' % "您选择的操作是:【%s】" % action_str)

        # 针对名片的操作
        if action_str in ["1", "2", "3", "4", "5", "6"]:
            if action_str == "1":
                tools.informationinput_card()
            elif action_str == "2":
                tools.searchscore_card()
            elif action_str == "3":
                tools.searchinformation_card()
            elif action_str == "4":
                tools.addsocre_card()
            elif action_str == "5":
                tools.socrearrage_card()
            elif action_str == "6":
                tools.showallstudent_card()
        elif action_str == "0":
            print('\033[1;31m%s\033[0m' % "欢迎再次使用【名片管理系统】!")
            break

        pass


if __name__ == '__main__':
    main()
