import pandas as pd
import rasterio
from pyproj import Transformer
from rasterio.windows import Window

# 读取Excel文件
df = pd.read_excel('C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量.xlsx')

# 设置坐标转换，从WGS84地理坐标系（经纬度）到UTM投影坐标系
transformer = Transformer.from_crs("epsg:4326", "epsg:32649", always_xy=True)

# 遍历DataFrame中的每一行
estimated_values = []
for index, row in df.iterrows():
    year = row['年度']
    longitude = row['经度']
    latitude = row['纬度']

    # 转换坐标
    x, y = transformer.transform(longitude, latitude)

    # 构建tif文件路径
    tif_path = f'I:/xxls_data/base/pred_jq/Soybean_{year}.tif'

    try:
        # 读取tif文件
        with rasterio.open(tif_path) as src:
            # 获取文件中一个像素代表的实际大小（假设像素大小相等）
            pixel_size = src.res[0]  # 像素大小（x方向）

            # 计算5公里范围对应的像素数量（x方向和y方向相同）
            distance_in_pixels = 2500 / pixel_size

            # 根据坐标获取窗口
            row_off, col_off = src.index(x, y)
            window = Window(col_off - distance_in_pixels / 2, row_off - distance_in_pixels / 2,
                            distance_in_pixels, distance_in_pixels)

            # 读取窗口数据
            data = src.read(1, window=window)

            # 计算平均值，忽略NaN值
            if data.size > 0:
                valid_data = data[data != src.nodata]
                if valid_data.size > 0:
                    mean_value = valid_data.mean()
                    estimated_values.append(mean_value)
                else:
                    estimated_values.append(None)
            else:
                estimated_values.append(None)
    except Exception as e:
        print(f"Error processing tif file for year {year}: {e}")
        estimated_values.append(None)

# 将获取的值添加到新列
df['估计值'] = estimated_values

# 保存更新后的Excel文件
df.to_excel('C:/Users/cau/Desktop/xxls/数据/站点大豆/大豆产量_更新.xlsx', index=False)
