# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:44:31 2023

@author: a_Yuan
"""

# 第3章Python程序的基本流程控制


# 3.1 计算思维和程序设计基本方法
# 3.2 顺序结构
# 3.3 分支结构
# 3.4 循环结构
# 3.5 程序调试


#3.1计算思维和程序为设计基本方法
# 3.1.1 计算思维
# 3.1.2 程序设计基本方法
#     冯诺依曼结构：输入设备、运算器、控制器、存储器和输出设备
#     输入方式：交互界面输入、文件上输入、网络输入
#     输出方式：屏幕输出、文件输出、网络输出
#     程序设计方法：结构化设计方法、面向对象的程序设计方法
#     结构化设计方法：顺序结构、分支结构、循环结构
#     三者相互嵌套、排列组合，以实现复杂问题的分解
#3.2顺序结构
    # 程序工作的一般流程：数据输入、运算处理、结果输出
# age_dad = int(input("请输入爸爸的年龄："))
# age_son = int(input("请输入儿子的年龄："))
# difference = age_dad - age_son
# print("爸爸与儿子的年龄差为：",difference)
    
#--3.2.1  计算语数英成绩并输出平均成绩，保留一位小数
grade_chinese = float(input("请输入您的语文成绩："))
grade_math = float(input("请输入您的数学成绩："))
grade_english = float(input("请输入您的英语成绩："))
average = (grade_chinese + grade_math + grade_english)/3
print("您的平均成绩为：%.1f" % average)

#--3.2.2  输入圆的半径，计算并输出圆的周长和面积

import math

radius = float(input("请输入圆的半径："))
circumference = 2 * math.pi * radius #注意格式：math.pi
area = math.pi * radius**2
print("圆的周长为：%.2f" % circumference)
print("圆的面积为：%.2f" % area)

#--3.3.3  从键盘输入年份，输出当年的年历
# Python 的内置日历模块calendar 有下列常用函数：
# calendar.weekday(year, month, day)  获取指定日期为星期代码整数，0为星期一，1为星期二，以此类推
# calendar.monthcalendar(year, month)  返回year年month月中以日期为一维元素列表，以每周日期列表为元素的二维列表
# calendar.month(year, month) 以多黄文本字符串格式返回year年month月的日历
# calendar..calendar(year)    以多行字符串形式返回year年的日历

import calendar
calendar.weekday(2008, 3, 3)
calendar.monthcalendar(2008, 3)
import calendar
print(calendar.month(2008,4))
import calendar
print(calendar.calendar(2008))

# eg.1
    # import calendar
    # year = int(input("请输入年份："))
    # table = calendar.caendar(year)
    # print(table)

#3.3分支结构
# 3.3.1 if语句
# eg:
name = input(input("请输入您的姓名："))
age = int(input("请输入您的年龄："))
if age >=18:
    print(name,"已经成年")
    print("符合驾照考试规定")
# 3.3.2 if-elif-else语句
# eg:
name=input("请输入您的姓名")
grade_chinese = float(input("请输入您的语文成绩："))
grade_math = float(input("请输入您的数学成绩："))
grade_english = float(input("请输入您的英语成绩："))
average=(grade_chinese +grade_math +grade_english)/3
if average >=85:
    print(name,"获一等奖")
elif average >=75:
    print(name,"获二等奖")
elif average >=60:
    print(name,"获三等奖")
else:
    print(name,"没有获奖")

# eg3-4编写程序，从键盘输入一个整型数字，判断改善胡子是否为偶数。
number=int(input("请输入一个整型数字："))
if number%2==0:
    print(number,"是一个偶数")
# eg3-5编写程序，从键盘输入三条边，判断是否能够构成一个三角形。如果能，则提示可以构成三角形；如果不能，则提示不能构成三角形。
side1=float(input("请输入三角形第一条边："))
side2=float(input("请输入三角形第二条边："))
side3=float(input("请输入三角形第三条边："))
if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    print(side1,side2,side3,"可以构成三角形")
else:
    print(side1,side2,side3,"不可以构成三角形")
# eg3-6编写程序，调用随机函数生成一个1~100之间的随机整数，从键盘输入数字进行猜谜，给出猜测结果（太大、太小、成功）的提示。
import random
# random.random()     生成一个半开区间[0.0,1.0)内的浮点数
# random.radint(start,Stop)       生成一个闭区间[start,stop]内的整数
# random.choice(seq)      随即返回一个range(start,stop[,step])中的整数
# random.shuffle(lst)     将列表lst的数列随机重排，不能作用于字符串和元组
randnumber=random.randint(1, 100)
guess=int(input("请输入您的猜测："))
if guess>randnumber:
    print("您的猜测太大")
elif guess<randnumber:
    print("您的猜测太小")
else:
    print("恭喜您猜对了")
#3.3.3分支语句嵌套
# eg:
sex=input("请输入您的性别（M或者F）:")
age=int(input("请输入您的年龄(1-120):"))
if sex=='M':
    if age>=22:
        print("到达合法结婚年龄")
    else:
        print("未到达合法结婚年龄")
else:
    if age>=20:
        print("到达合法结婚年龄")
    else:
        print("未到达合法结婚年龄")
# eg3-7编写程序，从键盘输入用户名和密码，要求先判断用户名再判断密码。
# 如果用户名不正确，则直接提示用户名输入有误；如果用户名正确，则进一步判断密码，并各处判断结果的提示。
username=input("请输入您的用户名：")
password=input("请输入您的密码：")
if username=="admin":
    if password=="123456":
        print("输入正确，恭喜进入！")
    else:
        print("密码有误，请重试！")
else:
    print("用户名有误，请重试！")
# eg3-8编写程序开发一个小型计算器，从键盘输入两个数字和一个运算符，根据运算符（+、-、*、/）进行相应的数学运算。如果不是这4中运算符，则给出错误提示。
first=float(input("请输入第一个数字："))
second=float(input("请输入第二个数字："))
sign=input("请输入运算符号：")
if sign=='+':
    print("两数之和为：",first+second)
elif sign=='-':
    print("两数之差为：",first-second)
elif sign=='*':
    print("两数之积为：",first*second)
elif sign=='/':
    if second!=0:
        print("两数之商为：",first/second)
    else:
        print("除数为0错误！")
else:
    print("符号输入有误！")
#3.4循环结构
# 3.4.1 while语句
# eg:
time=8
while time<12:
    print("有效次数内")
    time=time+1
else:
    print("计次已满")
# 1.while 语句的判别式中表达式的类型：x!=y,x>3 or x<5,-5(非0即为True)
# 2.while 循环体可能不执行：a=3 while a<=2:
# 3.while 全部执行完成后，执行else:语句
a=0
while a<10:
    print(1)
    if a>=6:
        break
    a+=1
else:
    print(3)
# 4.else子句可以省略
# 5.while 循环体需要注意最后是否有可以结束循环的条件，否则程序无法终止。
# 6.死循环：重复循环操作，如条件语句恒为真，即while True

# eg3.9编写程序，统计并输出1~1000y内所有能够同时被3和7整除的数字个数。
number=1
count=0
while number<1000:
    if number%3==0 and number%7==0:
        count=count+1
    number=number+1
print("同时能够被数字3和7整除的数字个数为：",count)

# eg3.10编写程序，用下列公式计算π的近似值，知道最后一项的绝对值小于10^-6为止。
import math
n=1 # 变量自增值
t=1 # 每项值
total=0 # 1/4π的值
flag=1 # 标记位（每项的正负符号）
while math.fabs(t)>=1e-6: # 当每项值的绝对值大于1e-6时进行计算
    total=total+t
    flag=-flag
    n=n+2
    t=flag*1.0/n
print("π=%f"%(total*4))

# 3.4.2for语句和range()内置函数
# for 语句的操作对象：字符串、列表、元组、字典、迭代器:
for i in "人生苦短，我用Python。":  # 字符串
    print(i)
lst=[1,2,3,4,8,9,1.22,3.66,"人生",(345,(4,5,6,0),678,(3.1,3.2))] # 列表不能含键值对？？
for i in lst:
    print(i[9][1][3])
    
# # 具体格式：
# for 循环变量 in 对象: # 循环变量不需要额外定义
#     语句块A
# else： # 可选
#     语句块B

# eg:
word="Hello"
for iNum in word:
    print(iNum,end=" ") # end值的双引号中为一个空格
# 运行结果为：“H e l l o ”【】

# eg:
merge=[25,"hello",12.8,"A"]
for iNum in merge:
    print(iNum,end=" ")
# 运行结果为：“25 hello 12.8 A ”

# eg计算字符串中某字符串出现的次数:
word = '山羊上山山碰山羊角'
sum = 0
for letter in word:
    if letter == '山':
        sum += 1
print(sum)

# 运行结果为“4”，即以遍历方式计算出“山”在字符串中出现的次数。

### for 语句经常与range()内置函数配合使用。
 # range()函数用于生成整数序列，通常的写法是：range(start,end,step).step的默认值是1

# 例如需要生成从[2,20]的偶数：
# 依次递增的顺序：
for i in range(2,21,2): # 或第二个数改为22
    print(i,end=" ") # end空值默认为换行

# 换一种写法依次递减的顺序是：
for i in range(20,1,-2): # 任然是左闭右开，所以用1
    print(i,end=" ")

# 随机顺序：???
import random
merge=[]
for i in range(2,21,2):
    merge.append(i)
random.shuffle(merge)
print(merge)


# eg3-11编写程序，使用for语句计算1~1000 的自然数之和。
total=0
for iNum in range(1,1000,1):
    total=total+iNum
print(total)

# eg3-12编写程序，有一人做了好事，解决三真一假问题。
# A说：不是我；
# B说：是C；
# C说：是D；
# D说：C胡说。
for iNum in['A','B','C','D']: #设iNum是做了好事的那个人
    if (iNum!='A')+(iNum=='C')+(iNum=='D')+(iNum!='D') == 3:
        print(iNum,"做了好事！")


# 3.4.3循环语句嵌套
for i in range(1,3):
    print("")
    for j in range(1,4):
        print("{}*{}={}".format(i,j,i*j),end=' ')

# eg3-13编写程序，使用双重循环输出九九乘法表。
# 以下是书上的写法：
for i in range(1,10):
    for j in range(1,10):
        print("%s*%s=%2s"%(i,j,i*j),end="\t") # %2s指长度为2的字符串
    print("\n")


# 另一写法：
for i in range(1,10):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j),end="\t")
    print("\n")

# eg3-14 编写程序，生成一个5行的三角形。
# 以下是书上的写法：
for i in range(1,6): # 5行
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print("\n")
# 另一写法：
for i in range(1,6):
    print((5-i)*"  ",end=" ")
    print((2*i-1)*"* ",end=" ")
    print("\n")

# eg3-15 编写程序解题：
#         山外山
#     +)  青龙山
# ---------------
#       青龙山外

# 课本写法：

for qing in range(10):
    for long in range(10):
        for shan in range(10):
            for wai in range(10):
                if (qing==long or qing==shan or qing==wai\
                    or long==shan or long==wai or shan==wai):
                    continue
                elif (shan*100 +wai*10 +shan +qing*100 +long*10 +shan\
                      == qing*1000+long*100+shan*10+wai):
                    print("qing=%d,long=%d,shan=%d,wai=%d"\
                          %(qing,shan,long,wai))
                    break    #break减少运行负担
# 执行结果为：qing=1,long=9,shan=0,wai=8

# 3.4.4转移和中断语句
# 1.break
# eg3.16编写程序，随机产生骰子的一面（数字1~6），给用户三次猜测机会，程序给出猜测提示（偏大或偏小）。
# 如果某次猜测正确，则提示正确并中断循环；如果三次均猜错，则提示机会用完。

import random
point=random.randint(1,6)
count=1
while count<=3:
    guess=int(input("请输入您的猜测："))
    if guess>point:
        print("您的猜测偏大！")
    elif guess<point:
        print("您的猜测偏小！")
    else:
        print("恭喜您猜对了！")
        break  # 直接跳出整个while-else循环体系
    count=count+1
else:
    print("很遗憾，三次全猜错了！")

# 半路循环：在死循环程序中，通过添加break语句终止程序的执行，称为半路循环。
# eg:
number=1
while 1:
    print("Python是一门程序语言")
    if number>=5:
        break
    number=number+1
print(number)

# 2.continue
# 中断本次循环的执行
# eg3-17编写程序，从键盘输入一段文字，如果其中包含“密”字（可能出现1次或者多次），
# 则输出时过滤掉该字，其他内容原样输出。
# 过滤器功能的程序呢！
sentence=input("请输入一段文字：")
for word in sentence:
    if word=="密":
        continue
    print(word,end="")

# eg3-18编写程序，从键盘输入密码，如果密码长度小于6，则要求重新输入。
# 如果长度等于6，则判断密码是否正确，如果正确则中断循环，否则提示错误并要求重新输入。
while 1:
    password=input("请输入密码：")
    if len(password)<6:
        print("长度为6位，请重试！")
        continue
    if password =="123456":
        print("恭喜您，密码正确！")
        break
    else:
        print("密码有误，请重试！")      #

#3.5程序调试】】】】】】】】】

# 3.5.1语法错误与逻辑错误
# 语法错误：程序代码不符合解释器语法规则，导致程序无法正常运行，如关键字拼写错误、缩进位置不正确、漏写规定符号等。
# 语法错误通常可以在编写代码或编译时被发现，编译器就会以醒目的形式报错。含有语法错误的语句是不能通过编译的。
# （简单来说就是：漏了，电脑看得出。）

# 逻辑错误：程序代码符合语法规定，但是由于算法、运行环境等问题不能得到预期的计算结果，如遗漏重要代码段、算法使用错误\\
#     、变量作用域错误、漏掉循环语句的结束条件等。
# 逻辑错误往往能够通过编译因而难以被直接发现，需要通过人工或调试工具跟踪执行过程来排查。
# （简单来说就是：写错了，电脑发现不了）

# 3.5.2常见语法错误（写Bug(bushi)代码的后用不到，debug的时候用来参照）】】】
# 1.算术错误（ArithmeticError）:x/0
# 2.断言错误（AssertionError）
# 3.属性错误（AttributeError）
# 4.缓冲错误（BufferError）
# 5.结束条件错误（EOFError） *
# 6.模块引入错误（ImportError）
# 7.查询错误（LookupError）
# 8.内存溢出错误（MemoryError）
# 9.对象名称错误（NameError）:变量没见过(大小写敏感)
# 10.操作系统错误（OSError）
# 11.引用对象错误（ReferenceError）
# 12.运行时错误（RuntimeError）
# 13.语法规则错误（SyntaxError）*:漏了“:”
# 14.系统内部错误（SystemError）
# 15.类型错误（TypeError）  *:str/int/float/bool
# 16.赋值参数错误（ValueError）
# 17.常规异常（Exception）

# 1[9].对象名称错误：
# （1）对象名称拼写错误：name="张三",print(Name)
# （2）对象名称未定义或赋值而直接使用：a=0,a+=1,b+=1

# 2[13].语法规则错误：
# （1）语法符号的错漏：for cNum in "Python" print(cNum)
# （2）误将关键词作为对象名称：class='三班' print(class)
# （3）赋值运算符与比较运算符的误用：if a ==b:  if a=b:
# eg:
    # import random
    # string = '床前明月光'
    # number = random.randint(0,4)
    # guess = input('请输入您的猜测：')
    # if guess = string[number]:
        # print('猜对了')
    # else:
        # print('猜错了')
# （4）缩进错误：
# eg:
    # import math
    # if math.pi>3:
        # print('yes')

# 3[7].查询错误
# （1）索引错误（IndexError）：索引值不存在或超出范围
# eg:
    # name="张三"
    # print(name[2])
# （2）映射错误（KeyError）:使用的键不存在（第四章）

# 4[15].类型错误
# （1）字符串和元组为不可变数据类型，修改元素会产生类型错误
# eg:
    # test="hello everyone."
    # test[0]="H"
    # print(test)
    # 产生错误提示：TypeError:'str' object does not support item assignment
# （2）字符串与数字不能直接连接，需要用str()对数字进行转化
# eg:
    # age=18
    # name="张三"
    # merge=name+"今年"+age+"岁"【】
    # print(merge)
    # 产生错误提示：TypeError:must be str, not int
# 正确写法：【】换为merge=name+"今年"+str(age)+"岁"
# （3）使用range()函数输出字符串、元组、列表中制定的元素是，需要先调用len()函数计算字符串中元素的个数。
# eg:
    # string ="123456789"
    # for i in range(1,string,2):
        # print(string[i])
    # 产生错误提示：TypeError: 'str' object cannot be interpreted as an integer
# 正确写法：
    # string="123456789"
    # for i in range(1,len(string),2):
    #     print(string[i])
      
# 5[6].模块引用错误：
# 在导入模块时，模块名写错或模块路径设置有问题，会导致模块引用错误
# eg:
    # import Calendar #calendar应该是全部小写
    # 产生错误提示：ModuleNotFoundError: No module named 'Calendar'

# 6[1].算术错误：
# （1）浮点计算错误（FloatingPointError）
# （2）溢出错误（OverflowError）
# （3）除零错误（ZeroDivision）:2/0
# 产生错误提示：ZeroDivisionError: division by zero

# 7[10]操作系统错误：
# 文件打开错误、读写错误、操作权限不够、请求超时等
# 文件名写错、文件路径不对、文件卡开模式不对等（详见第5章）
# eg:
    fobj=open("test.txt","r") #以只读(r)方式打开test.txt，并输出全部内容
    for line in fobj:
        print(line)
    fobj.close()
    # 但是文件不存在，程序无法正常执行
# 产生错误提示：FileNotFoundError: [Errno 2] No such file or directory: 'test.txt

# 8[3]属性错误：
# 属性应用或赋值失败会导致属性错误。方法名拼写错误也将提示为属性错误。
# eg:
    s='ABCDE'
    s=s.lowerr()
    print(s)
# 产生属性错误：AttributeError: 'str' object has no attribute 'lowerr'



# 3.5.3排查程序错误的方法
# 1.最简单的方法是在程序中插入print()函数，输出中间值进行调试，但是效率低。
# 2.使用Python编译调试工具：Pycharm\Spyder
# 具备断点设置、单步模式、变量查看、表达式计算等一系列调试功能，比较高效。
# eg:判断输入的一个整数是否为质数
# 解释：由于最小的因数是2，所以当小于整数一半的整数都不是这个数的因数时，这个数就是质数。
number=int(input("请输入一个整数："))
for i in range(2, number//2): # a//b:=b除a得到的商
    if number%i==0: # a%b:=b除a得到的余数
        break;
if i>number//2:
    print("%d 是一个质数" % number)
else:
    print("%d 不是一个质数" % number)
# 以上写法错误，在第一个if行断点调试，最后一次循环时，i=7，导致进入else语句。
# 更改为：
number=int(input("请输入一个整数："))
for i in range(2, number//2+1): # a//b:=b除a得到的商  # 这里更改为range(2,number//2+1)，因为括号()内左闭右开。
    if number%i==0: # a%b:=b除a得到的余数
        break;
if i>number//2:
    print("%d 是一个质数" % number)
else:
    print("%d 不是一个质数" % number)

# 另一种比较原始的方法（不过两种都没有考虑到1）：
number=int(input("请输入一个整数："))
for i in range(2,number//2):
    if number%i==0:
        print("%d 不是一个质数" % number)
        break
else:
    print("%d 是一个质数" % number)  #【】


# 3.5.4程序运行中try-except 异常处理】】】】】】】
# 1.try-except 结构：
# 书写格式：
# try:
#     <正常语句块A>
# except <错误名字1>:
#     <异常处理语句块B>
# eg:
    try:
        fobj= open("test.txt","r")  # 这里写可能出现错误的任何代码
    except IOError:  # 这里写可能出现的代码错误，不会直接产生报错  # IOError是输入输出错误
        print("文件打开失败")  # 这里写代码报错后的处理方式
# 2.try-except-else 结构：
# eg:
    try:
        num1=int(input("请输入分子："))
        num2=int(input("请输入分母："))
        num3=num1/num2
    except ZeroDivisionError as e:  # 本来ZeroDivisionError后面应该有()，这里不填(?)，但是可以except as
        print(e)
        print("除数为0")
    else:  # 如果上面的代码运行正常，那就执行else语句
        print(num3)
# 3.try-except-else-finally 结构
# eg:
    try:
        fobj= open("test.txt","r")
    except IOError:
        print("文件打开失败")
    else:
        print("文件打开成功")
        fobj.close()
    finally:  # 不管上面的代码是否运行正常，finally语句都会运行
        print("文件测试结束")






















































































