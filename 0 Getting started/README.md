# 0. Set up environment

## 软件安装
* Homebrew

```homebrew```是macOS使用的一个包管理器，通过homebrew可以很方便的安装开发所需的各种package。

```conda```是另一个很常见的包管理器。Conda的功能更强大，同时也更复杂，很容易把环境变量搞乱，在未来会产生很多头疼的问题。

安装homebrew：[https://brew.sh/](https://brew.sh/)

* Python 3.10

1. 查看python2的版本  
	* ```cmd> python --version```  
2. 查看python3是否安装及版本
	* ```cmd> which python3```  
	* ```cmd> python3 --version```  
3. 安装python 3.10 （若还未安装）  
	* ```cmd> brew install python@3.10```  
	* ```cmd> python3 --version```
4. Visual Studio Code (VSCode)

VSCode是一款主流IDE(Integrated Development Environment)。

---
P.S. 编辑器(Editor)和集成开发环境(IDE)有什么区别

编辑器：记事本, Sublime Text, Vim, etc.
集成开发环境：VS Code, PyCharm (Python), IntelliJ IDEA (Java), etc.

Editor主要负责编辑文本，提供一些基础的开发支持（语法高亮、自动补全等），更轻量.

IDE一般覆盖了开发时需要涉及的大部分功能，提供更强大的语法支持、debug功能、单元测试集成、git功能等，大大提升了开发的效率。

所有的功能也都可以使用命令行指令实现。我们会先使用命令行来进行操作，这样会帮助我们了解IDE背后是怎么工作的。熟练之后你会发现所有的可视化界面背后都是非常简单的代码。

---

* [安装VSCode](https://www.jetbrains.com/pycharm/download/#section=mac)  
* 安装插件Python

5. Git
	* ```cmd> brew install git```
	* ```cmd> git config --global user.name Leah```
	* ```cmd> git config --global user.email almighty.fann@gmail.com```
	* 注册Github账户并fork ztNIE的代码库，然后```cmd> git clone your_repository_link```
	* ~~删除这行之后尝试提交~~
	* ```cmd> git status```
	* ```cmd> git add *```
	* ```cmd> git commit```
	* ```cmd> git config --global credential.helper store```
	* [在github中生成密钥](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
	* ```cmd> git push```
    *  （Optional）[MIT: The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)

## 环境设置

* 虚拟环境

1. 什么是虚拟环境（virtual environment） 
	* 虚拟环境是一个为某个项目单独隔离的Python环境。可以把它理解为在某一个项目的文件夹里又安装了一个python，而且只有这个项目在使用这个python

2. 为什么要使用虚拟环境  
	* 虚拟环境可以保证每一个项目都可以使用自己的依赖，这样可以避免不同的项目之间依赖冲突所带来的麻烦

3. 创建虚拟环境
	* ```cmd> cd ~```
	* ```cmd> git clone https://github.com/ztNIE/programming101.git  # 这一步可以使用Leah的代码库```
	* ```cmd> cd programming101```
	* ```cmd> python3 -m venv your_env_name```
	* ```cmd> source your_env_name/bin/activate```

* 配置IDE
    * （PyCharm）打开文件夹Programming101
    * 了解各个部分都是什么（terminal，python console， debug， 运行）
    * hello_world.py (命令行运行，IDE运行)
    * [PyCharm快捷键Cheat Sheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard_mac.pdf)（建议打印一份放在电脑旁边随时看）
