# 运行tle2czml库的


from tle2czml import tle2czml
# 输入 TLE 文件路径
tle_file_path = "/Users/xxxx/python/CesiumSatelliteSimulation/qianfan.txt"

# 输出 CZML 文件路径
czml_file_path = "/Users/xxxx/python/CesiumSatelliteSimulation/satellites.czml"

# 调用 tle2czml 函数进行转换
tle2czml.create_czml(tle_file_path, czml_file_path)  # 注意函数名称可能不同

print(f"CZML 文件已生成: {czml_file_path}")
