# import pandas as pd
# import matplotlib.pyplot as plt
# import os
#
# # 文件夹路径
# folder_path = 'plate'
#
# # 初始化图形
# plt.figure(figsize=(10, 6))
#
# # 读取并绘制各个文件的数据
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.xlsx') and 'plate' in file_name:
#         # 提取玻璃片数量信息
#         plates = file_name.split('-')[1].split('.')[0]  # 提取文件名中的数字部分
#         # 读取数据并绘图
#         df = pd.read_excel(os.path.join(folder_path, file_name), skiprows=5)
#         # 查找包含 "plate" 的列名
#         transmittance_column = [col for col in df.columns if 'plate' in col.lower()][0]
#         plt.plot(df['Wavelength [nm]'], df[transmittance_column], label=f'PlateNumber: {plates}')
#
# # 设置图形标题和标签
# plt.xlabel('Wavelength [nm]')
# plt.ylabel('Transmittance')
# plt.title('Transmittance vs. Wavelength for Different Number of Glass Plates')
# plt.legend(title='Number of Plates')
#
# # 显示图像
# plt.show()




import pandas as pd
import matplotlib.pyplot as plt
import os

# 文件夹路径
folder_path = 'plate'

# 初始化图形
plt.figure(figsize=(10, 6))

# 创建空的DataFrame用于存储所有数据
all_data = pd.DataFrame(columns=['PlateNumber', 'Wavelength', 'Transmittance'])

# 读取并绘制各个文件的数据
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx') and 'plate' in file_name:
        # 提取玻璃片数量信息
        plates = file_name.split('-')[1].split('.')[0]  # 提取文件名中的数字部分
        # 读取数据并绘图
        df = pd.read_excel(os.path.join(folder_path, file_name), skiprows=5)
        # 查找包含 "plate" 的列名
        transmittance_column = [col for col in df.columns if 'plate' in col.lower()][0]
        plt.plot(df['Wavelength [nm]'], df[transmittance_column], label=f'PlateNumber: {plates}')

        # 提取500nm, 600nm, 700nm处的数据
        data_500nm = df.loc[df['Wavelength [nm]'].sub(500).abs().idxmin(), transmittance_column]
        data_600nm = df.loc[df['Wavelength [nm]'].sub(600).abs().idxmin(), transmittance_column]
        data_700nm = df.loc[df['Wavelength [nm]'].sub(700).abs().idxmin(), transmittance_column]

        # 将数据添加到DataFrame中
        all_data = pd.concat([all_data, pd.DataFrame({'PlateNumber': [plates]*3, 'Wavelength': [500, 600, 700], 'Transmittance': [data_500nm, data_600nm, data_700nm]})])

# 保存所有数据到一个CSV文件中
# all_data.to_csv('all_data.csv', index=False)

# 设置图形标题和标签
plt.xlabel('Wavelength [nm]')
plt.ylabel('Transmittance')
plt.title('Transmittance vs. Wavelength for Different Number of Glass Plates')
plt.legend(title='Number of Plates')

# 显示图像
plt.show()

