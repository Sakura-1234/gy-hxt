# print("hello world")
#
# a="hello world1"
# print(a)
# a="hello world"
# b="good morning"
# c="surprise morther fuck"
# print(a,b,c)
# print(a)
# print(b)
# print(c)
# l=[1,2,3,4,5]
# print(l[0])
# print(l)
# t=(1,2,3,4,5)
# print(t[0])
# print(t)
# s={1,2,3,4}
# print(s)
#
#
# a=10
# b="2"
# print(a+int(b))
# print(str(a)+b)
#
# a=10
# b="2.1"
# print(a+float(b))
# print(str(a)+b)
#
# a= True
# b=10
# print(a+b)
#
# a=False
# b=22
# print(a+b)
# d={"name":"王大锤","age":18}
# print(d)
# print(d["name"])
#
# l=[1,2,3,4,5]
# print(set(l))
# print(tuple(l))
#
# s={1,2,3,4,5}
# print(list(s))
# print(tuple(s))
#
# t=(1,2,3,4,5)
# print(list(t))
# print(set(t))
#
# a="12345678"
# print(list(a))
# print(set(a))
# print(tuple(a))
#
#
# a="lixiaolong"
# l=["x","a","c"]
# s={"x","a","c"}
# t=("x","a","c")
# d={"name":"李小龙","sex":"女" }
# print("x" in a)
# print("x" in l)
# print("x" in s)
# print("x" in t)
# print("name"in d)
#
# money=1.5
# if(money>=1.5):
#     print("买辣条")
# else:
#     print("喝西北风")
#
# a = 10
# # a = 1 - a  不可简写
# # a = a -1  可以写成 a -= 1
# a -= 1
# print(a)
#
# money=1
# if(money<1.5):
#     print("买辣条")
# elif(money<3):
#     print("买汽水")
# elif(money<10):
#     print("买薯片")
# else:
#     print("吃包子")
#
#
# for i in [1,2,3,4,5,6]:
#     print(i)
#     print("重要的事情要说100遍！")
#
# for i in range(100):
#     print("重要的事情要说100遍！")
#
#
# print(list(range(100)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,0,-1)))
# print(list(range(10,0,-2)))

# while True :
#     print("hello")

# for i in range(1,11):
#     if (i == 7):
#      continue
#     print(i)
# for i in range(1,11):
#     if(i in [5,7]):
#       continue
#       print(i)

# for x in range(1, 9):
#           y = 1
#           while y <= x:
#               print("%s*%s=%s" % (y, x, x * y), end=" ")
#               y += 1
#           print("")

# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%s*%s=%s" % (y,x,x*y),end=" ")
#     print("")#print
# print('\n'.join(['\t'.join(["%2s*%2s=%2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))
#
# list = []
# while True:
#     # 自定义输入数字个数
#     print('10')
#     try:
#         num = int(input())
#         for i in range(num):
#             a = int(input('请输入第' + str((i + 1)) + '个整数：'))
#             list.append(a)
#     except ValueError:
#         print('输入有误！')
#
#     # 冒泡排序核心代码，
#     for j in range(len(list) - 1):
#         for k in range(len(list) - 1):
#             if list[k] < list[k + 1]:
#                 t = list[k]
#                 list[k] = list[k + 1]
#                 list[k + 1] = t
#
#     print(list)
#
#     L = [3, 5, 7, 9, 2, 4, 6, 0]
#     L.sort()
#     for i in L:
#         print(str(i) + ' ', end='')

def div(a,b):
    if b==0:
        print("被除数不能为0")
    else:
        print(a/b)

div(2,9)
div(3,5)
div(9,10)


def select_data(sql):
    res='查询结果'
    return res
a=select_data("")
print(a)

#参数定义

#位置参数 调用是，参数有一个传一个
def s(a,b):
    return a+b
print(s(3,2))

#关键字参数 给参数设置默认值，
#如果调用时没有传参数则用默认值
#关键字、位置同时存在时，位置参数在前边，关键字参数在后边
def s(a=1,b=2):
     return  a+b
print(s(1,3))
print(s(1))
#调用参数
#按照位置传参
print(s(1,2))
#按照关键字传参
print(s(b=20))
#位置和关键字同时存在，位置在前，关键字灾后
print(s(10,b=22))
#print(s(10,a=20))错误，不能对同一个变量重复传参


#动态参数定义

# def ar(a,*args,b=10,**kwargs):
#     print(args)
#     print(kwargs)
# ar(1,2,3,4,c=10,b=2)

# def case(a,b=2):
#     print(a)
#     print(b)
#     print("这是一个测试用例")
#
# def log(func,*args,**kwargs):
#     print("用例参数",args,kwargs)
#     r=func(*args,**kwargs)
#
#     print("用例结果",r)
# log(case,10,20)

