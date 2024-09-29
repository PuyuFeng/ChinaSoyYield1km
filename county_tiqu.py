import geopandas as gpd
import rasterio
import rasterstats
import pandas as pd
import os

# 读取县级矢量数据
counties = gpd.read_file("C:/Users/cau/Desktop/xxls/数据/全国电子地图shp/区划边界九段线矢量地图/县ex.shp")

# 初始化一个DataFrame来存储结果
years = [2005,2010]
results = pd.DataFrame(index=[county for county in counties['县']], columns=years)

# 遍历每一年的遥感数据
for year in years:
    print(year)
    # 构建遥感数据的文件路径
    raster_path = f"C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM_mod/SPAM_{year}.tif"  # 假设每年的文件名为年份.tif

    # 确保文件存在
    if not os.path.exists(raster_path):
        print(f"File not found: {raster_path}")
        continue

    # 读取遥感数据
    with rasterio.open(raster_path) as src:
        affine = src.transform  # 获取仿射变换
        nodata = src.nodata  # 获取数据中定义的nodata值
        if nodata is None:
            nodata = -999000000  # 使用指定的nodata值

        raster_array = src.read(1)  # 读取栅格数据

        # 对于每个县，计算遥感数据的平均值
        for county in counties.itertuples():
            # 使用rasterstats计算平均值，指定affine和nodata参数
            avg_value = rasterstats.zonal_stats(county.geometry, raster_array, affine=affine, nodata=nodata, stats="mean")[0]['mean']
            if avg_value is not None:
                results.at[county.县, year] = avg_value

# 将结果保存为Excel文件
output_path = "C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM.xlsx"
results.to_excel(output_path)

