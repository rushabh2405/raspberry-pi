import time
import board
import digitalio

# Set up the LED pin
led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT

# Blink the LED
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)

