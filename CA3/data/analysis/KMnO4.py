import pandas as pd
import matplotlib.pyplot as plt
import os

# 存储文件夹路径
folder_path = 'KMnO4'

# 获取文件夹中所有文件名
file_names = os.listdir(folder_path)

# 初始化图形
plt.figure(figsize=(10, 6))

# 读取并绘制各个文件的数据
for file_name in file_names:
    if file_name.endswith('.xlsx'):
        # 提取浓度信息
        concentration = float(file_name.split('-')[1][:-5])  # 提取0.1这样的数字并转换为浮点数
        # 读取数据并绘图
        df = pd.read_excel(os.path.join(folder_path, file_name), skiprows=5)
        # 查找包含 "KMnO4" 的列名
        absorbance_column = [col for col in df.columns if 'KMnO4' in col][0]
        # 筛选出500-600nm范围内的数据
        df_range = df[(df['Wavelength [nm]'] >= 500) & (df['Wavelength [nm]'] <= 600)]
        # 找到吸收率最高的位置对应的波长和吸收率
        max_absorbance_index = df_range[absorbance_column].idxmax()
        max_absorbance = df_range.loc[max_absorbance_index, absorbance_column]
        max_wavelength = df_range.loc[max_absorbance_index, 'Wavelength [nm]']
        # 绘制曲线
        plt.plot(df['Wavelength [nm]'], df[absorbance_column], label=f'{concentration} g/L')
        # 在图上标出吸收率最高的位置对应的波长和吸收率
        plt.annotate(f"{max_wavelength:.2f} nm, {max_absorbance:.2f}",
                     xy=(max_wavelength, max_absorbance),
                     xytext=(max_wavelength - 5, max_absorbance - 0.2),
                     arrowprops=dict(arrowstyle='->', mutation_scale=10))

# 设置图形标题和标签
plt.xlabel('Wavelength [nm]')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Wavelength for Different Concentrations of $KMnO_4$')
plt.legend(title='Concentration')

# 显示图像
plt.show()


