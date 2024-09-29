import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter
font_english = FontProperties(fname=r'C:\Windows\Fonts\times.ttf', size=17)  # Times New Roman字体路径和大小

plt.rcParams['font.family']=' Times New Roman, SimSun'# 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['mathtext.fontset'] = 'stix'
# 读取Excel文件
excel_path = r'C:\Users\cau\Desktop\xxls\数据\县市级大豆\对比\EarthStat.xlsx'
data = pd.read_excel(excel_path)

# 提取年份和对应的R²与RMSE数据
years = data['年份']
benwenjieguo_r2 = data['本文结果-R²']
benwenjieguo_rmse = data['本文结果-RMSE']
gdhy_r2 = data['EarthStat-R²']
gdhy_rmse = data['EarthStat-RMSE']


# 设置图表主题
sns.set_theme(style="whitegrid")

# 创建图表
fig, ax1 = plt.subplots(figsize=(12, 5))

# 设置主色调为蓝色和红色
colors = ['#4c81a4', '#e46e68']

# 绘制RMSE的柱状图
bar_width = 0.4
ax1.bar(years - bar_width/2, benwenjieguo_rmse, width=bar_width, label='Stacking RMSE', color=colors[0], align='center', edgecolor='black')
ax1.bar(years + bar_width/2, gdhy_rmse, width=bar_width, label='EarthStat RMSE', color=colors[1], align='center', edgecolor='black')

# 设置轴标签
ax1.set_xlabel('Year', fontproperties=font_english)
ax1.set_ylabel('RMSE (t/ha)', fontproperties=font_english)
ax1.set_xticks(years, fontproperties=font_english)  # 设置横坐标显示所有年份
ax1.set_xlim([years.min() - 0.7, years.max() + 0.7])# 设置x轴的范围，留出少量空间
ax1.tick_params(axis='both', labelsize=14)


# 绘制R²的散点图，略微放大点大小
scatter_size = 85
ax2 = ax1.twinx()
ax2.scatter(years, benwenjieguo_r2, color=colors[0], label='Stacking R²', edgecolor='black', alpha=1, s=scatter_size)
ax2.scatter(years, gdhy_r2, color=colors[1], label='EarthStat R²', edgecolor='black', alpha=1, s=scatter_size)

# 设置轴标签
ax2.set_ylabel('R²', fontproperties=font_english)
ax2.tick_params(axis='y', labelsize=14)

# 移除网格以减少混乱
ax1.grid(False)
ax2.grid(False)

# 添加标题和图例
plt.title(' \n\n\n\n\n\n ', fontproperties=font_english, fontsize=14)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.97), ncol=1, fontsize=14, prop=font_english)

# 显示图表
plt.tight_layout()
plt.savefig(r'C:\Users\cau\Desktop\bean论文\figure\条形图\EarthStat-m.png', dpi=500)
plt.show()

