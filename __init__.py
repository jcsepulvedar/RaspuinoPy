import serial

def __init__(self):
    #Assuming you're connecting an Arduino
    try:
        ser = serial.Serial("/dev/ttyACM0",9600)
    except:
        ser = serial.Serial("/dev/ttyACM1",9600)

    while True:   
        print("Start")
        print("Waiting...")

        command = ser.read()
        try: command = str(command, "utf-8")
        except: command = str(command, "utf-16")

        if (command =="h"): print("Hello")