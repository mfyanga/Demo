#!/usr/bin/python
#coding=utf-8

print "Hellow world."
print "大家好！"

#1.标识符：以字符、数字、下划线组成，区分大小写,但不能以数值开头
# _var:不能直接访问的类属性，需要专门的接口访问，不能采用 from xx import * 导入
#__var:表示类的私有成员
#__var__:特殊方法专用的标识符，如类的构造函数__init__()
if True:
    print("True")
else:
    print("False")
print("没有严格的缩进")

raw_input("按下enter键退出，其他任意键显示...\n")

'''一行写多条语句'''
import sys;x = "runoob";sys.stdout.write(x + '\n')
import os
import math
import cmath
import support

def PrintInfo(*var_list):
    print "输出"
    #print "arg:",arg
    
    for var in var_list:
        print "var = ",var


def AddMoney():
    global money
    money += 19
    print "money:",money
    print "globals:"
    print globals()
    print "locals:"
    print locals()

def main():
    print 'main'

money = 100.0
if __name__ == '__main__':
    main()
   
    print '数到10'
    for i in range(10):
        print 'i = %s'%(i),

    fruit = ['苹果', '杏子', '梨子', '桃子']
    for i in fruit:
        print '水果:' + i
    
    print '这将直接执行'+os.getcwd()   
    
    a = b = c = 1
    print 'a = %s, b = %s, c = %s'%(a, b, c)
    a = 10
    print 'a = %s, b = %s, c = %s'%(a, b, c)
   
    dic = {'first':'1', 'second':'2'}
    print dic
    print dic.keys()
    print dic.values()
    
    n  = 2
    print type(n)
    
    print '########math info#############'   
    print dir(math)
    print '########cmath info############'
    print dir(cmath)

    PrintInfo(10)
    PrintInfo(20,30,40)
   
    print "Test module"
    support.print_func("module")
    
    print "money:", money
    money += 19;
    print "money:", money
    
    AddMoney() 
    print dir(support)
