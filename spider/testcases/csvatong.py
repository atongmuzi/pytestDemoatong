# 导入 csv 库
import csv

# 以读方式打开文件
with open("data.csv", mode="r", encoding="utf-8-sig") as f:
    # 基于打开的文件，创建csv.reader实例
    reader = csv.reader(f)
    # 获取第一行的header
    # header[0] = "设备编号"
    # header[1] = "温度"
    # header[2] = "湿度"
    # header[3] = "转速"
    header = next(reader)

    # 逐行获取数据，并输出
    for row in reader:
        print("{}{}: {}={}, {}={}, {}={}".format(header[0], row[0],
                                                 header[1], row[1],
                                                 header[2], row[2],
                                                 header[3], row[3]))
