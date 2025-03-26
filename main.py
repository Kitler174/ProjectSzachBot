import time
import serial
import time

ser = serial.Serial("/dev/ttyUSB0",38400)  # 'COM3' dla Windows, '/dev/ttyUSB0' dla Linux/Mac
time.sleep(2)

TOTAL_STEPS_PER_REV = 3200
def send_data(data):
    ser.write(data.encode())
    data = ser.readline()
    print(data)
tagx = 0
tagy = 0

miny = -30000
maxy = 30000
maxx = 150000
minx = 0

# 🔹 Główna pętla gry
running = True
while running:
    x = input("kord x >>> ")
    y = input("kord y >>> ")
    try:
        x = int(x)
        y = int(y)
        if x > maxx or x < minx or y > maxy or y < miny:
            print("max x:",maxx," min x",minx,"max y:",maxy," min y:",miny)
            print("Operacja nieudana")
        else:
            while(tagx != x or tagy != y):
                if tagx > x:
                    send_data('d')
                    tagx-=1
                elif tagx < x:
                    send_data('a')
                    tagx+=1
                if tagy > y:
                    send_data('s')
                    tagy-=1
                elif tagy < y:    
                    send_data('w')
                    tagy+=1
            print(f"Osiągnięto punkt x:{x}  y:{y}")
    except Exception:
        pass
