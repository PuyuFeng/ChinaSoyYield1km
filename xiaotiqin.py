import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

font_english = FontProperties(fname=r'C:\Windows\Fonts\times.ttf', size=13)  # Times New Roman字体路径和大小

plt.rcParams['font.family']=' Times New Roman, SimSun'# 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['mathtext.fontset'] = 'stix' # 设置数学公式字体为stix

config = {
    "font.family":'serif',
    "font.size": 13,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)


# 使用你提供的路径和文件名
file_paths = [
    "C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_本文结果.xlsx",
    "C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_SPAM.xlsx",
    "C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_EarthStat.xlsx",
    "C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_GDHY.xlsx"
]

# 读取所有文件并抽取差值列
dataframes = [pd.read_excel(file) for file in file_paths]
differences = [(df['差值'] / 1000) for df in dataframes]
source_names = ["本文结果", "SPAM", "EarthStat", "GDHY"]

# 创建一个包含所有差值数据的DataFrame，标记数据来源
combined_data = pd.concat(differences, axis=0, ignore_index=True)
combined_data = pd.DataFrame({
    "差值": combined_data,
    "数据源": sum([[name] * len(df) for name, df in zip(source_names, differences)], [])
})

# 使用seaborn绘制小提琴图与箱线图
plt.figure(figsize=(8.5, 5))
ax = sns.violinplot(x='数据源', y='差值', hue='数据源', data=combined_data, inner=None, palette="muted", legend=False, zorder=2)
box = sns.boxplot(x='数据源', y='差值', data=combined_data, color='#eeeeee', width=0.15, zorder=3,
                  boxprops=dict(edgecolor="#444444", linewidth=1.5),
                  whiskerprops=dict(color="#444444", linewidth=1.5),
                  capprops=dict(color="#444444", linewidth=1.5),
                  medianprops=dict(color="#444444", linewidth=1.5))  # 箱线图，统一颜色且调整宽度和边框

# plt.xlabel('数据源', fontproperties=font)
plt.ylabel('Deviations from station recorded data $\\rm {(t/ha)}$', fontproperties=font_english)
plt.xticks(fontproperties=font_english)  # 使用字体设置显示x轴刻度
plt.yticks(fontproperties=font_english)  # 使用字体设置显示y轴刻度
ax.grid(True, zorder=0)  # 设置格网在底层

plt.savefig(r'C:\Users\cau\Desktop\bean论文\figure\comp1.png', dpi=500)
plt.show()
