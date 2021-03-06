import serial


ser = serial.Serial("COM5", 9600)
hrValues = []
miliValues = []


def analisisHR():
    global hrValues
    global miliValues
    valores = []
    valoresMili = []
    for i in range(0, 97):
        valores.append((hrValues[i]+hrValues[i+1]+hrValues[i+2])/3)
        valoresMili.append((milivalues[i]+hrValues[i+1]+hrValues[i+2])/3)
    hrValues = hrValues[25:]
    miliValues = miliValues[25:]


while(1):
    lineBytes = ser.readline()
    line = lineBytes.decode("utf-8")
    if line[0:2] != "HR":
        continue
    line = line.rstrip()
    medidas = line.split(";")
    hr = int(medidas[0].split(":")[1])
    milis = int(medidas[1].split(":")[1])
    print(hr)


"""
import serial
hr_values = list()
mil_values = list()


def analisisHR():
    global hr_values
    global mil_values
    hr_values = hr_values[25:]
    mil_values = mil_values[25:]


ser = serial.Serial("COM5", 9600)
while(1):
    lineBytes = ser.readline()
    line = lineBytes.decode("ascii")
    if line[0:2] != "HR":
        continue
    line = line.rstrip()
    medidas = line.split(";")
    hr = int(medidas[0].split(":")[1])
    milis = int(medidas[1].split(":")[1])
    hr_values.append(hr)
    mil_values.append(milis)
    print(hr)

"""
"""
import serial

ser = serial.Serial("COM4", 9600)
while(1):
    lineBytes = ser.readline()
    line = lineBytes.decode("ascii")
    line = line.rstrip()
    measures = line.split(";")
    HR = measures[0].split(":")[1]
    mSconds = measures[1].split(":")[1]
    print((HR, mSconds))
"""
