\# 模块统一调用接口文档

\## 一、模块导入统一规则

所有工具函数/类统一从 src.utils 目录导入

1\. 推理计数器模块

from src.utils.counter import InferCounter

2\. 模型权重下载模块

from src.utils.download\_resnet import download\_model\_weight



\## 二、参数统一规范

1\. 文件路径参数：全部使用字符串(str)类型

2\. 计数增量参数：全部使用整数(int)类型



\## 三、函数返回值规范

1\. InferCounter 计数器类

\- add()：返回int，当前累计推理总次数

\- get\_total()：返回int，读取当前总次数

\- reset\_num()：无返回值，计数器归零

\- get\_data()：返回dict，存储推理计数结构化数据

2\. download\_model\_weight() 下载函数

返回str，返回权重文件完整保存路径

