#!/usr/bin/python3
#coding=utf-8

print "你好，Emploee"

class Emploee:
    'Define class Emploee'
    emp_count = 0

    def __init__(self, name, salary):
        print "Enter __init__"
        self.name = name
        self.salary = salary
        Emploee.emp_count += 1

    def DispayCount(self):
        print "Enter DispayCount()"
        print "Total emploee count:%d" % Emploee.emp_count

    def DisplayEmploee(self):
        print "Enter DisplayEmploee()"
        print  "name: ", self.name, "salary: ", self.salary

    def Display(self):
        print "Enter Display"
        print(self)
        print(self.__class__)



if __name__ == "__main__":
    print "Emploee.emp_count = %d" % Emploee.emp_count
    print  Emploee.__doc__    

    print "\n ep_1:"
    ep_1 = Emploee("ymf", 10.0)
    ep_1.DispayCount()
    ep_1.DisplayEmploee()
    ep_1.age = 32
    print "ep_1.age = ", ep_1.age
    #print "Emploee.age = ", Emploee.age

    print "\n ep_2："
    ep_2 = Emploee("Ming", 20.0)
    ep_2.Display()

    ep_3 = ep_1
