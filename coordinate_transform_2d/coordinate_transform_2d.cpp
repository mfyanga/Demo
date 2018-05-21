// Author: David Hopper
// E-mail: davidhopper@qq.com

#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <random>

struct Point {
  explicit Point() : x(0.0), y(0.0) {}
  explicit Point(double x_i, double y_i) : x(x_i), y(y_i) {}
  double x;
  double y;
};

// 2D coordinate transform
void CoordinateTransform2D(std::vector<Point>& points, double x_shift,
                           double y_shift, double angle);

int main(int argc, char** argv) {
  double x_shift = 1.0;
  double y_shift = 1.0;
  double angle = M_PI / 4.0;

  // Parse parameters.
  if (argc > 3) {
    try {
      x_shift = std::stod(argv[1]);
      y_shift = std::stod(argv[2]);
      angle = std::stod(argv[3]);
    } catch (...) {
      std::cout << "Usage: \n"
                << "\t" << argv[0] << " x_shift y_shit angle(rad)" << std::endl;
      std::cout
          << "The default transform parameters: (1.0, 1.0, PI/4.0) are used. "
          << std::endl;
    }    
  } else {
    std::cout << "Usage: \n"
              << "\t" << argv[0] << " x_shift y_shit angle(rad)" << std::endl;
    std::cout
        << "The default transform parameters: (1.0, 1.0, PI/4.0) are used. "
        << std::endl;
  }
  
  angle = (M_PI / 180) * angle;

  constexpr int kSize = 1000;
  //std::vector<Point> points(kSize);
  std::vector<Point> points;

  /*
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<double> dis(-100.0, 100.0);
  auto rand_num([&]() mutable {
    Point point(dis(gen), dis(gen));
    return point;
  });
  

  std::generate(std::begin(points), std::end(points), rand_num);
  */
  // Add a special point (0, 0) to check the correctness of the result.
  points.emplace_back(0.0, 0.0);
  points.emplace_back(2.0, 4.0);
  points.emplace_back(3.0, 4.0);
  points.emplace_back(4.0, 5.0);
  points.emplace_back(4.0, 4.0);
  points.emplace_back(7.0, 4.0);
  points.emplace_back(8.0, 3.0);
  points.emplace_back(0.0, 0.0);
  points.emplace_back(-2.0, 4.0);
  points.emplace_back(3.0, -4.0);
  points.emplace_back(-4.0, -5.0);
  points.emplace_back(-4.0, 4.0);
  points.emplace_back(-7.0, 4.0);
  points.emplace_back(8.0, -3.0);

  std::cout << "Points before transformation: " << std::endl;
  for (const auto& point : points) {
    std::cout << "(" << point.x << ", " << point.y << "), ";
  }
  std::cout << std::endl;

  auto start_time = std::chrono::steady_clock::now();
  CoordinateTransform2D(points, x_shift, y_shift, angle);
  auto end_time = std::chrono::steady_clock::now();
  std::cout << "Elapsed time in milliseconds: "
            << std::chrono::duration_cast<std::chrono::microseconds>(end_time -
                                                                     start_time)
                   .count()
            << " µs" << std::endl;

  std::cout << "Points after transformation: " << std::endl;
  for (const auto& point : points) {
    std::cout << "(" << point.x << ", " << point.y << "), ";
  }
  std::cout << std::endl;

  return 0;
}

// 2D coordinate transform
// Original: XOY
// Transformed: X'O'Y':
//  Translation: (x_shift, y_shift)
//  Rotation: angle (rad)
// A coordinate represented in XOY: (x, y)
// A coordinate represented in X'O'Y': (x_prime, y_prime)
// Transform formula:
//  x = x_prime * cos(angle) - y_prime * sin(angle) + x_shift
//  y = y_prime * cos(angle) + x_prime * sin(angle) + y_shift
//  x_prime = (x - x_shift) * cos(angle) + (y - y_shift) * sin(angle)
//  y_prime = (y - y_shift) * cos(angle) - (x - x_shift) * sin(angle)
void CoordinateTransform2D(std::vector<Point>& points, double x_shift,
                           double y_shift, double angle) {
  std::transform(
      std::begin(points), std::end(points), std::begin(points),
      [=](const Point& point) {
        double sin_val = std::sin(angle);
        double cos_val = std::cos(angle);
        Point trans_point(
            (point.x - x_shift) * cos_val + (point.y - y_shift) * sin_val,
            (point.y - y_shift) * cos_val - (point.x - x_shift) * sin_val);
        return trans_point;
      });
}
