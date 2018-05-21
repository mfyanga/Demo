#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    vector<pair<int, string>> vecInt = {{1, "test1"}, {2, "test2"}, {3, "test3"}, {11, "test4"}, {18, "test5"}};
    for (const auto &pairValue : vecInt)
    {
        cout << "{" << pairValue.first << ","<< pairValue.second << "}"<< endl;
    }   

    auto compare_s = [] (const pair<int, string> &point, int s) { return point.first < s;};
    //auto compare_s = [] (const pair<int, string> &point, int s) { return point.first >  s;}; error result

    auto it_lower = lower_bound(vecInt.begin(), vecInt.end(), 4, compare_s);
    cout << "after lower_bound 4: {" << it_lower->first <<  "," << it_lower->second << "}" << endl; 
    
    vector<pair<int, int>> vecIntRange = {{1, 3}, {2, 4}, {3, 5}, {11, 13}, {6, 10}};
    cout << "before sort vector<pair<int, int>>:" << endl;
    std::for_each(vecIntRange.begin(), vecIntRange.end(), [](pair<int, int> &data) { cout << "{" << data.first << "," << data.second << "}";});

    std::sort(vecIntRange.begin(), vecIntRange.end());  
    cout << "\nafer sort vector<pair<int, int>>:" << endl;
    std::for_each(vecIntRange.begin(), vecIntRange.end(), [](pair<int, int> &data) { cout << "{" << data.first << "," << data.second << "}";});
    cout << endl;
    //{1,3}{2,4}{3,5}{6,10}{11,13}
    std::size_t i = 0;
    std::size_t j = i + 1;
    while (j < vecIntRange.size()) 
    {
        if (vecIntRange.at(i).second < vecIntRange.at(j).first) 
        {
          ++i;
          ++j;
        }
        else 
        {
            vecIntRange.at(i).second = std::max(vecIntRange.at(i).second, vecIntRange.at(j).second);
            ++j;
        }
    }
    vecIntRange.resize(i + 1);
    cout << "afer sort agin:" << endl;
    std::for_each(vecIntRange.begin(), vecIntRange.end(), [](pair<int, int> &data) { cout << "{" << data.first << "," << data.second << "}";});
    cout << endl;
    cout << "std::floor(4.98) = " << std::floor(4.98) << endl;
    cout << "std::ceil(4.98) = " << std::ceil(4.98) << endl;
    return 0;
}
