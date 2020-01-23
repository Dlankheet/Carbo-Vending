from gpiozero import *
from time import *
from datetime import *
import json


amount_cans = 0
stock_registration = [0]
sold = 0
record = []
file = 'record_dataPL.json'

def open_record():
    '''Deze opent de Json file aan de hand van de variabele "file" bovenaan.'''
    with open(file) as f:
        recorddata = json.load(f)
        return recorddata


def write_record(new_recorddata):
    '''Deze functie schrijft de data weg die in create_record() gemaakt word.'''
    with open(file, 'w') as f:
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
    '''Deze functie meet de afstand.'''
    distance_sensor = DistanceSensor(echo=24, trigger=23)
    distance_sensor.max_distance = 0.4
    # error = distance_sensor.value()
    # if error >= 1:
    #    meting = 99
    meting = (distance_sensor.distance * 100)
    print("{0:.2f} Centimeter".format(meting))
    calculate_cans(meting)

def calculate_cans(meting):
    '''Aan de hand van de meting word er berekend hoeveel blikken er nog in de automaat zitten. '''
    if meting < 5.5:
        amount_cans = 6
        return amount_cans
        print("De automaat zit vol")
    elif meting < 11 and meting > 5.5:
        amount_cans = 5
        return amount_cans
        print("Er zijn blikjes uit.")
    elif meting > 11 and meting < 16.5:
        amount_cans = 4
        return amount_cans
        print("Er zijn blikjes uit.")
    elif meting > 16.5 and meting < 22:
        amount_cans = 3
        return amount_cans
        print("Er zijn blikjes uit.")
    elif meting > 22 and meting > 27.5:
        amount_cans = 2
        return amount_cans
        print("Er zijn blikjes uit.")
    elif meting > 27.5 and meting < 33:
        amount_cans = 1
        return amount_cans
        print("Letop, er is nog een blikje over.")
    elif meting > 33 and meting < 38.5:
        amount_cans = 0
        return amount_cans
        print("De automaat is leeg")
    else:
        print("Dit was een foutieve meting")
        amount_cans = 100


def create_record():
    global amount_cans, stock_registration, sold, record
    date = str(datetime.now().strftime("%Y-%m-%d"))
    time = str(datetime.now().strftime("%H:%M:%S"))
    recorddata = open_record()
    if amount_cans < 99 and amount_cans != stock_registration[0] and recorddata['records'][len(recorddata['records']) - 1]['Amount'] != amount_cans:
        sold += 1
        record = {"Tijd": time, "Date": date, "Amount": amount_cans, "Sold": sold}
        recorddata["records"].append(record)
        write_record(recorddata)
    else:
        print("De record is niet veranderd")


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