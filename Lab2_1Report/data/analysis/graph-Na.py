import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 从 Excel 文件中读取数据，假设有 '波长' 和 '强度' 两列
df = pd.read_excel('Na2.xlsx', skiprows=5)

# 提取波长和强度数据列
wavelengths = df['Wavelength [nm]']
intensities = df['Hg1']

# 绘制波长-强度曲线
plt.plot(wavelengths, intensities)
plt.xlabel('Wavelength/nm')
plt.ylabel('Intensity')
plt.title('Na Spectrum')

# 标记已知的两个峰
known_peaks = [(588.72, '588.72'), (589.34, '589.34')]
for peak_value, text_label in known_peaks:
    peak_index = (wavelengths - peak_value).abs().idxmin()
    plt.annotate(text_label, (wavelengths[peak_index], intensities[peak_index]),
                 xytext=(10, -20), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->"))

# 显示图像
plt.show()