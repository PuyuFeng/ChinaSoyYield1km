import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import rcParams

# 设置字体为宋体，确保字体文件路径正确
font_path = 'C:/Windows/Fonts/simsun.ttc'  # simsun.ttc是宋体的字体文件
font_prop = FontProperties(fname=font_path, size=14)

plt.rcParams['font.family']=' Times New Roman, SimSun'# 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['mathtext.fontset'] = 'stix' # 设置数学公式字体为stix

config = {
    "font.family":'serif',
    "font.size": 14,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)

# 载入数据
file_path = 'C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_本文结果.xlsx'
data = pd.read_excel(file_path)

# 假设Excel文件中的列名为'站点观测值'和'估计值'
obs_col = '站点观测值'  # 这里替换为文件中对应的列名
est_col = '估计值'  # 这里替换为文件中对应的列名

# 使用Seaborn绘制带有密度渐变的散点图
plt.figure(figsize=(6, 6), dpi=500)  # 增加DPI参数
sns.kdeplot(x=data[obs_col], y=data[est_col], levels=100, color='b', fill=True)
sns.scatterplot(x=data[obs_col], y=data[est_col], size=1, legend=False)

# 添加精确的y=x线
lims = [0, max(data[obs_col].max(), data[est_col].max()) + 0.5]
plt.plot(lims, lims, 'r--', alpha=0.5, zorder=1)

# 计算R²和RMSE
r_squared = r2_score(data[obs_col], data[est_col])
rmse = np.sqrt(mean_squared_error(data[obs_col], data[est_col]))

# 显示R²和RMSE
plt.text(lims[1] * 0.03, lims[1] * 0.9, f'R² = {r_squared:.2f}\nRMSE = {rmse:.2f} t/ha', fontsize=13,
         fontname='Times New Roman', bbox=dict(facecolor='white', alpha=1))

# plt.title('站点观测值与估计值散点图', fontproperties=font_prop)
plt.xlabel('Statistical yield $\\rm { (t/ha)}$',fontname="Times New Roman")
plt.ylabel('Estimated yield $\\rm { (t/ha)}$',fontname="Times New Roman")

# 设置坐标轴范围以包括原点并适应数据
plt.xlim(0, lims[1])
plt.ylim(0, lims[1])

# 设置坐标轴刻度字体为Times New Roman
plt.xticks(fontname="Times New Roman", fontsize=13)
plt.yticks(fontname="Times New Roman", fontsize=13)

plt.grid(True)

# 保存图像到指定路径
save_path = 'C:/Users/cau/Desktop/bean论文/figure/站点对比.png'
plt.savefig(save_path, dpi=500)  # 可以指定DPI
plt.show()
