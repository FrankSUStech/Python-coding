# Python selenium 模拟登录bilibili

​	**Selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。**

​	在登录bilibili的时候，会有一个拖动图片的验证——极验验证码。我们用selenium在Chrome中打开bilibili的登录页面。然后填写登录账号和密码。再点击登录按钮，页面弹出极验验证码，通过js获取两张图片(一张完整的图片，一张有缺口的图片)，这两张图片是用canvas画出来的。所有我们用toDataURL("image/png")方法拿到的是base64格式的图片。将这两张图片的用PIL中的Image来获转化之后的图片。比较两张图片的像素点，从而计算出拖动块需要移动的距离。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026160838876.gif)


# 流程图

![在这里插入图片描述](https://img-blog.csdnimg.cn/201910261607242.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjg1Njg3MQ==,size_16,color_FFFFFF,t_70)

# 总体框架

```python
class LoginBiliBili:

    def __init__(self, username, password):
        """
        初始化数据

        :param username: bilibili账号
        :param password: 密码
        """

    def open(self):
        """
        打开浏览器, 进入登陆界面
        输入用户名, 密码
        点击登陆

        :return: None
        """

    def get_geetest_image(self):
        """
        获取极验验证码图片
        :return: c_image(王者验证图) ic_image(有缺失的验证图)
        """

    def is_pixel_similar(self, c_image, ic_image, x, y):
        """
        比较两张图片的像素点

        注意: 像素点比较是有偏差的, 需要允许一定范围的误差,
            我们可以设置一个阈值
        :param ic_image:
        :param c_image:
        :param x:
        :param y:
        :return: 当像素点不相同时, 返回 False
        """

    def get_slice_gap(self, c_image, ic_image):
        """
        获取缺口的偏移量

        通过比较两张图片的所有像素点, 获取两张图片是从哪里开始不同
        从而得到 移动块 要在 x 方向移动的距离

        :param c_image: 完整的图片
        :param ic_image: 有缺失的图片
        :return: 缺口的偏移量
        """

    def drag_slider(self, gap):
        """
        拖动滑块

        :param gap: 需要拖动的距离
        :return: None
        """

    def login_success(self):
        """
        判断是否登陆成功
        :return: 成功返回 True 失败返回False
        """

    def login(self):
        """
        开始

        :return: None
        """


if __name__ == '__main__':
    login = LoginBiliBili('*******', '******')
    login.login()
```



# 初始化数据方法

*将一些初始化数据在__init__()函数中定义*

```python
def __init__(self, username, password):
    """
    初始化数据

    :param username: bilibili账号
    :param password: 密码
    """
    self.username = username
    self.password = password
    # 定义浏览器
    self.browser = webdriver.Chrome()
    # 定义显示等待
    self.wait = WebDriverWait(self.browser, 50)
    # bilibili登录url
    self.url = 'https://passport.bilibili.com/login'
```



# 打开浏览器方法

*此方法用来打开浏览器，在进入登陆页面之后，自动输入用户名，密码。以及点击的登录按钮*

```python
def open(self):
    """
    打开浏览器, 进入登陆界面
    输入用户名, 密码
    点击登陆

    :return: None
    """
    # 打开浏览器, 进入登陆界面
    self.browser.get(self.url)

    # 用户名输入框
    username_input_box = self.wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))
    )
    # 清空用户名输入框
    username_input_box.clear()
    # 将自己的用户名输入到用户名输入框
    username_input_box.send_keys(self.username)

    # 密码输入框
    password_input_box = self.wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login-passwd"]'))
    )
    # 清空密码输入框
    password_input_box.clear()
    # 将自己的密码输入到密码输入框
    password_input_box.send_keys(self.password)

    # 登录按钮
    login_button = self.wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="geetest-wrap"]/ul/li[5]/a[1]'))
    )
    # 点击登录
    login_button.click()
    # 休眠, 让验证码图片加载出来
    time.sleep(2)
```



# 拿极验验证码图片方法

*如何拿到极验验证码图片是我们进行模拟登录的关键一步，这里的极验验证码是由canvas绘制的两张图片，所有我们需要用js去获取图片。*

```python
def get_geetest_image(self):
    """
    获取极验验证码图片
    :return: c_image(王者验证图) ic_image(有缺失的验证图)
    """
    """
    完整的验证图
    页面源码:
    <canvas class="geetest_canvas_fullbg geetest_fade geetest_absolute" 
    height="160" width="260" style="display: none;"></canvas>
    """
    # 执行js 拿到canvas画布里面的图片数据
    js = 'return document.getElementsByClassName("geetest_canvas_fullbg")[0].toDataURL("image/png");'
    # 图片数据
    complete_img_data = self.browser.execute_script(js)
    # base64 编码的图片信息
    complete_img_base64 = complete_img_data.split(',')[1]
    # 转成bytes类型
    complete_img = base64.b64decode(complete_img_base64)
    # 加载图片 return 回去对比
    c_image = Image.open(BytesIO(complete_img))
    # c_image.show()
    # 保存图片 (可不必保存)
    c_image.save('c_image.png')

    """
    有缺失的验证码图

    页面源码:
    <canvas class="geetest_canvas_bg geetest_absolute" height="160" width="260"></canvas>
    """
    # 执行js 拿到canvas画布里的图片数据
    js = 'return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");'
    # 图片数据
    incomplete_img_data = self.browser.execute_script(js)
    # base64 编码的图片信息
    incomplete_img_base64 = incomplete_img_data.split(',')[1]
    # 转为bytes类型
    incomplete_img = base64.b64decode(incomplete_img_base64)
    # 直接加载图片 return 回去对比
    ic_image = Image.open(BytesIO(incomplete_img))
    # ic_image.show()
    # 保存图片(可不必保存)
    ic_image.save('ic_image.png')

    return c_image, ic_image
```



#　对比像素点方法　和　获取移动距离方法

*这两个方法我们要将它们联系起来，我们通过对比图片横向和纵向的像素点，来确定两张图片是从哪里开始不同的。当然，我们只需要得知水平方向哪里开始不同的（滑块只需要在水平方向移动）*

```python
def is_pixel_similar(self, c_image, ic_image, x, y):
    """
    比较两张图片的像素点

    注意: 像素点比较是有偏差的, 需要允许一定范围的误差,
    我们可以设置一个阈值
    :param ic_image:
    :param c_image:
    :param x:
    :param y:
    :return: 当像素点不相同时, 返回 False
    """
    # 获取两张图片执行位置的像素点
    c_pixel = c_image.load()[x, y]
    ic_pixel = ic_image.load()[x, y]
    # 阈值 允许误差
    threshold = 10
    # 对比
    if abs(c_pixel[0] - ic_pixel[0]) < threshold and \
    abs(c_pixel[1] - ic_pixel[1]) < threshold and \
    abs(c_pixel[2] - ic_pixel[2]) < threshold:
    return True
    return False

def get_slice_gap(self, c_image, ic_image):
    """
    获取缺口的偏移量

    通过比较两张图片的所有像素点, 获取两张图片是从哪里开始不同
    从而得到 移动块 要在 x 方向移动的距离

    :param c_image: 完整的图片
    :param ic_image: 有缺失的图片
    :return: 缺口的偏移量
    """
    # ic_image.size:['width', 'height']
    for x in range(c_image.size[0]):
    for y in range(c_image.size[1]):
    if not self.is_pixel_similar(c_image, ic_image, x, y):
    # 移动块只在水平方向移动 只需返回 x
    return x
```

# 拖动滑块方法

*然后就是拖动滑块了.*

```python
def drag_slider(self, gap):
    """
    拖动滑块

    :param gap: 需要拖动的距离
    :return: None
    """
    slider = self.wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]'))
    )
    # 抓住滑块
    ActionChains(self.browser).click_and_hold(on_element=slider).perform()
    # 移动 只在水平方向上移动
    ActionChains(self.browser).move_by_offset(xoffset=gap, yoffset=0).perform()
    # 释放滑块
    ActionChains(self.browser).release().perform()
```



**由于对比像素点有一定的误差,不一定会一次成功,所有我们会需要一个循环来进行多次验证,在判断成功登录之后,才结束进程.**

# 判断是否登录

```python
def login_success(self):
    """
    判断是否登陆成功
    :return: 成功返回 True 失败返回False
    """
    try:
    # 登录成功后 界面上会有一个消息按钮
    return bool(
    WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@title="消息"]')))
    )
    except TimeoutException:
    return False
```



# 开始登录

```python
def login(self):
    """
    开始

    :return: None
    """
    # 打开浏览器, 输入账号 密码, 点击登陆
    self.open()
    # 获取验证图 ic_image(有缺失的验证图) c_image(完整的验证图)
    c_image, ic_image = self.get_geetest_image()

    # 获取缺口的偏移量
    gap = self.get_slice_gap(c_image, ic_image)
    print(f'缺口的偏移量为:{gap}')
    # 拖动滑块
    # TODO 这边一直有一定的误差 暂时用测量工具解决
    self.drag_slider(gap-8)
    time.sleep(3)

    if self.login_success():
    print('登陆成功')
    else:
    self.login()
```



# 完整的代码

```python
class LoginBiliBili:

    def __init__(self, username, password):
        """
        初始化数据

        :param username: bilibili账号
        :param password: 密码
        """
        self.username = username
        self.password = password
        # 定义浏览器
        self.browser = webdriver.Chrome()
        # 定义显示等待
        self.wait = WebDriverWait(self.browser, 50)
        # bilibili登录url
        self.url = 'https://passport.bilibili.com/login'

    def open(self):
        """
        打开浏览器, 进入登陆界面
        输入用户名, 密码
        点击登陆

        :return: None
        """
        # 打开浏览器, 进入登陆界面
        self.browser.get(self.url)

        # 用户名输入框
        username_input_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))
        )
        # 清空用户名输入框
        username_input_box.clear()
        # 将自己的用户名输入到用户名输入框
        username_input_box.send_keys(self.username)

        # 密码输入框
        password_input_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-passwd"]'))
        )
        # 清空密码输入框
        password_input_box.clear()
        # 将自己的密码输入到密码输入框
        password_input_box.send_keys(self.password)

        # 登录按钮
        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="geetest-wrap"]/ul/li[5]/a[1]'))
        )
        # 点击登录
        login_button.click()
        # 休眠, 让验证码图片加载出来
        time.sleep(2)

    def get_geetest_image(self):
        """
        获取极验验证码图片
        :return: c_image(王者验证图) ic_image(有缺失的验证图)
        """
        """
        完整的验证图
        页面源码:
        <canvas class="geetest_canvas_fullbg geetest_fade geetest_absolute" 
        height="160" width="260" style="display: none;"></canvas>
        """
        # 执行js 拿到canvas画布里面的图片数据
        js = 'return document.getElementsByClassName("geetest_canvas_fullbg")[0].toDataURL("image/png");'
        # 图片数据
        complete_img_data = self.browser.execute_script(js)
        # base64 编码的图片信息
        complete_img_base64 = complete_img_data.split(',')[1]
        # 转成bytes类型
        complete_img = base64.b64decode(complete_img_base64)
        # 加载图片 return 回去对比
        c_image = Image.open(BytesIO(complete_img))
        # c_image.show()
        # 保存图片 (可不必保存)
        c_image.save('c_image.png')

        """
        有缺失的验证码图

        页面源码:
        <canvas class="geetest_canvas_bg geetest_absolute" height="160" width="260"></canvas>
        """
        # 执行js 拿到canvas画布里的图片数据
        js = 'return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");'
        # 图片数据
        incomplete_img_data = self.browser.execute_script(js)
        # base64 编码的图片信息
        incomplete_img_base64 = incomplete_img_data.split(',')[1]
        # 转为bytes类型
        incomplete_img = base64.b64decode(incomplete_img_base64)
        # 直接加载图片 return 回去对比
        ic_image = Image.open(BytesIO(incomplete_img))
        # ic_image.show()
        # 保存图片(可不必保存)
        ic_image.save('ic_image.png')

        return c_image, ic_image

    def is_pixel_similar(self, c_image, ic_image, x, y):
        """
        比较两张图片的像素点

        注意: 像素点比较是有偏差的, 需要允许一定范围的误差,
            我们可以设置一个阈值
        :param ic_image:
        :param c_image:
        :param x:
        :param y:
        :return: 当像素点不相同时, 返回 False
        """
        # 获取两张图片执行位置的像素点
        c_pixel = c_image.load()[x, y]
        ic_pixel = ic_image.load()[x, y]
        # 阈值 允许误差
        threshold = 10
        # 对比
        if abs(c_pixel[0] - ic_pixel[0]) < threshold and \
                abs(c_pixel[1] - ic_pixel[1]) < threshold and \
                abs(c_pixel[2] - ic_pixel[2]) < threshold:
            return True
        return False

    def get_slice_gap(self, c_image, ic_image):
        """
        获取缺口的偏移量

        通过比较两张图片的所有像素点, 获取两张图片是从哪里开始不同
        从而得到 移动块 要在 x 方向移动的距离

        :param c_image: 完整的图片
        :param ic_image: 有缺失的图片
        :return: 缺口的偏移量
        """
        # ic_image.size:['width', 'height']
        for x in range(c_image.size[0]):
            for y in range(c_image.size[1]):
                if not self.is_pixel_similar(c_image, ic_image, x, y):
                    # 移动块只在水平方向移动 只需返回 x
                    return x

    def drag_slider(self, gap):
        """
        拖动滑块

        :param gap: 需要拖动的距离
        :return: None
        """
        slider = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]'))
        )
        # 抓住滑块
        ActionChains(self.browser).click_and_hold(on_element=slider).perform()
        # 移动 只在水平方向上移动
        ActionChains(self.browser).move_by_offset(xoffset=gap, yoffset=0).perform()
        # 释放滑块
        ActionChains(self.browser).release().perform()

    def login_success(self):
        """
        判断是否登陆成功
        :return: 成功返回 True 失败返回False
        """
        try:
            # 登录成功后 界面上会有一个消息按钮
            return bool(
                WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@title="消息"]')))
            )
        except TimeoutException:
            return False

    def login(self):
        """
        开始

        :return: None
        """
        # 打开浏览器, 输入账号 密码, 点击登陆
        self.open()
        # 获取验证图 ic_image(有缺失的验证图) c_image(完整的验证图)
        c_image, ic_image = self.get_geetest_image()

        # 获取缺口的偏移量
        gap = self.get_slice_gap(c_image, ic_image)
        print(f'缺口的偏移量为:{gap}')
        # 拖动滑块
        # TODO 这边一直有一定的误差 暂时用测量工具解决
        self.drag_slider(gap-8)
        time.sleep(3)

        if self.login_success():
            print('登陆成功')
        else:
            self.login()


if __name__ == '__main__':
    login = LoginBiliBili('*******', '******')
    login.login()
```
