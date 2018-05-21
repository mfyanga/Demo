#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <functional>
#include <list>
#include <algorithm>

bool Cmp(int a, int b)
{
    std::cout << "Cmp(int a, int b)" << std::endl;
    return a < b;
}

class CFuctor
{
public:
    bool operator() (int a, int b)
    {
        std::cout << "CFuctor::operator()(int a, int b)" << std::endl;
        return a < b;
    }

};

int main()
{
    std::vector<int> vecInts1{4, 7, 2, 8, 123, 9};
    std::vector<int> vecInts2(vecInts1);
    
    auto startTime = std::chrono::steady_clock::now();
    std::sort(std::begin(vecInts2), std::end(vecInts2), [](int a, int b){ return a < b; });
    for (auto &value : vecInts2)
    {
        std::cout << value << "\t";;
    }
    auto end_time = std::chrono::steady_clock::now();
    std::cout << "\nIt takes me " << std::chrono::duration_cast<std::chrono::microseconds>(end_time - startTime).count() << "us\n";
 

    startTime = std::chrono::steady_clock::now();
    std::sort(vecInts1.begin(), vecInts1.end(), Cmp);
    for (auto &value : vecInts1)
    {
        std::cout << value << "\t";;
    }
    end_time = std::chrono::steady_clock::now();
    std::cout << "\nIt takes me " << std::chrono::duration_cast<std::chrono::microseconds>(end_time - startTime).count() << "us\n";
    
  
    int a = 10;
    auto f = [a] { std::cout<< "a = " << a << std::endl;};    
    f();
     
    //隐式值捕获
    auto f1 = [=] { std::cout << "lambda::f1 a = " << a << std::endl; };
    auto f2 = [&] { std::cout << "lambda::f2 a = " << ++a  << std::endl; };
    a = 321;
    f1();
    f2();
    auto f3 = [a] () mutable { std::cout << "lambda::f3 a = " << ++a << std::endl; };
    f3();
    std::cout << "after lambda::f3 a =" << a << std::endl;
    
    //std::function<T>使用listCallFunction
    std::cout << "Test use std::function<>" << std::endl;
    CFuctor functor;
    std::list<std::function<bool(int, int)>> listCallFunction;
    using FUNCTION_TYPE = std::function<bool(int, int)>;
    //使用函数对象
    listCallFunction.push_back(functor);
    //使用C函数
    listCallFunction.push_back(Cmp);
    //使用Lambda表达式
    listCallFunction.push_back([](int a, int b)->bool { 
        std::cout << "lambda [](int a, int b)->bool {}" << std::endl;
        return a < b; });
    std::for_each(listCallFunction.begin(), listCallFunction.end(), [](FUNCTION_TYPE &obj){ obj(3, 4);});
    

    return 0;
}
