import simple_draw as sd
import random as r

sd.resolution = (1200, 600)
start_x = []
start_y = []
snowfall_length = []
snowfall_factor_a = []
snowfall_factor_b = []
snowfall_factor_c = []
quantity_snowfall = 0


def create_snowfall(N):
    global snowfall_length, quantity_snowfall
    global start_x, start_y
    global snowfall_factor_a, snowfall_factor_b, snowfall_factor_c
    quantity_snowfall += N
    for _ in range(N):
        start_x += [r.randint(100, 1000)]
        start_y += [r.randint(550, 1600)]
        snowfall_length += [r.randint(20, 40)]
        snowfall_factor_a += [r.random()]
        snowfall_factor_b += [r.random()]
        snowfall_factor_c += [r.randint(1, 179)]


def draw_snowfall(color):
    global SNOWFALL
    start_point = [sd.Point(start_x[i], start_y[i]) for i in range(quantity_snowfall)]
    SNOWFALL = [sd.snowflake(center=start_point[i],
                             length=snowfall_length[i], factor_a=snowfall_factor_a[i], factor_b=snowfall_factor_b[i],
                             factor_c=snowfall_factor_c[i], color=color) for i in range(quantity_snowfall)]


def dy_snowfall():
    global start_x, start_y
    for i in range(quantity_snowfall):
        start_y[i] -= 5
        start_x[i] += r.randint(-5, 5)


def exit_border_snowfall():
    res = []
    for i, y in enumerate(start_y):
        if y - snowfall_length[i] <= 0:
            res.append(i)
    return sorted(res, reverse=True)


def del_snowfall(res):
    global quantity_snowfall
    global start_x, start_y
    draw_snowfall(color=sd.background_color)

    for i in res:
        start_x.pop(i)
        start_y.pop(i)
        snowfall_length.pop(i)

    quantity_snowfall -= len(res)
    draw_snowfall(color=sd.COLOR_WHITE)
