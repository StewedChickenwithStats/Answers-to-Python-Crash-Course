import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 调整尺寸以适合屏幕
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 重新绘制起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75)


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
