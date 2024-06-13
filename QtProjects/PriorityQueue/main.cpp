#include <QCoreApplication>
#include <QDebug>
#include <queue>
#include <vector>
#include <QString>
#include<string>

class Node{
public:
    Node(double x, double y):x_(x), y_(y){
    }

    bool operator<(const Node& n){
        return this->x_ < n.GetX();
    }

    const double& GetX() const {
        return x_;
    }

    const double& GetY() const {
        return y_;
    }
 private:
    double x_ =0.0;
    double y_ = 0.0;
};

struct ComP{
    bool operator()(const Node& left, const Node& right){
        return left.GetX() < right.GetX();
    }
};

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    qDebug() << "Hello priority queue.";

    std::string debug_str = "Test std::priority_queue<int, std::vector<int>, std::less<int>>";
    qDebug() << QString::fromStdString(debug_str);
    std::priority_queue<int, std::vector<int>, std::less<int>> int_pq;
    int_pq.push(100);
    int_pq.push(3);
    int_pq.emplace(200);
    while (!int_pq.empty()) {
        auto data = int_pq.top();
        qDebug() << data;
        int_pq.pop();
    }

    debug_str = "Test std::priority_queue<Node, std::vector<Node>>";
    qDebug() << QString::fromStdString(debug_str);

    auto comp_fun = [](const Node& left, const Node& right)->bool{
        return left.GetX() < right.GetX();
    };
    std::priority_queue<Node, std::vector<Node>, ComP> node_pq;
//    std::priority_queue<Node, std::vector<Node>, comp_fun> node_pq;
    Node n1(1.0, 2.0);
    node_pq.emplace(n1);

    Node n2(3.0, 2.0);
    qDebug() << (n1 < n2);
    node_pq.emplace(n2);

    Node n3(-1.0, 2.0);
    node_pq.emplace(n3);

    Node n4(8.0, 2.0);
    node_pq.emplace(n4);

    while (!node_pq.empty()) {
        auto data = node_pq.top();
        qDebug() << "(" << data.GetX() << "," << data.GetY() << ")";
        node_pq.pop();
    }

    return a.exec();
}
