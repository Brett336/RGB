from time import sleep
import serial
fullword = ""
ON = b"0xF7C03F"
OFF = b"0xF740BF"

morseAlphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/"
        }
msg = input("Type message >: ")
msg = msg.upper()
for i in range(len(msg)):
    b = msg[i]
    #print (b)
    #print (morseAlphabet[b])
    fullword = fullword+morseAlphabet[b]
print(fullword)
full = "."+fullword
fullword = full
port = input("Input The Port")
ser = serial.Serial(port,9600)
ser.write(OFF)
print(len(fullword))

for i in range(len(fullword)):
    ser.write(OFF)
    sleep(0.5)
    if fullword[i]== "!":
        sleep(1)
    elif fullword[i]=="/":
        sleep(3.0)
    elif fullword[i]==".":
        print("Sending .")
        ser.write(ON)
        sleep(0.5)

    elif fullword[i]=="-":
        print("Sending -")
        ser.write(ON)
        sleep(1.5)

    else:
        ()
    #print(i)
    print(fullword[i])


