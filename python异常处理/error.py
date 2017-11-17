#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("D:/1/testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
    



#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("D:/1/testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print "Error: 没有找到文件或读取文件失败"





#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "shutdown file"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"




#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        

try:
    mye(0)                
except "Invalid level!":
    print 1
else:
    print 2
