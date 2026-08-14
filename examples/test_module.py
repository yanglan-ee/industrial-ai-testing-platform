# 模块独立运行测试脚本
# 测试对象：src/utils下计数器、权重下载工具
from src.utils.counter import InferCounter
from src.utils.download_resnet import download_model_weight

def test_counter():
    """测试推理计数器全部功能"""
    print("===== 开始测试推理计数器 =====")
    # 初始化
    cnt = InferCounter()
    # 单次计数+1
    cnt.add()
    # 批量循环计数+5
    for _ in range(5):
        cnt.add()
    # 读取总数
    total = cnt.get_total()
    print(f"当前推理总次数：{total}")
    # 清空计数器
    cnt.reset_num()
    print(f"清空后计数：{cnt.get_total()}")
    print("===== 计数器测试完成，无报错 =====\n")

def test_download_model():
    """测试权重下载功能"""
    print("===== 开始测试权重下载工具 =====")
    save_path = download_model_weight()
    print(f"下载返回路径：{save_path}")
    print("===== 权重下载测试完成，无报错 =====\n")

if __name__ == "__main__":
    test_counter()
    test_download_model()