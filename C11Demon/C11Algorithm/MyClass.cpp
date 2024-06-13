#include "MyClass.h"

#include<iostream>
 
MyClass::MyClass() {
}

void MyClass::Test(int a) {
    templateFunction(a);
}
template<typename T>
void MyClass::templateFunction(T param) {
    // 模板函数的实现
    std::cout << "MyClass::templateFunction() param = " << param << std::endl;
}
