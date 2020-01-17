from gpiozero import *
from time import *
from datetime import *

meting = 0
amount_cans = 0

def vandalism_alarm():
    buzzer = Buzzer(9)
    for i in range(0, 5):
        buzzer.on()
        sleep(1)
        buzzer.off()

def read_distance():
    global meting
    distance_sensor = DistanceSensor(echo=24, trigger=24)
    distance_sensor.max_distance = 0.4
    error = distance_sensor.value()
    if error >= 1:
        meting = 99
    meting = (distance_sensor.distance * 100)
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
    if amount_cans < 99:
        stock_registration = [amount_cans, date, time]
        print(stock_registration)

def start_machine():
    print("Programma is gestart.")
    button = Button(15)
    led = LED(14)
    tilt = Button(15)
    machine_loop = True
    while machine_loop:
        if button.value == 1:
            print("Meting word gestart.")
            led.on()
            read_distance()
            calculate_cans()
            time.sleep(0.5)
            led.off()

        if tilt.vaulue == 1:
            led.on()
            vandalism_alarm()
            led.off()

#read_distance()
start_machine()
