# 如何用Python来开发一个ATM系统
*python 有着易于阅读，易于维护的特点，有丰富的第三方库。用一门语言来开发ATM系统并不简单，但是当你用上了有着丰富的第三方库的python的时候，也许你可以从容面对。*
## 分析系统蓝图
开发一个ATM系统是面向用户的，我们首先将这个ATM系统跟用户的关系表现出来。首先我们画出用例图。
![ATM用例图](https://img-blog.csdnimg.cn/20190805201043711.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjg1Njg3MQ==,size_16,color_FFFFFF,t_70)
这个时候我们把思维理顺了，可以开始写代码了。
##### 我们先定义一个用户类
*用户类来记录用户的姓名、身份证号、电话号码、银行卡*

```python
class User:

    def __init__(self, name, idcard, phonenum, card):
        self.name = name
        self.idcard = idcard
        self.phonenum = phonenum
        self.card = card

```
##### 然后定义一个卡类
*卡类是用来记录银行卡的卡号、密码、存储的金额、是否被冻结的状态*

```python
class Card:
    def __init__(self, cardnum, password, money, islock=False):
        self.cardnum = cardnum
        self.password = password
        self.money = money
        self.islock = islock
```

*完成了用户和银行卡的类定义，我们还只是完成了一小步。*
##### 定义一个ATM类
*我们几乎所有的事情要在ATM类中完成，登陆、开户、查询、取款等等，这些都要在ATM中完成，所以编写ATM类这是非常重要也是最难写的。不过也不要着急，我们一步一步来完善ATM的功能。*

**首先我们导入用户模块和银行卡模块，还有随机数模块，我们要用它来生成用户的银行卡号。**
```python
import random
import time
from card import Card
from user import User
```
**然后把类的大致框架写出来，定义一个用来存储所有信息的字典。**

```python
class ATM:

    userDict = dict()
    islogin = None
```
**ATM系统欢迎界面很容易写出来**

```python
@staticmethod
def welcome():
    print('''
       **********************
       *                    *
       *  welcome to bank   *
       *                    *
       **********************
       ''')

@staticmethod
def select():
    print('''
       **********************
       *  1.登陆   2.开户    *
       *  3.查询   4.取款    *
       *  5.存款   0.退出    *
       *  6.转账   7.改密    *
       *  8.锁卡   9.解锁    *
       **********************
       ''')
    num = input("请选择服务项目：")
    return num
```
**定义函数来获取银行卡的卡号，银行卡的卡号是随机的**

```python
@classmethod
def getcardnum(cls):
    while True:
        cardnum = str()
        for x in range(6):
            cardnum += str(random.randrange(0, 10))
        if cardnum not in cls.userDict:
            return cardnum
```
**如果是新用户的话，需要开户**

```python
@classmethod  
def openuser(cls):
    name = input("请输入您的姓名:")
    idcard = input("请输入您的身份证号码:")
    phonenum = input("请输入您的电话号码:")
    psd = input("请设置您的密码:")
    psd2 = input("请确认您的密码:")
    if psd == psd2:
        money = int(input("请输入您的预存金额:"))
        if money > 0:
            cardnum = cls.getcardnum()
            card = Card(cardnum, psd, money)
            user = User(name, idcard, phonenum, card)
            cls.userDict[cardnum] = user
            print("开卡成功!您的卡号为%s,请牢记..." % cardnum)
        else:
            print("预存金额非法，开卡失败！")

    else:
        print("两次输入密码不一致，开卡失败！")
```
**登录函数，这里要注意在开始输入卡号之后，要先判断此卡号是否已经被冻结。如果已经冻结，则无法登录。登录成功，在这里就要把我们定义的islogin赋值为True,因为查询、取款、存款、转账、改密操作我们要先判断是否已经登录。**

```python
@classmethod
def login(cls):
    cardnum = input("请输入你的卡号:")
    user = cls.userDict.get(cardnum)

    if user:
        if user.card.islock:
            print("您的卡片已经被锁！")
            return

        else:
            a = 0
            while a < 3:
                psd = input("请输入您的密码:")
                if psd == user.card.password:
                    print("登陆成功!")
                    cls.islogin = cardnum
                    break
                else:
                    print("密码错误，登陆失败!")
                    a += 1
            if a == 3:
                user.card.islock = True
                print("您的卡片已经被冻结！")
    else:
        print("卡号不存在")
```
**查询**

```python
@classmethod
def search(cls):
    if cls.islogin:
        print("您当前的余额为%d元" % cls.userDict.get(cls.islogin).card.money)
    else:
        print("请登录后查询！")
```
**取款**

```python
@classmethod
def withdrawals(cls):
    if cls.islogin:
        print("您当前的余额为%d元" % cls.userDict.get(cls.islogin).card.money)
        rmoney = int(input("输入您想提取的金额:"))
        if rmoney <= cls.userDict.get(cls.islogin).card.money:
            cls.userDict.get(cls.islogin).card.money -= rmoney
            print("取款中，请稍后...")
            time.sleep(1)
            print("成功提取%d元!" % rmoney)
            print("您当前的余额为%d元!" % cls.userDict.get(cls.islogin).card.money)
            return
        else:
            print("您的余额不足%d元,请重新输入!" % rmoney)
    else:
        print("请登录后取款！")
```
**存款**

```python
@classmethod
def deposit(cls):
    if cls.islogin:
        addmoney = int(input("请您放入钞票:"))
        cls.userDict.get(cls.islogin).card.money += addmoney
        print("存款中，请稍后...")
        print("您本次存入的金额为:%d元" % addmoney)
        print("您的余额为%d元" % cls.userDict.get(cls.islogin).card.money)
    else:
        print("请登录后存款！")
```
**更改密码**

```python
@classmethod
def changepassword(cls):
    if cls.islogin:
        newpsd1 = input("请输入您的新密码:")
        newpsd2 = input("请再次输入您的新密码:")
        if newpsd1 == newpsd2:
            cls.userDict.get(cls.islogin).card.password = newpsd2
            print("更改密码成功！")
        else:
            print("两次输入密码不一致，更改密码失败！")
    else:
        print("您还未登录，请登陆后更改密码！")
```
**冻结银行卡**

```python
@classmethod
def lock(cls):
    if cls.islogin:
        cls.userDict.get(cls.islogin).card.islock = True
        print("您的卡片已经成功冻结!")
        cls.islogin = None

    else:
        print("您还未登录，请登陆后进行操作！")
```
**解冻银行卡**

```python
@classmethod
def unlock(cls):
    cardnum = input("请输入你的卡号:")
    user = cls.userDict.get(cardnum)
    if user:
        psd = input("请输入您的密码:")
        if psd == user.card.password:
            user.card.islock = False
            print("卡片解锁成功!")
            cls.islogin = cardnum
        else:
            print("密码错误，登陆失败!")
    else:
        print("卡号不存在")

```
**转账**

```python
@classmethod
def transfer(cls):
    if cls.islogin:
        receive = input("请输入接受账号:")
        a = cls.userDict.get(receive)
        if a:
            tmoney = int(input("请输入您转账的金额:"))
            if tmoney <= cls.userDict.get(cls.islogin).card.money:
                cls.userDict.get(cls.islogin).card.money -= tmoney
                cls.userDict.get(receive).card.money += tmoney
                print("成功转账%d元到%s" % (tmoney, receive))
            else:
                print("您的余额不足%d元！" % tmoney)

        else:
            print("账号不存在！")
    else:
        print("您还未登陆，请登录后进行操作！")
```
**好了，到这里ATM系统基本完成了。只要调用ATM类就可以完成所有操作。**

```python
from atm import ATM
import time
import json
from card import Card
from user import User


def main():
    ATM.welcome()

    while True:
        time.sleep(0.2)
        num = ATM.select()
        if num == '1':
            print("登陆！")
            ATM.login()
        elif num == '2':
            print("开户！")
            ATM.openuser()
        elif num == '3':
            print("查询!")
            ATM.search()
        elif num == '4':
            print("取款！")
            ATM.withdrawals()
        elif num == '5':
            print("存款！")
            ATM.deposit()
        elif num == '6':
            print("转账！")
            ATM.transfer()
        elif num == '7':
            print("更改密码！")
            ATM.changepassword()
        elif num == '8':
            print("冻结卡片！")
            ATM.lock()
        elif num == '9':
            print("解冻卡片")
            ATM.unlock()
        elif num == '0':
            print("已退出！")
            print("请及时取走您的卡片！")
                    break
        else:
            print("选择有误，请重新输入！")


if __name__ == '__main__':
    main()
```
**但是我们并不只限于此，ATM系统虽然可以实习所有的操作，但是如果我们退出系统之后，数据去没有保存下来。因此，需要将数据序列化保存到磁盘中，同样，也需要将磁盘中的数据反序列化变成对象。**

```python
from atm import ATM
import time
import json
from card import Card
from user import User


def user2dict(user):
    """序列化"""
    return {'name': user.name,
            'idcard': user.idcard,
            'phonenum': user.phonenum,
            'card': {'cardnum': user.card.cardnum,
                     'password': user.card.password,
                     'money': user.card.money,
                     'islock': user.card.islock}}


def dict2user(d):
    """反序列化"""
    return User(d['name'],
                d['idcard'],
                d['phonenum'],
                Card(d['card']['cardnum'],
                     d['card']['password'],
                     d['card']['money'],
                     d['card']['islock']))


def main():
    ATM.welcome()
    # noinspection PyBroadException
    try:
        # with open('use.txt', 'rb') as f:
        #     ATM.userDict = pickle.load(f)
        with open('use.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                userdict = json.loads(line)
                user = dict2user(userdict)
                ATM.userDict[user.card.cardnum] = user
    except BaseException:
        pass
    while True:
        time.sleep(0.2)
        num = ATM.select()
        if num == '1':
            print("登陆！")
            ATM.login()
        elif num == '2':
            print("开户！")
            ATM.openuser()
        elif num == '3':
            print("查询!")
            ATM.search()
        elif num == '4':
            print("取款！")
            ATM.withdrawals()
        elif num == '5':
            print("存款！")
            ATM.deposit()
        elif num == '6':
            print("转账！")
            ATM.transfer()
        elif num == '7':
            print("更改密码！")
            ATM.changepassword()
        elif num == '8':
            print("冻结卡片！")
            ATM.lock()
        elif num == '9':
            print("解冻卡片")
            ATM.unlock()
        elif num == '0':
            print("已退出！")
            print("请及时取走您的卡片！")
            with open('use.txt', 'w', encoding='utf-8') as f2:
                for user in ATM.userDict.values():
                    userstr = json.dumps(user, default=user2dict)
                    f2.write(userstr+'\n')
            break
        else:
            print("选择有误，请重新输入！")


if __name__ == '__main__':
    main()
```
#### 接下来看一下最终得成果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190806190538610.gif)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190806190557336.gif)
