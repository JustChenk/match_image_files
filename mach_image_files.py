# import os
# import pandas as pd
#
# # 读取CSV文件
# csv_file_path = r'C:\Users\10697\Desktop\test\image_names.csv'
# df = pd.read_csv(csv_file_path)
#
# # 指定图像文件夹路径
# image_folder_path = r'C:\Users\10697\Desktop\test\xc_yilian_frame'
#
# # 获取文件夹中的所有图像文件
# image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]
#
# # 检查每一行的图像是否在文件夹中
# for index, row in df.iterrows():
#     image_name = row['']  # 请替换为实际的列名称
#     if image_name in image_files:
#         print(f"{image_name} 在文件夹中")
#     else:
#         print(f"{image_name} 不在文件夹中")
#


import os
import pandas as pd
import shutil

# 读取CSV文件
csv_file_path = r'C:\Users\10697\Desktop\test\image_names.csv' # Excel文件路径
df = pd.read_csv(csv_file_path)

# 指定图像文件夹路径和目标文件夹路径
image_folder_path = r'C:\Users\10697\Desktop\test\xc_yilian_frame' # 查找图片目录
target_folder_path = r'C:\Users\10697\Desktop\test\yilian'      # 复制对应的图片到新目录

# 获取文件夹中的所有图像文件
image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder_path):
    os.makedirs(target_folder_path)

# 指定要查找的列索引
target_column_index = 0  # 这里假设你想在第二列（索引为1）中查找图像文件

# 复制每个在文件夹中找到的图像到目标文件夹
for index, row in df.iterrows():
    image_name = row.iloc[target_column_index]  # 使用 iloc 获取特定列的值
    image_name = image_name.split('\\')[-1]
    if image_name in image_files:
        source_path = os.path.join(image_folder_path, image_name)
        target_path = os.path.join(target_folder_path, image_name)
        shutil.copyfile(source_path, target_path)
        print(f"{image_name} 复制到 {target_folder_path}")
    else:
        print(f"{image_name} 不在文件夹中")
