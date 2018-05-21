#include <iostream>
//no this header file
//#include <cuchar> no 
#include <locale>
using namespace std;

int main(int atgc, char **argv)
{
    char utf8[] = u8"\u4F60\u597D\u554A";
    char16_t utf16[] = u"hello";
    char32_t utf32[] = U"hello equals \u4F60\u597D\u554A";
    
    cout << "utf8 = " << utf8 << endl;
    cout << "utf16 = " << utf16 << endl;
    cout << "utf32 = " << utf32 << endl;
    /*
    char16_t utf16_str[] = u"\u4F60\u597D\u554A";
    size_t nSize = sizeof(utf16_str);
    char mb_str[nSize * 2];
    mbstate_t s;
    c16rttomb(mb_str, utf16_str, &s);
    cout << "nSize = " << nSize << " mb_str = " << mb_str << endl;
    */
    
    //C++11 原生字符串，即所见及所得 R 
    cout << "hello \n world" << endl;
    cout << R"(hello \n world)" << endl;

    cout << u8R"(\u4F60\u597D\u554A)" << endl;
    cout << "你好" << endl;
    cout << u8R"(你好)" << endl;
    
    cout << sizeof(u8R"(hello)") << " : " << u8R"(hello)" << endl;
    cout << sizeof(uR"(hello)") << " : " << uR"(hello)" << endl;
    cout << sizeof(UR"(hello)") << " : " << UR"(hello)" << endl; 

    //C++对编码转换的新支持都要源自于C++的locale机制的支持
    //定义一个locale
    cout << "locale facet" << endl;
    locale lc("en_US.UTF-8");

    //查询lc是否支持一些facet
    if (!has_facet<codecvt<wchar_t, char, mbstate_t>>(lc))
    {
        cout << "Do not support muti char to wchar_t facet" << endl; 
    }

    if (!has_facet<codecvt<char, char, mbstate_t>>(lc))
    {
        cout << "Do not support muti char to char facet" << endl;
    }

    if (!has_facet<codecvt<char16_t, char, mbstate_t>>(lc))
    {
        cout << "Do not support utf-16 to utf-8 facet" << endl;
    }

    if (!has_facet<codecvt<char32_t, char, mbstate_t>>(lc))
    {
        cout << "Do not support utf-32 to utf-8 facet" << endl;
    }
    return 0;
}
