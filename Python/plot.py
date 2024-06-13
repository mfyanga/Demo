#!/usr/bin/python3
#-*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

print("你好")

print(matplotlib.matplotlib_fname())

plt.rcParams["font.family"]="SimHei"
list_tuples = zip([1,2,3],[0.1,0.2,0.3])
data = dict(list_tuples)

#1.Create canvas
fig = plt.figure(num = 1, figsize = (4, 4))

#2.Divide the canvas into four areas of 2 * 2 and select the 1s area as  ax1
ax1 = fig.add_subplot(221)
ax1.scatter(data.keys(), data.values())

#select the 2s area as ax2
ax2 = fig.add_subplot(224)
ax2.plot(data.keys(), data.values())

app = [70, 30, 100, 76, 12, 45, 99]
ax3 = fig.add_subplot(223)
x = np.arange(1, 8)
ax3.plot(x, app)
ax3.set_xlim([0, 8])
ax3.set_ylim([0, 100])
ax3.set_xticks(np.linspace(1,7, 7))
ax3.set_yticks(np.linspace(30,100, 7))

ax3.set_xticklabels(["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"], fontproperties="SimHei", fontsize=12, rotation=45)

plt.show()
