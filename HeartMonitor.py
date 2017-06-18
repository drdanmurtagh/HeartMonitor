import serial #Handles Serioal IO with the USB COM port from teh Photon board    
import numpy as np         
import io 
import matplotlib.pyplot as plt
import time #Useful for timing
from scipy import signal

try: 
    ser = serial.Serial('COM4', 9600, timeout = 2) #Opens the COM port for serial IO 
except Exception : 
    ser.close()
    ser = serial.Serial('COM4', 9600, timeout = 2) #Opens the COM port for serial IO 
    
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser)) #Setup a text reader for the open serial port 
s=[]; #Signal Array
t=[]; #Time Array 
t0 =  float(time.time()*1000) #Get the t0 

# Doing a really dodgy loop here where to break out you have to throw a CTRL+C 
try:  
    while True:
        V = (float(sio.readline())) #I know that the Analog Input read from the photon board is just going to throw a number in mV
        s.append(V) #Save the value in the signal 
        t.append(float(time.time()*1000) - t0) #Update the time (n.b. there will be an offset from 0 as it take stime to get here from the t0 def) 
        op = "Voltage = {0:.2f} V".format(V) #Format a string and print the OP 
        print(op) 
        time.sleep(0.01) #Wait 10ms 
except KeyboardInterrupt :   #So when you CTRL+C 
    ser.close() #Close the serial port 
    fig = plt.figure(num = 1, figsize = (10,10))  #Plot the raw input data 
    plt.xlabel('Index')
    plt.ylabel('Voltage (mV)')
    plt.plot((s))
    plt.show()
    fig = plt.figure(num = 2, figsize = (10,10)) #Plot the timed inut data 
    plt.xlabel('Time (mS)')
    plt.ylabel('Voltage (mV)')
    plt.plot(t,s)
    plt.show()