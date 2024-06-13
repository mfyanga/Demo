# 感知数据结构说明

感知信息分为障碍物，地图，定位三部分，以下分开说明

```
message LocalDynamicMap {
  optional citibot.common.message.Header header = 1;
  //感知障碍物
  optional PerceptionObstacles perception_obstacles = 2;  // An array of obstacles
  //地图信息
  optional citibot.common.hdmap.Map map = 3;
  //定位信息
  optional citibot.localization.LocalizationEstimate localization = 4;
}
```

## 地图信息

地图信息在感知信息里面的字段为map，这个字段正常情况需要填写，如果不填则没有任何地图信息，规控需要紧急停车

为了适配后续更复杂的场景，采用了地图标准的格式，在L2基础场景下，由于场景简单，很多中间层可以跳过，具体使用规则说明如下：

| 字段            | 解释                                                                                                                                                |
| ------------- |:------------------------------------------------------------------------------------------------------------------------------------------------- |
| road          | 道路，数组，L2正常最多只有一条道路，多于一个只管第一个                                                                                                                      |
| section       | 路段，数组，L2正常只有一段路，多于一个只管第一个                                                                                                                         |
| boundary      | 道路边界，最多只有一个，里面包含一个outer_polygon和多个不可行驶的洞（L2暂不用考虑）                                                                                                 |
| outer_polygon | 道路边界的外边缘结构，最多只有一个，里面包含多个edge                                                                                                                      |
| edge          | 路沿的结构，数组，正常最多2个（即左右边界），进行贴边算法时需要遍历找出左右边界，里面包含系数，起点终点等，起点一般从0开始，特别注意：系数需要满足一定的合理性，包括帧间的变化，需是尽量平滑合理的曲线，规控对于不合理的轨迹可以紧急停车 |

对于以上规则

（1）如果是正常的感知未检测到造成的缺省，规控按未找到边界进行处理（不支持自动驾驶，减速停车）

（2）比如是不合理的填充，则规控可以进行报错，并紧急停车处理

map示例结构如下：

```
map {
  road {
    section {
      boundary {
        outer_polygon {
          edge {
            curve {
              segment {
                c0: 1.5
                c1: 0
                c2: 0
                c3: 0
                start: 0
                end: 30
              }
            }
          }
          edge {
            curve {
              segment {
                c0: -1.5
                c1: 0
                c2: 0
                c3: 0
                start: 0
                end: 30
              }
            }
          }
        }
      }
    }
  }
}
```
