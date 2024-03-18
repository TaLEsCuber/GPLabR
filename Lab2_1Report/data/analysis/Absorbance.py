import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# 读取Excel文件
df = pd.read_excel('Absorbance.xlsx')

# 提取各列数据
concentration = df['浓度/(g/L)']
peak1 = df['吸收峰1']
peak2 = df['吸收峰2']
peak3 = df['吸收峰3']

# 创建绘图窗口
plt.figure(figsize=(10, 6))

# 绘制各组数据
plt.scatter(concentration, peak1, label='Absorption Peak 1', color='b')
plt.scatter(concentration, peak2, label='Absorption Peak 2', color='g')
plt.scatter(concentration, peak3, label='Absorption Peak 3', color='r')

# 计算并绘制各组数据的线性拟合直线
for i, peak_data in enumerate([peak1, peak2, peak3], start=1):
    slope, intercept, r_value, p_value, std_err = linregress(concentration, peak_data)
    plt.plot(concentration, slope * concentration + intercept, label=f'Fit Line {i}: Slope={slope:.2f}, Correlation Coefficient={r_value:.2f}')

# 添加图例、标题和坐标轴标签
plt.legend()
plt.title('Relationship between Concentration and Absorption Peaks')
plt.xlabel('Concentration (g/L)')
plt.ylabel('Absorption Peak')
plt.grid(True)

# 显示图像
plt.show()
