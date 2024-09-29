import pandas as pd
import rasterio
from pyproj import Transformer
from rasterio.windows import Window  # 确保导入了Window类

# 读取Excel文件
df = pd.read_excel('C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量.xlsx')

# 设置坐标转换，从WGS84地理坐标系（经纬度）到UTM投影坐标系
transformer = Transformer.from_crs("epsg:4326", "epsg:32649", always_xy=True)

# 定义年份范围
year_range = [2005, 2010]  # 包含2001至2016年

# 遍历DataFrame中的每一行
estimated_values = []
for index, row in df.iterrows():
    year = row['年度']
    if year not in year_range:
        estimated_values.append(None)
        continue  # 跳过不存在tif文件的年份

    longitude = row['经度']
    latitude = row['纬度']

    # 转换坐标
    x, y = transformer.transform(longitude, latitude)

    # 构建tif文件路径
    tif_path = f'C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM_mod/SPAM_{year}.tif'

    try:
        # 读取tif文件
        with rasterio.open(tif_path) as src:
            # 获取该点对应的行和列
            row_index, col_index = src.index(x, y)
            # 读取指定位置的像素值
            value = src.read(1, window=Window(col_index, row_index, 1, 1))

            # 检查读取的值是否为无数据值
            if value[0, 0] == src.nodata:
                estimated_values.append(None)
            else:
                estimated_values.append(value[0, 0])  # 读取单个像素值
    except Exception as e:
        print(f"Error processing tif file for year {year}: {e}")
        estimated_values.append(None)

# 将获取的值添加到新列
df['估计值'] = estimated_values

# 保存更新后的Excel文件
df.to_excel('C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_SPAM.xlsx', index=False)
