import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
meting = 0

def read_distance():
    global meting
    TRIG = 16
    ECHO = 18

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, 0)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(0.1)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    meting = (stop - start) * 17000
    if meting > 2000:
        print("probeer opnieuw")
    else:
        print("{0:.2f} Centimeter".format(meting))

def calculate_cans():
    global meting
    if meting < 5.5:
        print("de automaat zit vol")
    elif meting < 11 and meting > 5.5:
        print("Er is een blikje uit")
    else:
        print("De automaat is leeg.")


def start_machine():
    print("Programma is gestart.")
    button = 10
    led = 8
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    testscript = True
    while testscript:
        if GPIO.input(button) == 1:
            print("Meting word gestart.")
            GPIO.output(led, 1)
            read_distance()
            calculate_cans()
            time.sleep(0.5)
            GPIO.output(led, 0)


def led_blink():
    LED = 8
    GPIO.setup(LED, GPIO.OUT)

    for i in range(0, 10):
        GPIO.output(LED, 1)
        print("Ik ga aan")
        time.sleep(1)
        GPIO.output(LED, 0)
        print("Ik ga uit")
        time.sleep(2)

    print("Ik ben klaar")


# read_distance()
start_machine()
# led_blink()
