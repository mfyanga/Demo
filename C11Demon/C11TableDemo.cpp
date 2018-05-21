#include <iostream>
#include <list>
#include <vector>
using namespace std;

class CTest
{
public:
    CTest(int a):i(a)
    {
    }
    
private:
    int i = 0;
};

int main(int argc, char **argv)
{
    list<list<int>> table;
    cout << "table.size() = " << table.size() << endl; 
    cout << "table.back().size()=" << table.back().size() << endl;
    table.emplace_back();
    table.back().emplace_back(1);
    //table.back().emplace_back();
    cout << "table.size() = " << table.size() << endl;
    cout << "table.back().size()=" << table.back().size() << endl;
    table.emplace_back();
    table.back().emplace_back(2);
    cout << "table.size() = " << table.size() << endl;
    cout << "table.back().size()=" << table.back().size() << endl;
    
    //segment error
    /*
    list<list<int>> table1;
    table1.back().push_back(1);
    cout << "table1.size() = " << table1.size() << endl;
    cout << "table1.back().size()=" << table1.back().size() << endl;
    */
    list<int> list1;
    list1.push_back(1);
    cout << "list1.size()" << endl;

    vector<vector<int>> vecTable;
    vecTable.emplace_back();
    vecTable.back().push_back(1);
    cout << "vecTable.size() = " << vecTable.size() << " vecTable.capacity() = "<< vecTable.capacity() <<  endl;
    cout << "vecTable.back().size() = " << vecTable.back().size() << " vecTable.back().capacity() = " << vecTable.back().capacity() << endl; 
   
    vector<vector<int>> table2;
    cout << "table2.size() = " << table2.size() << endl;
    table2 = vector<vector<int>>(3, vector<int>(4, 10));
    cout << "table2.size() = " << table2.size() << endl;
    cout << "table2.back().size() = " << table2.back().size() << endl;
    for (auto &row: table2)
    {
        cout << "row.size() = " << row.size() << endl;
    } 

    double dValue = 1e2;
    double dVal = 2.0 + dValue;
    cout << "dValue = " << dValue << endl; 
    cout << "dVal = " << dVal << endl;

    vector<vector<int>> table3 = vector<vector<int>>(3, vector<int>(4, 1));
    cout << table3.size() << " " << table3.back().size() << endl;
   return 0;
}
