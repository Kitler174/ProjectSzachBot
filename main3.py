import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 38400)

# Aktualna pozycja kątowa w krokach
m1_pos = 0
m2_pos = 0

# Docelowa pozycja
target_m1 =500  # przykładowa
target_m2 = -500

def send_motor_command(motor, direction):
    command = f"M{motor}{'+' if direction > 0 else '-'}1\n"
    ser.write(command.encode())
    print("Sent:", command.strip())
    time.sleep(0.005)  # krótki czas na wykonanie jednego kroku

while True:
    # Zmienna sterująca może być np. pobierana z trajektorii
    if m1_pos < target_m1:
        send_motor_command(1, 1)
        m1_pos += 1
    elif m1_pos > target_m1:
        send_motor_command(1, -1)
        m1_pos -= 1

    if m2_pos < target_m2:
        send_motor_command(2, 1)
        m2_pos += 1
    elif m2_pos > target_m2:
        send_motor_command(2, -1)
        m2_pos -= 1

    # Można dodać logikę pauzowania / zmiany celu / odbierania wejścia
    if m1_pos == target_m1 and m2_pos == target_m2:
        print("Cel osiągnięty")
        break
