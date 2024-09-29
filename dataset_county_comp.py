import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter  # 导入格式化工具

font_english = FontProperties(fname=r'C:\Windows\Fonts\times.ttf', size=17)  # Times New Roman字体路径和大小

plt.rcParams['font.family']=' Times New Roman, SimSun'# 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['mathtext.fontset'] = 'stix' # 设置数学公式字体为stix

config = {
    "font.family":'serif',
    "font.size": 20,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)

# 读取Excel文件
excel_path = r'C:\Users\cau\Desktop\xxls\数据\县市级大豆\数据集对比-EarthStat.xlsx'
data = pd.read_excel(excel_path)

# 提取年份和对应的R²与RMSE数据
years = data['年份']
benwenjieguo_r2 = data['本文结果-R²']
benwenjieguo_rmse = data['本文结果-RMSE']
gdhy_r2 = data['GDHY-R²']
gdhy_rmse = data['GDHY-RMSE']

# 设置中文字体为宋体
font = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=14)

# 设置图表主题
sns.set_theme(style="whitegrid")

# 创建图表
fig, ax1 = plt.subplots(figsize=(12, 5))

# 设置主色调为蓝色和红色
colors = ['#4c81a4', '#e46e68']

# 绘制RMSE的柱状图
bar_width = 0.4
ax1.bar(years - bar_width/2, benwenjieguo_rmse, width=bar_width, label=r'本文结果 $\rm {RMSE}$', color=colors[0], align='center', edgecolor='black')
ax1.bar(years + bar_width/2, gdhy_rmse, width=bar_width, label='$\\rm {MapSPAM\; RMSE}$', color=colors[1], align='center', edgecolor='black')

# 设置轴标签
ax1.set_xlabel('年份', fontproperties=font, fontname='Times New Roman')
ax1.set_ylabel('RMSE', fontproperties=font, fontname='Times New Roman')
ax1.set_xticks(years, fontname='Times New Roman')  # 设置横坐标显示所有年份
# 设置横坐标刻度字体为Times New Roman
ax1.set_xticklabels(years, fontproperties=font_english)
ax1.set_xlim([years.min() - 0.7, years.max() + 0.7])  # 设置x轴的范围，留出少量空间
ax1.tick_params(axis='both', labelsize=17)
ax1.set_yticklabels(ax1.get_yticks(), fontproperties=font_english)  # 强制使用Times New Roman
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # 设置y轴格式为两位小数

# 绘制R²的散点图，略微放大点大小
scatter_size = 85
ax2 = ax1.twinx()
ax2.scatter(years, benwenjieguo_r2, color=colors[0], label=r'本文结果 $\rm {R^2}$', edgecolor='black', alpha=1, s=scatter_size)
ax2.scatter(years, gdhy_r2, color=colors[1], label='$\\rm {MapSPAM \; R^2}$', edgecolor='black', alpha=1, s=scatter_size)

# 设置轴标签
ax2.set_ylabel('R²', fontproperties=font)  # 中文
ax2.set_yticklabels(ax2.get_yticks(), fontproperties=font_english)  # 强制使用Times New Roman
ax2.tick_params(axis='y', labelsize=17)
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))  # 设置y轴格式为两位小数

# 移除网格以减少混乱
ax1.grid(False)
ax2.grid(False)

# 添加标题和图例
plt.title(' \n\n\n\n\n\n ', fontproperties=font, fontsize=16)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.97), ncol=1, fontsize=12, prop=font)

# 显示图表
plt.tight_layout()
plt.savefig(r'C:\Users\cau\Desktop\xxls\数据\图片\柱状图\MapSPAM-1.png', dpi=500)
plt.show()
