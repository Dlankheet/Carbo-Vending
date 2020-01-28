from gpiozero import *
from time import *
from datetime import *
import json

file = 'record_dataHL.json'
maintenance_value = 0

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
    return calculate_cans(meting)


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
    elif meting > 22 and meting < 27.5:
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
        amount_cans = 101
        return amount_cans


def create_record():
    global maintenance_value
    date = str(datetime.now().strftime("%Y-%m-%d"))
    time = str(datetime.now().strftime("%H:%M:%S"))
    recorddata = open_record()
    amount_cans = read_distance()
    sold = recorddata['records'][len(recorddata['records']) - 1]['Sold']
    if maintenance_value == 1:
        maintenance_counter = 0
        maintenance_value = 0
    else:
        maintenance_counter = recorddata['records'][len(recorddata['records']) - 1]['Maintenance']

    print("Amount of cans {}".format(amount_cans))
    print("Old data {}".format(recorddata['records'][len(recorddata['records']) - 1]))

    if amount_cans < 99 and recorddata['records'][len(recorddata['records']) - 1]['Amount'] != amount_cans:
        sold += 1
        maintenance_counter += 1
        record = {"Time": time, "Date": date, "Amount": amount_cans, "Sold": sold, "Maintenance": maintenance_counter}
        print("New data {}".format(record))
        recorddata["records"].append(record)
        write_record(recorddata)
    else:
        print("De record is niet veranderd")


def start_machine():
    global maintenance_value
    print("Programma is gestart.")
    button = Button(15)
    tilt = Button(10)
    maintenance_button = Button(11)
    machine_loop = True
    while machine_loop:
        if button.value == 1:
            print("Meting word gestart.")
            sleep(1)
            create_record()

        if maintenance_button.value == 1:
            maintenance_value = 1
            sleep(1)
            print("Onderhoudsknop is ingedrukt.")

        if tilt.value == 0:
            sleep(0.3)
            if tilt.value == 0:
                vandalism_alarm()


start_machine()
