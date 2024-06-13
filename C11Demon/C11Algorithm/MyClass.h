//#ifndef MYCLASS_H
//#define MYCLASS_H
#pragma once

class MyClass {
public:
    MyClass();

    void Test(int a);
//private:
    template<typename T>
    void templateFunction(T param);
};
 
//#endif // MYCLASS_H
