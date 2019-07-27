# python 歌词解析器
#### 前言
*歌词解析器，顾名思义就是在播放歌曲的时候，音乐播放器放到那一句就显示对应的歌词。*
*在 python中歌词解析器并不难写，运用 time模块来编写歌词解析器， time.sleep()函数推迟调用线程的运行，进而可以控制歌词的播放。为了在播放歌词的同时播放音乐，需要导入 pygame 模块。

> https://baike.baidu.com/item/Pygame/7707076?fr=aladdin 安装 pip install pygame

*
#### 实现步骤
![歌词解析器步骤图](https://img-blog.csdnimg.cn/20190726205039156.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjg1Njg3MQ==,size_16,color_FFFFFF,t_70)
##### 获取歌词字典函数
首先用 import 关键字导入 time 模块和 pygame 模块，我们需要用到 time模块中的sleep()函数

```python
import time
import pygame
```
定义一个函数来后去歌词词典，参数为歌词字符串，通过函数返回歌词字典。

```python
def get_music_dict(musiclrc):
    """获得歌词字典

    :param musiclrc: 歌词字符串
    :return: 时间与歌词对应的字典
    """
    dictmusic = {}  # 创建一个空字典，用来装 时间(key) 和 歌词(value)
    listline1 = musiclrc.splitlines()  # 安照行进行切割 把每一行变成列表的一个元素

    for i in listline1:  # 把每一行元素遍历出来，准备切割

        listline2 = i.split("]")  # 以 ] 为切割符
        value = listline2[-1]  # 每一次遍历 把歌词元素(每一次遍历都是最后一个) 赋值给 value

        for j in range(len(listline2)-1):  # 遍历 listLine2  len(listLine2)-1 除去最后的非时间字符串(歌词)

            keymusic = listline2[j][1:]  # [1:]从索引值为1开始取目的是除去 [
            # keymusic = listline2[j].strip()[1:]  # [1:]从索引值为1开始取目的是除去 [ 如果有缩进的话 需要用strip()去除空格  方案二

            keytime = keymusic.split(":")  # 对遍历的的时间字符串以冒号进行切割

            musictime = float(keytime[0])*60+float(keytime[1])  # 计算出每个时间的总秒数

            key = musictime  # 把时间赋值给字典中的 key

            dictmusic[key] = value  # 把value 赋值给对应的时间 key
    # print(dictmusic)

    return dictmusic
```

##### 打印输出歌词
获取歌词字典之后，如何打印歌词是最关键的。先将字典中所有的时间放入到一个列表中——时间列表，将时间列表进行升序排序，遍历时间列表，将时间列表里的值传入time.sleep()函数，从而达到控制在什么时间打印歌词。

```python
def print_music_dict(dictmusic):
    """打印输出歌词

    :param dictmusic:时间与歌词对应的字典
    """
    listmuscitime = []  # 创建空列表,把字典的key写进去
    for keys in dictmusic.keys():
        listmuscitime.append(keys)
    listmuscitime.sort()  # 默认对列表进行升序
    time.sleep(listmuscitime[0])
    for index in range(len(listmuscitime)):
        if index > 0:
            time.sleep((listmuscitime[index]-listmuscitime[index-1]))  # 两段歌词之间的时间
            print(dictmusic.get(listmuscitime[index]))  # 对列表里面的key值下标遍历,进而用get取字典的value


```
##### 主函数


```python
def main():
    """主函数"""
    musiclrc = '''
[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]    
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
    '''
    pygame.mixer.init()  # 初始化音频部分 
    path = r"chuanqi.mp3"  # 音频绝对地址
    pygame.mixer.music.load(path) 
    pygame.mixer.music.play()

    print_one_by_one("开始播放音乐！")


    get_music_dict(musiclrc)
    dictmusic = get_music_dict(musiclrc)
    print_music_dict(dictmusic)
    time.sleep(300)


if __name__ == '__main__':
    main()


```

