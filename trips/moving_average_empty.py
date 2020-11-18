import matplotlib.pyplot as plt
import random

# sample size: depende de los datos que te arroje el sensor


def smooth_curve_average(points, sample_size):
    smoothed_points = []
    x_coordinates = list()
    stuff = list()
    counter = 0
    for i in range(len(points)):
        if counter < sample_size:
            counter += 1
            stuff.append(points[i])
        else:
            counter = 0
            s = sum(stuff)
            smoothed_points.append(s/sample_size)
            stuff.clear()
            x_coordinates.append(i)

    return smoothed_points, x_coordinates


def smooth_curve_exponential(points, factor=0.9):
    smoothed_points = []
    gap = 100
    for i in range(len(points)-gap):
        t_1 = points[i]
        t = points[i+gap]

    return smoothed_points


"""
    lapse = 1
    for i in range(len(points)-lapse):
        t_1 = points[i]
        t = points[i+lapse]
        point = t_1*factor+t*(1-factor)
        smoothed_points.append(point)
"""
sample_size = 20
data_series = []
peaks = []


# Semilla pseudo aleatoria. Funciones matematicas que generan numeros "aleatorios" con un punto de inicio.
random.seed(0)

while len(data_series) < 1000:
    data_series.append(random.uniform(360, 380))

data_series_smooth_ex = smooth_curve_exponential(data_series, 0.95)
data_series_smooth_av, x = smooth_curve_average(data_series, 20)


# plt.plot(data_series)
plt.plot(data_series_smooth_ex)
#plt.plot(x, data_series_smooth_av)
plt.plot()
plt.ylabel("Data")

plt.show()
