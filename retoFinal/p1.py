import datetime
import serial
import jorge
import enterData
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Basura


def signalKY(points, times):
    x = times
    y = points
    # window size 51, polynomial order 3
    yhat = scipy.signal.savgol_filter(y, 51, 3)

    #plt.plot(x, y)
    plt.plot(x, yhat, color='red')
    plt.show()


def getSerialConnector(baudRate, port):
    ser = serial.Serial(port, baudRate)
    return ser


# returns this moment in mysql formal.
def getMeditionTime():
    n = str(datetime.datetime.now())
    timePair = n.split()
    date = timePair[0]
    hour = timePair[1]
    return date, hour[0:8]


# funcion original para smooth
def smooth_curve_average(points, sample_size):
    smooth = []
    sample_size
    for i in range(0, len(points), sample_size):
        avg = sum(points[i:i+sample_size])
        avg = avg/sample_size
        smooth.append(avg)
    return smooth


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
    #hrMed = list()
    #timeMed = list()
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
            #hr = int(parts[0].split(":")[1])
            #ms = int(parts[1].split(":")[1])
            # if(ms < 0):
            #ms *= -1
            red = int(parts[0].split(":")[1])
            ir = int(parts[1].split(":")[1])
            # hrMed.append(hr)
            # timeMed.append(ms)
            # if(len(redMed < 100)):
            redMed.append(red)
            # if len(irMed) < 100:
            irMed.append(ir)
            #print(f"heartBeat {hr} time {ms} infrared {red} ir {ir}")
            print(f"infrared {red} ir {ir}")
    return redMed, irMed


# receibes the serial communication, stores 30 second measure, procceses, and returns a heartRate ready to be inserted into the database
def computeHeartRate(S: object):
    meditions, time = getRawKYMeditionData(ser)
    smooth = smooth_curve_average(meditions, 5)
    peaks = find_peaks(smooth)[0]
    peakNum = len(peaks)
    hr = (30000*peakNum)/(time[-1]-time[0])
    return hr

# recebies the serial communication, measures 100 meditions, proceses and returns SPO ready for insertion


def computeSPO2(S: object):
    redMed, irMed = getRawMaxMeditions(S)
    hr, hr_valid, spo2, spo2_valid = jorge.calc_hr_and_spo2(irMed, redMed)
    if spo2_valid == True:
        return spo2
    else:
        return -1


# HR:649;ML:13147
# HR:3;ML:3587;RED:3771;IR:3880
sqlUser = "root"
sqlPassword = "(phoskyGUP28)"
status = "-"
idPerson = 1


ser = getSerialConnector(9600, "COM4")
while(True):
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode("ascii")

        if ("START MAX TRANSMITION" in line):
            spo2 = computeSPO2(ser)
            #createOxygenRegister(oxygen, status, idPerson, user, password)
            if spo2 != -1:
                enterData.createOxygenRegister(
                    spo2, status, idPerson, sqlUser, sqlPassword)
                print("*************************************************************************************************************************")
                print(f"Inserted -> {spo2}")
            else:
                print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

        elif ("START KY TRANSMITION" in line):
            hr = computeHeartRate(ser)
            # createHeartbeatRegister(heartBeat, status, idPerson, user, password):
            enterData.createHeartbeatRegister(
                hr, status, idPerson, sqlUser, sqlPassword)
            print("*************************************************************************************************************************")
            print(f"inserted -> {hr}")

            """    
            meditions, time = getRawKYMeditionData(ser)
            smooth = smooth_curve_average(meditions, 5)
            peaks = find_peaks(smooth)[0]
            print("*********************************")
            peakNum = len(peaks)
            hr = (30000*peakNum)/(time[-1]-time[0])
            print(hr)
            


            smooth, times = smooth_curve_average(meditions, time, 1200)
            plt.plot(time, meditions)
            plt.plot()
            plt.ylabel("Heartbeat")
            plt.xlabel("Time Miliseconds")
            plt.show()
            """
        else:
            print(line)
    except:
        continue
