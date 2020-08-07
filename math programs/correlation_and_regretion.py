import math


def correlation_and_regression():
    x = input('Enter x value: ')
    y = input('Enter y value: ')
    xl = [float(i) for i in x.split()]
    yl = [float(i) for i in y.split()]
    n = len(xl)
    x_bar = round(sum(xl) / n, 3)
    y_bar = round(sum(yl) / n, 3)
    x_minus_x_bar = []
    y_minus_y_bar = []
    xb_min_yb = []
    x_minus_x_bar_sq = []
    y_minus_y_bar_sq = []

    for num in xl:
        x_minus_x_bar.append(num - x_bar)
    for num in yl:
        y_minus_y_bar.append(num - y_bar)

    for num in range(len(x_minus_x_bar)):
        xb_min_yb.append(x_minus_x_bar[num] * y_minus_y_bar[num])
        x_minus_x_bar_sq.append(pow(x_minus_x_bar[num], 2))
        y_minus_y_bar_sq.append(pow(y_minus_y_bar[num], 2))
    sb_min_yb_sq = math.sqrt(sum(x_minus_x_bar_sq) * sum(y_minus_y_bar_sq))
    r = sum(xb_min_yb) / sb_min_yb_sq
    print(round(r))


while True:
    correlation_and_regression()
