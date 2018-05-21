#include<iostream>
#include<vector>
#include<string>
//#include <gflags/gflags.h>
#include <signal.h>
#include <cstddef>
#include <memory>
using namespace std;

void Handle(int iNum)
{
    cout << "signal num=" << iNum << endl;
    exit(0);
}

class CPerson
{
public:
    CPerson() = default;
    CPerson(string name, int age, bool sex)
    {
        m_strName = name;
        m_iAge = age;
        m_bSex = sex;
    }

    string GetName() const
    {
        return m_strName;
    }
 
    int GetAge() const
    {
        return m_iAge;
    }
    
    bool GetSex() const
    {
        return m_bSex;
    }
private:
    string m_strName;
    int m_iAge;
    bool m_bSex;
};

struct HowManeyBytes
{
    char a;
    int b;
};
int main(int argc, char **argv)
{
    cout << "Enter main()" << endl;
    char *pTest = "hellworld";
    cout << "pTest=" << pTest << endl;
    
    for (int i = 0; i < argc; ++i)
    {
        cout << argv[i] << endl;
    }

    int iArray[] = {10, 11, 13, 14};
    
    cout << "use for auto data : iArray!" << endl;
    for (auto data : iArray)
    {
         cout << data << "\t";
    }
    cout << endl;
 
    cout << "use begin() and end()" << endl;
    for (int *p = begin(iArray); p != end(iArray); ++p)
    {
        cout <<  *p <<  "\t";
    }
    cout << endl;
    
    cout << "Test CPerson" << endl;
    CPerson p;
    cout << "name = " << p.GetName() << endl;
    cout << "age = "  << p.GetAge() << endl;
    cout << "sex = "  << p.GetSex() << endl;

    cout << "Test vector emplace" << endl;
    CPerson p1("li", 23, 1);
    vector<CPerson> personVec;
    personVec.emplace_back("yang", 30, 0);
    for (auto& em : personVec)
    { 
        cout << "name = " << em.GetName() << endl;
        cout << "age = "  << em.GetAge() << endl;
        cout << "sex = "  << em.GetSex() << endl;
    }
    personVec.push_back(p1);
    cout << "personVec.capacity = " << personVec.capacity() << endl;
    personVec.shrink_to_fit();

   cout << "Test covert between digit and str" << endl;
   string strDigit = "12345";
   cout <<  stoi(strDigit) << endl;
   string str1 = "1234abc";
   size_t len = 4;
   cout <<  stoi(str1, &len, 8) << endl;

   cout << "Test use lambda" << endl;
   auto lambadaA = [len](){return len;}; 
   cout << lambadaA() << endl;

   cout << "Test right value referenc" << endl;
   int lValue = 2;
   int &&rReference = lValue * 43;
   cout << "rReference=" << rReference << " ++rReference=" << ++rReference << endl;
   /*
   signal(SIGTERM, Handle);
   while(1)
   {
   }
   */

   std::cout << "offset of char a:" << offsetof(HowManeyBytes, a) << std::endl;
   std::cout << "offset of int b:" << offsetof(HowManeyBytes, b)<<  std::endl;
   
   std::cout << " alignof(HowManeyBytes):" << alignof(HowManeyBytes) << std::endl;
   std::unique_ptr<CPerson> ptrPerson;
   if (!ptrPerson)
   {
       std::cout<< "before new !ptrPerson" << std::endl;
       std::cout << "name:" << ptrPerson->GetName() << std::endl;
   }

   ptrPerson = std::unique_ptr<CPerson>(new CPerson("yang", 12, true));
   if (!ptrPerson)
   {
      std::cout << "after new !ptrPerson" << std::endl;
   }
   else
   {
       std::cout << "name:" << ptrPerson->GetName() << std::endl;
   }
   return 0;
}
