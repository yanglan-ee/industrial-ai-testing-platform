自动化测试平台工具模块详细接口文档



模块1：推理计数器



文件存放路径：src/utils/counter.py

封装类名称：InferCounter



1\. 整体功能

全局推理次数统计工具，自动累计推理运行次数，支持查看总次数、一键清零，保证多次调用计数不混乱。

2\. 每一个函数详细说明

构造函数 init()

• 作用：创建计数器实例，初始化总推理次数为0

• 输入参数：无

• 返回内容：无

add()

• 作用：推理次数累加，每调用一次+1

• 输入参数：无

• 返回内容：整数，累加之后最新的推理总次数

get\_total()

• 作用：读取当前累计的推理总次数

• 输入参数：无

• 返回内容：整数，当前全部推理次数总和

reset\_num()

• 作用：清空计数器，总次数归零

• 输入参数：无

• 返回内容：无

get\_data()

• 作用：返回字典格式数据，供报告工具使用

• 输入参数：无

• 返回内容：字典，包含"推理总次数"键值对

3\. 代码调用示例

from src.utils.counter import InferCounter

\# 创建计数器

test\_counter = InferCounter()

\# 单次推理计数+1

test\_counter.add()

\# 查看总次数

total = test\_counter.get\_total()

print("当前推理总次数：", total)

\# 清空计数器

test\_counter.reset\_num()

4\. 异常提示说明

当前版本所有方法均无参数输入，不存在参数类型错误问题。



模块2：预训练权重自动下载工具



文件存放路径：src/utils/download\_resnet.py

封装函数名称：download\_model\_weight



1\. 整体功能

自动生成权重存放文件夹，在线下载ResNet18官方预训练权重，保存为pth文件，不用手动去网页下载模型。

2\. 函数详细说明

download\_model\_weight()

• 作用：下载ResNet18预训练权重并保存到本地

• 输入参数：无（保存路径由文件内常量WEIGHT\_PATH控制，默认./src/utils/weights/resnet18.pth）

• 返回内容：字符串，权重文件保存路径；出错时返回空字符串""（控制台打印下载进度和保存路径）

3\. 代码调用示例

from src.utils.download\_resnet import download\_model\_weight

\# 执行下载，接收返回的文件路径

save\_path = download\_model\_weight()

print("权重文件保存位置：", save\_path)

4\. 异常提示说明

1. 网络断开、下载超时：控制台报错，建议检查网络后重新运行

2\. 没有文件夹读写权限：控制台报错，建议检查文件夹权限

