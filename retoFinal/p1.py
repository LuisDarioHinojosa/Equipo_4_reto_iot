import datetime
import serial
import matplotlib.pyplot as plt


def getSerialConnector(baudRate, port):
    ser = serial.Serial(port, baudRate)
    return ser


def getRawData():
    ser = getSerialConnector(9600, "COM5")
    counter = 0

    sampleSize = 2000
    hmed = list()
    tmed = list()

    while(counter < sampleSize):
        try:
            lineBytes = ser.readline()
            line = lineBytes.decode("ascii")
            line = line.rstrip()
            parts = line.split(":")
            hr = int(parts[0])
            miliseconds = int(parts[1])
            hmed.append(hr)
            tmed.append(miliseconds)
            counter += 1

        except:
            continue
    return hmed, tmed


def getMeditionTime():
    n = str(datetime.datetime.now())
    timePair = n.split()
    date = timePair[0]
    hour = timePair[1]
    return date, hour[0:8]


def smooth_curve_average(points, times, sample_size):
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
            x_coordinates.append(times[i])

    return smoothed_points, x_coordinates


h, t = getRawData()


smooth, times = smooth_curve_average(h, t, 50)
plt.plot(times, smooth)
plt.plot()
plt.ylabel("Heartbeat")
plt.xlabel("Time Miliseconds")
plt.show()


"""
ser = getSerialConnector(9600, "COM5")
counter = 0

sampleSize = 2000
sc = 0
hmed = list()
tmed = list()

while(counter < sampleSize):
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode("ascii")
        line = line.rstrip()
        parts = line.split(":")
        hr = int(parts[0])
        miliseconds = int(parts[1])
        hmed.append(hr)
        tmed.append(miliseconds)
        counter += 1

    except:
        continue




smooth, times = smooth_curve_average(hmed, tmed, 1000)
plt.plot(times, smooth)
plt.plot()
plt.ylabel("Heartbeat")
plt.xlabel("Time Miliseconds")
plt.show()
"""
