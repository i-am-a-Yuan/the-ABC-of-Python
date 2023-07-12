# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:47:48 2023

@author: 86183
"""


'''
1.1为什么学习python


'''



# python的特点：
# 简单、易学、免费、开源
# 解释型语言：编辑代码，通过解释器进行实现
# 可移植性：应用于不同解释器中
# 代码规范：缩进，简洁
# 胶水语言：连接不同编程语言、网页端、应用中
# 丰富的库：如math、symtom等。积累资源充分应用
# 动态类型：？？？？？？？？？


# python的基础课：
#     编程思维
#     办公自动化
#     面向对象
#     程序模块结构
#     第三方库
    
# python数据分析：
#     pandans
#     numpy
#     数据可视化
    
# 机器学习与深度学习：
#     TensorFlow
#     OpenCV
#     其它

# 其它：
#     测试
#     游戏
    
    
'''
 2.2搭建python开发环境
 
 
'''
# 安装python解释器：
    # http://www.python.org
    # 可嵌入的压缩文件：Windows x86-64 embeddable zip file
    # 可执行的安装文件：Windows x86-64 executable installer
    # 基于Web的安装文件：Windows x86-64 web-based installer

# 执行exe文件后勾选“Add Python 3.7 to PATH”

# 相关程序介绍：
    # 自带的简单开发环境：IDLE (Python 3.8 64-bit)
    # 交互式命令行程序：Python 3.8(64-bit)
    # 官方技术手册【对应的是在线的技术手册】：Python 3.8 Manuals(64-bit)
    # 已安装的模块文档：Python 3.8 Module Docs(64-bit)

'''
 2.3python中的输出函数：print()
 
'''

# ·print()函数可以输出哪些内容？
#     1）print()函数输出的内容可以是数字
#     2）print()函数输出的内容可以是字符串
#     3）print()函数输出的内容可以是含有运算符的表达式
# ·print()函数可以将内容输出的目的地
#     1）显示器
#     2）文件
# ·print()函数的输出形式
#     1）换行
#     2）不换行


#2.3.eg1
# 输出数字
print(3.14)
print(520)
# 输出字符串
print("人生苦短，我用python")
print("http://time.baidu.com")
print('He said to me, "A man can be killed, but can \'t be defeated!"')
# 输出运算符的表达式
print(4+6)
print(10-1)
# 输出内容到文件，a+打开方式（如果文件不存在则创建后写入，如果存在，则把内容补充在最后）
fp = open("C:/Users\86183\Desktop/firsttext.txt","a+") # a+的方式是打开后追加在文件中内容后面添加
print("人生苦短我用Python",file=fp)
fp.close()


'''
2.4转义字符与愿意字符


'''

# 转义字符的结构：反斜杠“\”加上想要实现的转移功能首字母
# 转义字符的使用场景：
# 反斜杠、单引号、双引号本身带有特殊用途，因此在正常字符串中需要使用反斜杠对这些字符进行转义
# 反斜杠：\\
# 单引号：\'
# 双引号：\"

# 换行符：\n -newline
# 回车符：\r -return
# 水平制表符:\t -tab
# 退格：\b -backspace
 

# 愿意字符的结构：在引号前加r或R
print("http:\\www.lixin.edu.cn")
print(r"http:\\www.lixin.edu.cn")
print("http:\\www.lixin.edu.cn")

print("第一个字符串",'第二个字符串',"第三个字符串")
print("第一个字符串",'第二个字符串',"第三个字符串",end="\n")
print("第一个字符串\n",'第二个字符串\n',"第三个字符串\n") #逗号表示两个字符串空格
print("111",end="")
print("222",end="\n")
print("333",end="\t")
print("444",end="\r")
print("555",end="")

print("1234567\r89")

print("12345","45678",sep='@')

'''
IDLE快捷键使用



新建文件快捷键：ctrl+n
选定区域缩进快捷键：ctrl+]
选定区域取消缩进快捷键：ctrl+[
选定区域快速注释快捷键：Alt+3
选定区域快速取消注释快捷键：Alt+4
选定区域中空格替换为Tab：Alt+5（需要设定多少空格对应一个Tab）
选定区域中Tab替换为空格：Alt+6（需要设定一个Tab对应多少空格）

'''













    














