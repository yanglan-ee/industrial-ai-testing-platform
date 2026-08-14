# ResNet18 weight auto download script
import os
import torch
import torchvision.models as models

WEIGHT_PATH = "./src/utils/weights/resnet18.pth"

def download_model_weight():
    save_dir = os.path.dirname(WEIGHT_PATH)
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print("Weight folder created")
    except PermissionError:
        print("权重文件夹创建失败，请检查文件夹权限")
        return ""

    print("Start downloading ResNet18 pretrained weights...")
    try:
        model = models.resnet18(pretrained=True)
        torch.save(model.state_dict(), WEIGHT_PATH)
        print(f"Download complete, path: {WEIGHT_PATH}")
        return WEIGHT_PATH
    except Exception:
        print("模型下载失败，请检查网络后重新运行")
        return ""


if __name__ == "__main__":
    download_model_weight()