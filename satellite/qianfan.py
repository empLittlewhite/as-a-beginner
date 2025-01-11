import json
from sgp4.api import Satrec
from sgp4.api import jday
from datetime import datetime, timedelta
import pytz

# 定义CZML文档的初始部分
czml_document = [{
    "id": "document",
    "name": "Satellite CZML",
    "version": "1.0"
}]

def parse_epoch(line1):
    """
    解析TLE中的纪元时间，并转换为ISO8601格式。
    TLE中的epoch格式为YYDDD.DDDDDDDD
    """
    epoch_str = line1[18:32].strip()
    year = int(epoch_str[0:2])
    doy = float(epoch_str[2:])

    # 解析年份
    if year < 57:
        year += 2000
    else:
        year += 1900

    # 解析年中的第几天
    day = int(doy)
    fraction = doy - day
    date = datetime(year, 1, 1) + timedelta(days=day - 1, seconds=fraction * 86400)
    date = date.replace(tzinfo=pytz.UTC)
    return date.isoformat()

def tle_to_czml(input_file, output_file):
    """
    将TLE格式的数据转换为CZML格式并保存到文件。
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # 移除空行和空白字符
    lines = [line.strip() for line in lines if line.strip()]

    # 确保每个卫星有3行：名称、line1、line2
    if len(lines) % 3 != 0:
        print("警告：TLE数据的行数不是3的倍数，可能存在不完整的数据。")
    
    for i in range(0, len(lines), 3):
        try:
            name = lines[i]
            line1 = lines[i+1]
            line2 = lines[i+2]
        except IndexError:
            print(f"警告：无法解析第{i+1}行到第{i+3}行的卫星数据。")
            continue

        # 使用sgp4解析TLE
        try:
            satellite = Satrec.twoline2rv(line1, line2)
        except Exception as e:
            print(f"错误：解析卫星{name}的TLE数据时出错: {e}")
            continue

        # 解析纪元时间
        epoch_iso = parse_epoch(line1)

        # 获取纪元的年、月、日、时、分、秒
        epoch_year = int(line1[18:20])
        epoch_day = float(line1[20:32])
        if epoch_year < 57:
            epoch_year += 2000
        else:
            epoch_year += 1900

        # 使用jday获取儒略日
        jd, fr = jday(epoch_year,
                     1, 1, 0, 0, 0)  # 临时初始化
        # 计算年中的第几天转为日期
        base_date = datetime(epoch_year, 1, 1, tzinfo=pytz.UTC)
        epoch_datetime = base_date + timedelta(days=epoch_day - 1)
        jd, fr = jday(epoch_datetime.year, epoch_datetime.month, epoch_datetime.day,
                      epoch_datetime.hour, epoch_datetime.minute, epoch_datetime.second + epoch_datetime.microsecond * 1e-6)

        # 计算卫星位置和速度
        error_code, position, velocity = satellite.sgp4(jd, fr)
        if error_code != 0:
            print(f"错误：SGP4计算卫星{name}位置时出错，错误代码: {error_code}")
            continue

        # position单位为千米，转换为米
        x, y, z = [coord * 1000 for coord in position]

        # 创建CZML对象
        czml_satellite = {
            "id": name,
            "name": name,
            "availability": f"{epoch_iso}/" + (epoch_datetime + timedelta(hours=1)).isoformat(),
            "position": {
                "cartesian": [x, y, z]
            },
            "label": {
                "text": name,
                "font": "14pt Arial",
                "fillColor": {
                    "rgba": [255, 255, 255, 255]
                },
                "outlineColor": {
                    "rgba": [0, 0, 0, 255]
                },
                "outlineWidth": 2,
                "pixelOffset": {
                    "cartesian2": [0, -20]
                }
            },
            "point": {
                "color": {
                    "rgba": [255, 0, 0, 255]
                },
                "pixelSize": 10
            }
        }

        czml_document.append(czml_satellite)

    # 写入CZML文件
    with open(output_file, 'w') as f:
        json.dump(czml_document, f, indent=4)
    print(f"CZML文件已生成并保存为 {output_file}")

if __name__ == "__main__":
    input_tle_file = "/Users/alan/as-a-beginner/satellite/qianfan.txt"      # 输入的TLE文件
    output_czml_file = "/Users/alan/as-a-beginner/satellite/satellite.czml" # 输出的CZML文件
    tle_to_czml(input_tle_file, output_czml_file)