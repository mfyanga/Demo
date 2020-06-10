#!/usr/bin/python
import matplotlib.pyplot as plt

list_tuples = zip([1,2,3],[0.1,0.2,0.3])
data = dict(list_tuples)
fig, ax = plt.subplots()
ax.scatter(data.keys(), data.values())
plt.show()
