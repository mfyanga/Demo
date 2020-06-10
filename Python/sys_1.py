#!/usr/bin/python
#coding=utf-8
import sys
import os


if __name__=="__main__":
    print "main"
    sys.stdout.write("sys.platform()\n")
    print sys.platform
    if sys.platform.startswith('linux'):
        print "linux"
    sys.stdout.write("please input:\n")
    line = sys.stdin.readline()
    print line
    
    dictionary = os.environ
    for key in dictionary.keys():
        print key,"=",dictionary[key]
else:
    print "common module"
