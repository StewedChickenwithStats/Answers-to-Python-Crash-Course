import csv  # 导入模块csv（csv模块包含在Python标准库中，可用于分析CSV文件中的数据行，让我们快速提取感兴趣的值

filename = 'sitka_weather_07-2014.csv'
# 打开文件，将结果文件对象存储在f中
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与该文件向关联的阅读器（reader）对象。reader处理文件中以逗号分割的第一行数据，并将每项数据都作为一个元素存储在列表中
    header_row = next(reader)  # 内置函数next()返回文件的下一行
    print(header_row)
