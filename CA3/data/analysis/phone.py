import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('phone.xlsx',skiprows=5)

# 提取X和Y的数据列
x_data = df['Wavelength [nm]']
y_data = df['phone']

# 绘制X-Y曲线图
plt.plot(x_data, y_data)
plt.xlabel('Wavelength/nm')
plt.ylabel('Intensity')
plt.title('Mobile phone screen spectrum')
plt.grid(True)  # 添加网格线
plt.show()
