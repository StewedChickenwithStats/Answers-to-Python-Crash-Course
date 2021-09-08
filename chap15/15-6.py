import pygal

from die import Die

#创建一个D6
die=Die()

#掷几次骰子，并将结果存储在一个列表中
results=[die.roll() for roll_num in range(1000)]

#分析结果
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

#对结果进行可视化
hist = pygal.Bar()#创建一个pygal.Bar()实例，并将其存储在hist中

hist.title = "Results of rolling one D6 1000 times"#设置hist的属性title
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]#将掷D6骰子的可能结果用作x轴的标签
#给每个轴添加标题
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)#第一个参数是指定的标签，第二个参数是一个包含图表中值的列表
hist.render_to_file('die_visual.svg')#将图标渲染为一个SVG文件
