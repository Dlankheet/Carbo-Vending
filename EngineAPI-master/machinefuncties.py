from gpiozero import *
from time import *
from datetime import *
import json
import json_open
import app


meting = 0
amount_cans = 0
stock_registration = [0]
sold = 0
record = []
hl_file = 'record_data_hl.json'
pl_file = 'record_data_pl.json'

def open_record():
    with open(hl_file) as f:
        recorddata = json.load(f)
        return recorddata


def write_record(new_recorddata):
    with open(pl_file, 'w') as f:
        json.dump(new_recorddata, f, indent=2)


def vandalism_alarm():
    """Laat buzzer afgaan voor aantal keer in range. """
    buzzer = Buzzer(9)
    for i in range(0, 1):
        print("letop vandalisme")
        buzzer.on()
        sleep(1)
        buzzer.off()
        sleep(1)


def read_distance():
    global meting
    distance_sensor = DistanceSensor(echo=24, trigger=23)
    distance_sensor.max_distance = 0.4
    # error = distance_sensor.value()
    # if error >= 1:
    #    meting = 99
    meting = (distance_sensor.distance * 100)
    print("{0:.2f} Centimeter".format(meting))
    calculate_cans()

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


def create_record():
    global amount_cans, stock_registration, sold, record
    date = str(datetime.now().strftime("%Y-%m-%d"))
    time = str(datetime.now().strftime("%H:%M:%S"))
    if amount_cans < 99 and amount_cans != stock_registration[0]:
        record = {"Tijd": time, "Date": date, "Amount": amount_cans, "Sold": sold}
        recorddata = open_record()
        recorddata["records"].append(record)
        write_record(recorddata)


def start_machine():
    global sold
    print("Programma is gestart.")
    button = Button(15)
    led = LED(14)
    tilt = Button(10)
    machine_loop = True
    while machine_loop:
        if button.value == 1:
            print("Meting word gestart.")
            sold += 1
            led.on()
            read_distance()
            create_record()
            sleep(0.5)
            led.off()

        # if tilt.value == 0:
        #     led.on()
        #     vandalism_alarm()
        #     led.off()

start_machine()