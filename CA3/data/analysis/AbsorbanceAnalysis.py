import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('all_data.csv')

# 计算自然对数
df['Log_Transmittance'] = df['Transmittance'].apply(lambda x: np.log(x))

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
