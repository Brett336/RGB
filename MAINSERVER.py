import serial, socket
from time import sleep

HOST = ""
PORT = 7766
sock = socket.socket()
ON = b"0xF7C03F"
OFF = b"0xF740BF"
White = b"0xF7E01F"
Bright = b"0xF700FF"
Dim = b"0xF7807F"
Red = b"0xF720DF"
Green = b"0xF7A05F"
Blue = b"0xF7609F"
Vape = b"0xF710EF"
OrangeYellow = b"0xF730CF"
DarkYellow = b"0xF708F7"
Yellow = b"0xF728D7"
LightGreen = b"0xF7906F"
GrenBlue= b"0xF7B04F"
Cyan = b"0xF78877"
LightBlue = b"0xF7A857"
DarkBlue = b"0xF750AF"
Purple = b"0xF7708F"
DarkPink = b"0xF748B7"
Pink = b"0xF76897"
Flash = b"0xF7D02F"
Strobe = b"0xF7F00F"
Fade = b"0xF7C837"
Smooth = b"0xF7E817"
ser = serial.Serial("COM5", 9600)
end = 0
try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
sock.listen(5)
while 1:
    # wait to accept a connection - blocking call
    conn, addr = sock.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    com = conn.recv(1024).decode()
    print(com)
    """if com[0] == "&":
        print("Flash list incoming")
        col = []
        while end != 1:
            play = 0
            gom = ""
            gom = conn.recv().decode()
            if gom == "$":
                timer = gom.strip("$")
                timer = float(timer)
                print("Timer set to " + timer + " seconds")
            elif gom == "£":
                leg = len(col)
                i = 0
                while 1:
                    if i + 1 == leg:
                        i = 0
                    else:
                        sleep(timer)
                        ser.write(col[i])
            else:
                print(gom)
                gom = eval(gom)
                col.append(gom)"""

    com = eval(com)
    ser.write(com)
    sleep(0.25)

s.close()
