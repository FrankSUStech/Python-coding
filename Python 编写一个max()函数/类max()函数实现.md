#  在python中写一个类似于max()的函数
***设计一个函数，完成max()函数功能传递1个，必须可迭代对象，返回可迭代对象中的最大值若传递多个，必须number或str ，返回最大值***

```python
from collections.abc import Iterable


def max_(*args):
    """类似于max()函数功能

    :param args:传入的参数 可以是 list tuple str number
    :return:最大值
    """
    # 只有一个元素,并且这个元素为可迭代对象 isinstance(args[0], Iterable) 检查是否为可迭代对象
    if len(args) == 1 and isinstance(args[0], Iterable) and len(args[0]) > 0:
        maxnum = list(args[0])[0]
        for x in range(len(args[0])):
            if args[0][x] > maxnum:
                maxnum = args[0][x]
        return maxnum
    elif len(args) > 1:
        maxnum = args[0]
        for x in args:
            if x > maxnum:
                maxnum = x
        return maxnum


def main():
    """主函数"""
    # 传递多个参数
    print(max_(1, 2, 33))
    print(max_("d", "c", "b", "a"))
    # 传递可迭代对象
    print(max_(["1", "2"]))
    print(max_(["1", "2"]))


if __name__ == '__main__':
    main()

```

