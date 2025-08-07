import os
from natsort import natsorted  # 导入 natsort 库

# 设置文件夹路径
folder_path = r'E:\ex_cvpr\DASS-main\dataset\SABS\images\images'

# 设置输出的txt文件路径
output_txt_path = r'E:\ex_cvpr\DASS-main\dataset\SABS\images\image_filenames.txt'

# 获取文件夹中所有文件的文件名
file_names = os.listdir(folder_path)

# 过滤掉非图像文件（如果需要，只保留图片文件，例如以.png结尾）
image_files = [file for file in file_names if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

# 使用 natsort 对文件名进行自然排序
sorted_image_files = natsorted(image_files)

# 将文件名保存到txt文件
with open(output_txt_path, 'w') as output_file:
    for file_name in sorted_image_files:
        output_file.write(file_name + '\n')

print(f"文件名已保存到: {output_txt_path}")
