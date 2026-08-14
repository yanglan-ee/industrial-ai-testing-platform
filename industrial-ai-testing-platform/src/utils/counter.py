# -*- coding: utf-8 -*-
# 推理次数计数器，记录模型推理总次数
class InferCounter:
    def __init__(self):
        # 初始化计数
        self.total_num = 0

    def add(self):
        # 推理一次，数字加1
        self.total_num = self.total_num + 1
        return self.total_num

    def reset_num(self):
        # 清空计数
        self.total_num = 0

    def get_total(self):
        # 返回当前总次数
        return self.total_num

    def get_data(self):
        # 给报告工具提供数据
        info = {
            "推理总次数": self.total_num
        }
        return info

# 全局计数器，整个项目共用
count_tool = InferCounter()