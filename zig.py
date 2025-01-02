# receiving side
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=.5)
while True:
    incoming = ser.readline().strip().decode('utf-8')  # Decode bytes to string
    if incoming == "":
        print('Received data: ' + incoming)
    elif incoming[0] == "2":
        print('Received data: ' + incoming)


# sending side
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=.5)

while True:
    ser.write(b'1 1827 \r\n')  # Note the b before the string to send bytes 
    ser.write(b'2 9282 \r\n')
    incoming = ser.readline().strip().decode('utf-8')  # Decode bytes to string
    print('Received Data: ' + incoming)