import datetime
import serial
#import serial.tools.list_ports as portInterface
import matplotlib.pyplot as plt


def getSerialConnector(baudRate, port):
    ser = serial.Serial(port, baudRate)
    return ser


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


def getRawKYMeditionData(S: object):
    loop = True
    kyMed = list()
    kyTime = list()
    while(loop):
        lineBytes = S.readline()
        line = lineBytes.decode("ascii")
        if("END KY TRANSMITION" in line):
            loop = False
        else:
            line = line.rstrip()
            parts = line.split(";")
            HR = int(parts[0].split(":")[1])
            MS = int(parts[1].split(":")[1])
            if(MS < 0):
                MS *= -1
            kyMed.append(HR)
            kyTime.append(MS)
            print(f"Medition: {HR} Time: {MS}")

    return kyMed, kyTime


def getRawMaxMeditions(S: object):
    hrMed = list()
    timeMed = list()
    redMed = list()
    irMed = list()
    loop = True
    while(loop):
        lineBytes = S.readline()
        line = lineBytes.decode("ascii")
        if("END MAX TRANSMITION" in line):
            loop = False
        else:
            line = line.rstrip()
            parts = line.split(";")
            hr = int(parts[0].split(":")[1])
            ms = int(parts[1].split(":")[1])
            if(ms < 0):
                ms *= -1
            red = int(parts[2].split(":")[1])
            ir = int(parts[3].split(":")[1])
            hrMed.append(hr)
            timeMed.append(ms)
            redMed.append(red)
            irMed.append(ir)
            print(f"heartBeat {hr} time {ms} infrared {red} ir {ir}")
    return hrMed, timeMed, redMed, irMed


# HR:649;ML:13147
# HR:3;ML:3587;RED:3771;IR:3880
ser = getSerialConnector(9600, "COM4")
while(True):
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode("ascii")

        if ("START MAX TRANSMITION" in line):
            hm, tm, rm, im = getRawMaxMeditions(ser)

        elif ("START KY TRANSMITION" in line):
            meditions, time = getRawKYMeditionData(ser)
            smooth, times = smooth_curve_average(meditions, time, 50)
            plt.plot(time, meditions)
            plt.plot()
            plt.ylabel("Heartbeat")
            plt.xlabel("Time Miliseconds")
            plt.show()
        else:
            print(line)
    except:
        continue
