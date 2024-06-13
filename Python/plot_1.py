#!/usr/bin/python3
#-*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print("你好")
# 定义参数
x0 = 3.0  # lower_point的x坐标
y0 = 2.0  # lower_point的y坐标
delta_s = 1  # 与lower_point的距离
theta_0 = np.pi/2.54  # lower_point的航向角
inter_heading = np.pi/3  # p点的航向角

# 定义角度范围
theta = np.linspace(0, 2*np.pi, 100)

# 计算函数值
p_x = x0 + delta_s * np.cos(inter_heading + theta_0)
p_y = y0 + delta_s * np.sin(inter_heading + theta_0)

# 绘制图形
plt.figure(figsize=(15, 5))

# 绘制 p_x = x0 + delta_s * cos(inter_heading + theta_0)
plt.subplot(1, 3, 1)
plt.plot(theta, x0 + delta_s * np.cos(inter_heading + theta + theta_0), label='p_x = x0 + delta_s * cos(inter_heading + theta_0)')
plt.xlabel('theta')
plt.ylabel('p_x')
plt.title('p_x = x0 + delta_s * cos(inter_heading + theta_0)')
plt.legend()

# 绘制 p_y = y0 + delta_s * sin(inter_heading + theta_0)
plt.subplot(1, 3, 2)
plt.plot(theta, y0 + delta_s * np.sin(inter_heading + theta + theta_0), label='p_y = y0 + delta_s * sin(inter_heading + theta_0)')
plt.xlabel('theta')
plt.ylabel('p_y')
plt.title('p_y = y0 + delta_s * sin(inter_heading + theta_0)')
plt.legend()

# 绘制 lower_point和p点的连线
plt.subplot(1, 3, 3)
plt.plot([x0, p_x], [y0, p_y], 'b--')  # lower_point到p点的连线
plt.plot(x0, y0, 'ro', label='lower_point')  # lower_point的位置
plt.plot(p_x, p_y, 'bo', label='p')  # p点的位置
plt.xlim(-1, 2)
plt.ylim(-1, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle Function Graph')
plt.legend()

plt.show()