#操作文件
# f=open("a.txt","w")#以写入的形式打开文件
# f.write("hello哈哈哈")#写入数据
# f.close()#关闭文件
#
# f=open("a.txt","r")
# e=f.read()
# print(e)
# f.close()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,'=',i*j,end='\t')
#     print()
#
# c=10
# def aaa():
#      global c
#      c=20
#
#
# aaa()
# print(c)


#字符串
# a="1234567890"
# b="456"
# print(a[0])
# print(a[2:6])
# print(a[:6])
# print(a[4:])
# print(a[-2:])
# print(a[1:-2])

# a="  dsad  "
# a=a.strip()
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# line="用例名，账户名，充值金额，预期结果"
# line=line.replace("，",",")
# print(line)
# print(line.split(','))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} x {} = {}".format(j,i,i*j),end='\t')
#     print()


#遍历列表
# l = [1,2,3,4,5,6,7,8]
#
# l[0]=20#根据下表修改列表元素的值
# l.append(9)#往列表末尾添加数据
# l.insert(2,30)#根据下标往列表中插入数据
# l.extend((1,2,3,4,5))#往列表末尾添加多个数据
# l.pop()#根据下标删除数据
# l.pop(0)#根据下标删除数据
# l.remove(2)#根据内容删除列表中的数据，有重复只会删除第一个
# print(l.index(6))#查询某个元素的下标，多个值，至查询第一个
# l.sort()#默认升序，会修改原列表中的数据
# l.sort(reverse=True)#降序l 1




# print(l)

# l = [10,1,35,61,89,36,55]
# # 依次比较相邻的两个数据，如果前边的数据比后边的大， 则交换两个数据的位置，直到把最大的数据都放到最后第一次排序结束，
# # 第二次排序重复第一次排序的动作，把第二大的放到倒数第二的位置，依次类推，直到所有的数据都排好序为止
#
#
# l = [10,1,35,61,89,36,55]
# # 依次比较相邻的两个数据，如果前边的数据比后边的大， 则交换两个数据的位置，直到把最大的数据都放到最后第一次排序结束，
# # 第二次排序重复第一次排序的动作，把第二大的放到倒数第二的位置，依次类推，直到所有的数据都排好序为止
#
#
# for i in range(len(l)-1,0,-1): # i代表最后一个未排好序的数据下标
#     for j in range(0,i): # j 代表每次循环时，当前位置的下标
#         if(l[j] > l[j+1]): # 比较当前位置和下一个位置的数据大小，如果当前位置大于下个位置，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]  # 交换两个数据的位置
#
# print(l)


# #创建一个类
# class str_deom():
#     s=None
#
#     def replace(self):
#         print("字符串替代")
#
#     def split(split):
#          print("字符串切割")
#
# sd=str_deom()#实例化 sd就是一个对象
# sd.s="hello"
# sd.replace()
# sd.split()
#
# class str_demo():
#
#     # 不需要显式调用，程序自动调用的
#     def __init__(self):
#         print("魔法方法")
#
#     # 实例方法
#     def replace(self):
#         print("实例方法")
#         pass
#
#     @classmethod # 装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static():
#         print("静态方法")
#
#
#
# # 类外部调用方法
# str_demo.split() # 调用类方法
# str_demo().replace() # 通过对象调用实例方法
# str_demo.static() # 通过类名调用静态方法
# str_demo().static() # 通过对象调用静态方法
# str_demo() # 调用__init__魔法方法
#
# class privateDemo():
#     _a=None
#
#     def set_a(self,value):
#         self._a=value
#     def get_a(self):
#         return self._a
# p=privateDemo()
# p.set_a("hello")
# print(p.get_a())



import requests

#编写一个返回随机手机号的方法
def fff():
    import random
    s= random.choices(["153","189"],k=1)
    E="".join(s)
    l = random.choices("91929001",k=8)# 在指定集合中，随机获取一组数据

    d = "".join(l)
    print(E+d)
fff()

#编写一个返回指定长度和内容的随机字符串方法
def aaa():
    import random
    l = random.choices("0123456789asdfg",k=10)
    return print("".join(l))
aaa()
#编写一个随机姓名的方法
import random
l = random.choices("胡程方赵钱孙李周武郑王")
F="".join(l)
O=  random.choices("晓超鱼天房安琪越黄成")
E="".join(O)
print(F+E)

print("asdf")
try:
    # r=open("b.txt","r")#FileNotFoundError
    print(1/2)#ZeroDivisionError
except (FileNotFoundError) as  e:
    print(e)
    print("程序执行遇到了问题")
    print("重新打开文件")
except ZeroDivisionError as e :
    print("除数不能为0")
else:
    print("程序运行没报错")
finally:("不管程序有没有报错都会运行")

print("文件已经打开")

程超大SB
 陈超 喜欢 奥里给 ，小啊giao

