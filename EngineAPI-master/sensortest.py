import RPi.GPIO as GPIO
import time, datetime

GPIO.setmode(GPIO.BOARD)
meting = 0
amount_cans = 0

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
    global meting, amount_cans
    if meting < 5.5:
        amount_cans = 6
        print("de automaat zit vol")
    elif meting < 11 and meting > 5.5:
        amount_cans = 5
        print("Er is een blikje uit")
    elif meting > 11 and meting < 16.5:
        amount_cans = 4
        print("Er is een blikje uit")
    elif meting > 16.5 and meting < 22:
        amount_cans = 3
        print("Er is een blikje uit")
    elif meting > 22 and meting > 27.5:
        amount_cans = 2
        print("Er is een blikje uit")
    elif meting > 27.5 and meting < 33:
        amount_cans = 1
        print("Er is een blikje uit")
    elif meting > 33 and meting < 38.5:
        amount_cans = 0
        print("De meting is leeg!")
    else:
        print()
        amount_cans = 99

def write_result():
    global amount_cans
    time = datetime.time.hour.minute()
    date = datetime.date.today()
    stock_registration = [amount_cans, date, time]
    print(stock_registration)

def start_machine():
    print("Programma is gestart.")
    button = 10
    led = 8
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    machine_loop = True
    while machine_loop:
        if GPIO.input(button) == 1:
            print("Meting word gestart.")
            GPIO.output(led, 1)
            read_distance()
            calculate_cans()
            time.sleep(0.5)
            GPIO.output(led, 0)

        if GPIO.input(tilt_sensor) == 1:
            print("Er wordt vandalisme gepleegd!")



# read_distance()
start_machine()

