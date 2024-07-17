import os
import shutil

# 源文件夹和目标文件夹路径
output_path = "output"
output_mer_path = "output_mer"
journals_path = os.path.join(output_mer_path, "journals")
assets_path = os.path.join(output_mer_path, "assets")

# 创建目标文件夹
if not os.path.exists(output_mer_path):
    os.makedirs(output_mer_path)
if not os.path.exists(journals_path):
    os.makedirs(journals_path)
if not os.path.exists(assets_path):
    os.makedirs(assets_path)

# 复制 output 下的所有 md 文件到 output_mer/journals/
for root, dirs, files in os.walk(output_path):
    for file in files:
        if file.endswith(".md"):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(journals_path, file)
            shutil.copy(src_file, dst_file)

# 复制 file 及其子文件夹下的所有图片到 output_mer/assets/
for root, dirs, files in os.walk("file"):
    for file in files:
        if file.endswith((".jpg", ".png", ".gif", ".jpeg")):  # 根据需要添加图片格式
            src_file = os.path.join(root, file)
            dst_file = os.path.join(assets_path, file)
            shutil.copy(src_file, dst_file)