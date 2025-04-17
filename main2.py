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
x = 0
y = 9
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
a = input()
x = 0
y =  14
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
#############################1
x = 0
y = 17
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
a = input()
x = 30
y = 10
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
#############################2
x = 30
y = 0
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
a = input()
x = 40
y = 0 
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
                    
#############################3