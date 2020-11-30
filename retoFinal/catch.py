from p1 import getSerialConnector

ser = getSerialConnector(9600, "COM3")


while True:
    stuff = str(input("Enter Somethig:"))
    ser.write(stuff)
    line = ser.readline()
    sent = line.decode("ascii")
    print(line)
