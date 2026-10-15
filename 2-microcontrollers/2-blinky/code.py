import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print("on")
    time.sleep(1)
    led.value = False
    print("off")
    time.sleep(1)
