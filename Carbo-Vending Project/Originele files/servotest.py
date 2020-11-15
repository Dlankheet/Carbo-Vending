from time import sleep
from gpiozero import *

servo = Servo(7)
button = Button(15)
while True:
    if button.value == 1:
        print("button is pressed")
        servo.max()
        sleep(1)
        servo.min()
        sleep(1)