import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 从 Excel 文件中读取数据，假设有 '波长' 和 '强度' 两列
df = pd.read_excel('Hg2.xlsx',skiprows=5)

# 提取波长和强度数据列
wavelengths = df['Wavelength [nm]']
intensities = df['Hg1']

# 绘制波长-强度曲线
plt.plot(wavelengths, intensities)
plt.xlabel('Wavelength/nm')
plt.ylabel('Intensity')
plt.title('Hg Spectrum')

# 寻找峰值
peaks, _ = find_peaks(intensities, distance=10)

# 选择强度最高的五个峰
highest_peaks = sorted(peaks, key=lambda x: intensities[x], reverse=True)[:6]

# 标记峰值对应的波长值，并微调位置避免重叠
offset = 0.1  # 调整的偏移量
for i, peak in enumerate(highest_peaks):
    if i != 3:  # 排除第四个数据点
        plt.annotate(f"{wavelengths[peak]:.2f}", (wavelengths[peak], intensities[peak]),
                     xytext=(10, -20), textcoords='offset points',
                     arrowprops=dict(arrowstyle="->"))
    else:
        plt.text(wavelengths[peak], intensities[peak], f"{wavelengths[peak]:.2f}",
                 verticalalignment='bottom', horizontalalignment='center')



# 显示图像
plt.show()
