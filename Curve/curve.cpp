#include <cmath>
#include <iostream>
#include <vector>

struct Point {
  double x, y;
};

// 计算两点之间的距离
double distance(const Point& p1, const Point& p2) {
  return sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
}

// 计算航向
double heading(const Point& p1, const Point& p2) {
  return atan2(p2.y - p1.y, p2.x - p1.x);
}

// 计算曲率
double curvature(const Point& p1, const Point& p2, const Point& p3) {
  double k1 =
      2 * ((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y));
  double k2 =
      pow((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y), 1.5);
  return k1 / k2;
}

int main() {
  // 假设points是描述曲线的点的向量
  std::vector<Point> points = {/* 在这里填入您的点的坐标 */};

  for (int i = 1; i < points.size() - 1; ++i) {
    double head = heading(points[i - 1], points[i]);
    double curv = curvature(points[i - 1], points[i], points[i + 1]);

    // 计算曲率变化率
    double curv_change_rate =
        (curvature(points[i - 1], points[i], points[i]) -
         curvature(points[i], points[i + 1], points[i + 1])) /
        distance(points[i - 1], points[i + 1]);

    // 打印每个点的航向、曲率和曲率变化率
    std::cout << "Point " << i << ": Heading = " << head
              << ", Curvature = " << curv
              << ", Curvature Change Rate = " << curv_change_rate << std::endl;
  }

  return 0;
}