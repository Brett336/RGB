import serial
from random import randint
from time import sleep
HOST = "BRETTPC"
PORT = 7766
#sock = socket.socket()
ON = b"0xF7C03F"
OFF = b"0xF740BF"
White = b"0xF7E01F"
Bright = b"0xF700FF"
Dim = b"0xF7807F"
Red = b"0xF720DF"
Green = b"0xF7A05F"
Blue = b"0xF7609F"
r2 = b"0xF710EF"
r3 = b"0xF730CF"
r4 = b"0xF708F7"
r5 = b"0xF728D7"
g2 = b"0xF7906F"
g3 = b"0xF7B04F"
g4 = b"0xF78877"
g5 = b"0xF7A857"
b2 = b"0xF750AF"
b3 = b"0xF7708F"
b4 = b"0xF748B7"
b5 = b"0xF76897"
Flash = b"0xF7D02F"
Strobe = b"0xF7F00F"
Fade = b"0xF7C837"
Smooth = b"0xF7E817"
ser = serial.Serial("COM5", 9600)

color = []
col =""
while col !="$":
    col = input("Input color " + str(len(color)) + ". Type $ to stop  >: ")
    if col == "$":
        print ("End of color")
    else:
        col = eval(col)
        color.append(col)
timer = float(input("Input how fast. 0.25 min >: "))
print ("You have selected these colours ")
print (color)
print (len(color))
randome = input("Do you want a random order? y or n >: ")
max = len(color)-1
if randome == "y":
    j = 255
    while 1:
        i = randint(0,max)
        if i == j:
            ()
        else:
            ser.write(color[i])
            sleep(timer)
            j = i
elif randome == "n":
    max = len(color)
    i = 0
    while 1:
        """if i == max:
            i=0"""
        for i in range(len(color)):
            ser.write(color[int(i)])
            sleep(timer)

else:
    print ("invalid")






