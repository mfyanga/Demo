#include <iostream>

#include "MyClass.h"

int main(int argc, char **argv)
{
     MyClass obj;
     int param = 8;     
     // obj.Test(param);
     obj.templateFunction(param);

     std::string s = "hello world.";
     obj.templateFunction(s);
    return 0;
}
