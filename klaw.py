import pygame
import time
import serial
import time

# Ustawienia portu szeregowego (zmień na odpowiedni port COM)
ser = serial.Serial("/dev/ttyUSB0",38400)  # 'COM3' dla Windows, '/dev/ttyUSB0' dla Linux/Mac
time.sleep(2)

TOTAL_STEPS_PER_REV = 3200
def send_data(data):
    ser.write(data.encode())  # Zamień dane na bajty i wyślij przez port szeregowy
    data = ser.readline()

    print(f'Odebrano: {data}')
# 🔹 Inicjalizacja Pygame
pygame.init()

# 🔹 Ustawienia okna
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sterowanie Strzałkami")

# 🔹 Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 🔹 Główna pętla gry
running = True
while running:
    screen.fill(WHITE)  # Czyszczenie ekranu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Obsługa klawiszy
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_data('a')
                send_data('a')
                send_data('a')
                send_data('a')
            elif event.key == pygame.K_DOWN:
                send_data('d')
                send_data('d')
                send_data('d')
                send_data('d')
            elif event.key == pygame.K_LEFT:
                send_data('w')
                send_data('w')
                send_data('w')
                send_data('w')
            elif event.key == pygame.K_RIGHT:
                send_data('s')
                send_data('s')
                send_data('s')
                send_data('s')

    pygame.display.flip()  # Aktualizacja ekranu

# 🔹 Zamykanie Pygame
pygame.quit()
