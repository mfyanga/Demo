#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iostream>
using namespace std;

class LimitData {
public:
  LimitData(double start, double end, double limit):start_s_(start), end_s_(end), limit_v_(limit) {
  }
  double start_s() { return start_s_; }
  double end_s() { return end_s_; }
  double limit_v() { return limit_v_; }

  double start_s_ = 0.0;
  double end_s_ = 0.0;
  double limit_v_ = 0.0;
};

double ComputeLimitDL(double v){
  constexpr double kMaxDL = 0.11;
  constexpr double kMinDL = 0.04;
  constexpr double kMaxV = 17.0;
  constexpr double kMinV = 7.0;

  double dl = kMaxDL - (kMaxDL - kMinDL)/(kMaxV - kMinV) * (v - kMinV);
}

int main(int argc, char **argv)
{
    vector<pair<int, string>> vecInt = {{1, "test1"}, {2, "test2"}, {3, "test3"}, {11, "test4"}, {18, "test5"}};

    int sum = 0;
    sum = std::accumulate(vecInt.begin(), vecInt.begin() + 3, sum, [](int a, const pair<int, string> &item){ return a + item.first;});
    std::cout << "sum = " << sum << std::endl;
    for (const auto &pairValue : vecInt)
    {
        cout << "{" << pairValue.first << ","<< pairValue.second << "}"<< endl;
    }   

    auto compare_s_upper = [] (int s, const pair<int, string> &point) { return point.first < s;};
    auto compare_s_lower = [] (const pair<int, string> &point, int s) { return point.first <  s;};

    auto it_lower = lower_bound(vecInt.begin(), vecInt.end(), 4, compare_s_lower);
    cout << "after lower_bound 4: {" << it_lower->first <<  "," << it_lower->second << "}" << endl;
    auto it_upper = upper_bound(vecInt.begin(), vecInt.end(), 4, compare_s_upper);
    cout << "after upper_bound 4: {" << it_upper->first <<  "," << it_upper->second << "}" << endl;   
 
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


    std::vector<int> datas = {10,20,5,4,3,100,70};
    std::cout << "Print origin datas:" << std::endl;
    for (const auto &d : datas){
       std::cout << d << "\t";
    }
    std::cout << std::endl;
     
    int con_data = 10;
    std::cout << "con_data = " << con_data << std::endl;
    auto itr = std::remove_if(datas.begin(), datas.end(), [con_data](int d) {return d < con_data;});
    std::cout << "Print after remove datas:" << std::endl;
    for (const auto &d : datas){
       std::cout << d << "\t";
    }
    std::cout << std::endl;
    
    std::cout << "Print data after the itr after remove return." << std::endl;
    for (auto it = itr; it != datas.end(); ++it) {
       std::cout << *it << "\t";
    }    
    std::cout << std::endl;
    std::cout << "Test the ralation between speed and limit dl" << std::endl;
    for (double v = 7.0; v < 17.10; v += 0.4) {
       std::cout << "v = " << std::to_string(v) << ", limit dl = " << ComputeLimitDL(v) << std::endl;
    }
    

    std::vector<double> s = {1.0, 2.0, 3.5, 4.0, 6.5, 7.8};
    const auto &iter_double = std::lower_bound(s.begin(), s.end(), 4.0, [](double v, const double &data) { return (data - v) > 0;}); 
    std::cout << "*iter_double = " << std::to_string(*iter_double) << std::endl;

    const auto &iter_double2 = std::upper_bound(s.begin(), s.end(), 4.0);
    std::cout << "*iter_double2 = " << std::to_string(*iter_double2) << std::endl; 
       
    std::vector<LimitData> speed_limits;
    speed_limits.push_back({0.0, 10.0, 2.0});
    speed_limits.push_back({10.0, 20.0, 4.0});
    speed_limits.push_back({20.0, 30.0, 5.0});
    speed_limits.push_back({30.0, 50.0, 10.0});
    
    double m_s = 8.0;
    auto compare = [](const LimitData& d, const double match_s) { return d.start_s_  <=  match_s; };
    auto iter = std::lower_bound(speed_limits.begin(), speed_limits.end(), m_s, compare);
    // auto iter = std::find_if(speed_limits.begin(), speed_limits.end(), compare);
    if (iter == speed_limits.end()) {
      std::cout << "not find." << std::endl;
    } else {
      std::cout << m_s << ", [" << iter->start_s() << ", " << iter->end_s() << ", " << iter->limit_v() << "]" << std::endl;
    }
    return 0;
}
