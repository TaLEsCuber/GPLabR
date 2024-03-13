import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('all_data.csv')

# 计算自然对数
df['Log_Transmittance'] = df['Transmittance'].apply(lambda x: np.log(0.01*x))

# 创建子图
fig, ax = plt.subplots()

# 遍历不同波长的数据
for wavelength, data in df.groupby('Wavelength'):
    # 计算线性拟合
    slope, intercept, r_value, p_value, std_err = linregress(data['PlateNumber'], data['Log_Transmittance'])
    line = slope * df['PlateNumber'] + intercept
    # 绘制线性拟合曲线
    ax.plot(df['PlateNumber'], line, label=f'Wavelength {wavelength}nm, Slope={slope:.2f}, R={r_value:.2f}')

    # 在线上标注数据点
    for i, row in data.iterrows():
        ax.scatter(row['PlateNumber'], row['Log_Transmittance'], marker='o', color='black')

# 设置图表标题和标签
ax.set_title('Linear Fit of Log(Transmittance) vs. Plate Number')
ax.set_xlabel('Plate Number')
ax.set_ylabel('Log(Transmittance)')
ax.legend()

# 显示图表
plt.show()






# import math
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import linregress
#
# # 读取CSV文件
# df = pd.read_csv('all_data.csv')
#
# # 创建一个空的图像
# plt.figure(figsize=(10, 6))
#
# # 遍历不同波长的数据
# for wavelength, data in df.groupby('Wavelength'):
#     # 计算透射率的自然对数
#     data['Ln_Transmittance'] = data['Transmittance'].apply(lambda x: -1 * math.log(x))
#
#     # 计算线性拟合
#     slope, intercept, r_value, p_value, std_err = linregress(data['PlateNumber'], data['Ln_Transmittance'])
#
#     # 绘制原始数据点
#     plt.scatter(data['PlateNumber'], data['Ln_Transmittance'], label=f'Wavelength {wavelength} nm')
#
#     # 绘制线性拟合线
#     plt.plot(data['PlateNumber'], slope * data['PlateNumber'] + intercept, label=f'Fit Wavelength {wavelength} nm')
#
#     # 在图上标出斜率和相关系数
#     textstr = f'Slope: {slope:.2f}\nR-squared: {r_value ** 2:.2f}'
#     plt.text(data['PlateNumber'].iloc[-1], data['Ln_Transmittance'].iloc[-1], textstr, verticalalignment='bottom')
#
# # 添加标题和标签
# plt.title('Transmittance vs. PlateNumber with Linear Fit')
# plt.xlabel('PlateNumber')
# plt.ylabel('Ln(Transmittance)')
# plt.legend(title='Slope and R-squared', loc='upper left')
# plt.grid(True)
#
# # 显示图像
# plt.show()
