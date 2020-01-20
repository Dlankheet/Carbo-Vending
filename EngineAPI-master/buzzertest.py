from gpiozero import Buzzer, Button
from time import sleep

buzzer = Buzzer(9)
button = Button(15)

while True:
        print("waiting")
        button.wait_for_press()
        print("The button was pressed!")
        buzzer.on()
        sleep(0.1)
        buzzer.off()

# def led_blink():
#     LED = 8
#     GPIO.setup(LED, GPIO.OUT)
#
#     for i in range(0, 10):
#         GPIO.output(LED, 1)
#         print("Ik ga aan")
#         time.sleep(1)
#         GPIO.output(LED, 0)
#         print("Ik ga uit")
#         time.sleep(2)
#
#     print("Ik ben klaar")


