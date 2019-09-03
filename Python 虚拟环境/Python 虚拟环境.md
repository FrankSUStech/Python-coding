
# 虚拟环境-windows

## virtualenv的概述

> virtualenv是用来创建Python的虚拟环境的库，虚拟环境能够独立于真实环境存在，
> 并且可以同时有多个互相独立的Python虚拟环境，每个虚拟环境都可以营造一个干净
> 的开发环境，对于项目的依赖、版本的控制有着非常重要的作用。
>
> 虚拟环境有什么意义？
> 	如果我们要同时开发多个应用程序，应用A需要Django1.11，而应用B需Django1.8怎么办？
> 	这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。
> 	virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。



## virtualenv的安装和使用

### 安装和创建virtualenv

#### 安装虚拟环境

​	安装virtualenv跟安装一般的Python库是一样的操作，直接使用pip命令就行了：

```ini
pip install virtualenv
```

#### 创建虚拟环境

​	安装完成之后就可以使用virtualenv的命令来创建虚拟环境了，
​			  首先，需要进入需要创建虚拟环境的文件夹，比如F盘的envs文件夹，
​			  然后，使用以下命令创建一个虚拟环境，python版本的路径是可选的：
​				virtualenv 虚拟环境名称 [-p python版本的路径]
​				如：virtualenv env1 
​				如：virtualenv env1 -p C:\Python36\python.exe

#### 启动虚拟环境

​	在env1文件夹下打开CMD

```ini
env1>\Scripts\activate
```

进入虚拟环境后：
			使用pip安装numpy模块
			创建test.py文件,并在文件中使用numpy模块
			在cmd命令窗口使用python test.py执行文件

```ini
>python test.py
```

#### 退出虚拟环境（进入真实系统环境）

```ini
>deactivate  (如果报错则使用:env1\Scripts\deactivate)
```

## virtualenvwrapper 的安装和使用

*virtualenvwrapper是virtualenv的包装版，使用更方便*

### 安装

windows安装:

```ini
>pip install virtualenvwrapper-win
```

Linux安装:

```ini
>pip install virtualenvwrapper
```

### 使用

```ini
创建
>mkvirtualenv 虚拟环境名字 [-p python的路径]
删除
>rmvirtualenv 虚拟环境名称
```

注意：创建的虚拟环境放在用户目录下的Envs中

```
C:\Users\15011\Envs
```

### 进入

```ini
>workon 虚拟环境名称

```

### 退出

```ini
>deactivate

```



## pip常用命令

```ini
>pip install xxx:安装xxx依赖包
>pip list:查看当前环境下所有依赖包
>pip freeze:查看虚拟环境新安装的包
>pip uninstall xxx:卸载xxx包

```

## 出虚拟环境的包到文件

```ini
>pip freeze > requirements.txt

```

## 将文件中的所有包导入到虚拟环境

```ini
>pip install -r requirements.txt

```



# 虚拟环境-Linux

## virtualenv和virtualenvwrapper 的安装和使用 

**【请使用普通用户】**

### 安装虚拟环境

```shell
sudo apt update
sudo pip3 install virtualenv virtualenvwrapper

```

 安装后如果不能使用虚拟环境命令，则需要配置环境变量                    

1, 进入家目录: cd ~             

2, 使用vim打开.bashrc, 定位到最后:shift+g，并添加以下2行代码(注意修改自己Ubuntu的用户名)                  

```shell
export WORKON_HOME=/home/自己Ubuntu的用户名/.virtualenvs                 
source /usr/local/bin/virtualenvwrapper.sh        

```

3, 在家目录创建.virtualenvs目录: 

```shell
mkdir .virtualenvs      

```

4, 加载修改后的设置，使之生效：

```shell
source .bashrc 

```

### 创建虚拟环境

```shell
mkvirtualenv env             
mkvirtualenv env2 ‐p /usr/bin/python3  (指定python路径) 

```

### 退出虚拟环境

```shell
deactivate

```

### 进入虚拟环境

```shell
workon 虚拟环境名称

```

### 删除虚拟环境

```shell
rmvirtualenv env

```

