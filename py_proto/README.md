## 说明

本工程为使用`python`加载自定义`proto`文件示例，整个工程文件如下：

```shell
├── build_pb2.sh ##生成 py proto
├── common ## 自定义proto，可直接从platform中拷贝（请保持原目录结构）
│   └── message
├── example_pb2.py ## 加载py proto 示例工程
└── README.md ## 使用说明
```

**工程运行需要在docker内运行**，运行之前需要从`platform`中将`proto`拷贝至工程目录，并保持上述目录结构，拷贝完成后运行`bash build_pb2.sh`生成`py proto`，生成目录为`py_proto_gen`，生成后便可加载`proto`文件了，具体使用请参考`example_pb2.py`。
