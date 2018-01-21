'''安装beautifulsoup：
由于直接使用sudo apt-get install python-bs4安装时报错（未找到），aliyun的apt源地址有问题．
所以到官网上下载beautifulsoup4-4.6.0.tar.gz:https://www.crummy.com/software/BeautifulSoup/bs4/download/4.6/
下载解压后运行：sudo python setup.py install
报错：ModuleNotFoundError: No module named 'setuptools'

安装setuptools,安装前需要安装pip(pip是一个安装和管理Python包的工具).
1. 安装pip，发现又需要apt-get安装，仍然报错，与上面直接安装一样报错．所以又回到apt-get命令安装．
这里安装修改为先安装pip,然后安装setuptools,最后安装beautifulsoup4.6

更改apt-get的源为网易(gedit /etc/apt/sources.list)：
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb http://mirrors.163.com/ubuntu/ precise universe
deb-src http://mirrors.163.com/ubuntu/ precise universe
deb http://mirrors.163.com/ubuntu/ precise-updates universe
deb-src http://mirrors.163.com/ubuntu/ precise-updates universe
deb http://mirrors.163.com/ubuntu/ precise multiverse
deb-src http://mirrors.163.com/ubuntu/ precise multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse

修改保存后，运行：sudo apt-get update
报错：由于没有公钥，无法验证下列签名： NO_PUBKEY A6804EA8EAE0D85C
下载公钥：sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6804EA8EAE0D85C
再次运行: sudo apt-get update 成功
运行： sudo apt-get upgrade 更新成功

2. 安装pip,直接运行：sudo apt-get install python3-pip报错无法安装
先安装aptitude工具：sudot apt-get install aptitude
然后：sudo aptitude install python3-pip

各种报错，无法解决！！！　放弃了，打算windows中进行安装．
xp中安装，由于python3.5+不支持xp，目前最新版为3.6.
安装3.4版本(3.4.4rc1):https://www.python.org/downloads/windows/
安装后设置环境变量:Path中添加;C:\Python34
安装pip:https://pypi.python.org/pypi/pip#downloads
下载最新版为pip-9.0.1.tar.gz,解压，进入目录下执行：python setup.py install
安装成功，添加环境变量：Path中添加;C:\Python34\Scripts
cmd下运行pip list　验证安装成功

Windows还是好用，被Ubuntu折磨这一年多，还是用回windows吧(ubuntu还经常莫明其妙死机,更别多稳定性了：之前android环境ubuntu
下出问题搞了几天有没有，windows下最多几个小时;这次python3安装pip,ubuntu下搞了大半天还没搞定！windows下呢，几十分钟搞定，不想说啥了).

然后运行安装: pip install beautifulsoup4
嗯，又是几秒就搞定了．

注：关于python虚拟环境
可以安装python虚拟环境来管理多个python项目，如果未使用虚拟环境，每个库都是全局使用．
所以使用虚拟环境是很有好处的，包括项目打包后给别人使用，只要python版本相同，导入使用不会有各种兼容性问题．
所以，给自己定个规定，所有的项目都在virtualenv下开发．

安装virtualenv: pip install virtualenv
成功，可以在C:\Python34\Scripts下看到pip3.ext pip.ext virtualenv.exe等．

创建虚拟环境：virtualenv scrapingEnv　（创建要等一会，需要安装setuptools pip wheel等，应该是创建一个隔离的python环境）
之后关于爬虫的项目都在scrapingEnv下开发,注意scrapingEnv是在当前目录下创建
激活并使用:
cd scrapingEnv
Scripts/activate
全新安装beautifulsoup:　pip install beautifulsoup4
验证安装成功： python
from bs4 import BeautifulSoup

释放退出虚拟环境：quit()　先退出python环境
deactivate 退出虚拟环境

3. 编辑器使用：vsc不支持xp安装，搜索后使用pycharm作为python开发ide来使用．
pycharm安装后，xp中无法运行．．．．还是安装个win7虚拟机来用吧．
pycharm使用教程:http://www.phperz.com/article/14/1213/14349.html



