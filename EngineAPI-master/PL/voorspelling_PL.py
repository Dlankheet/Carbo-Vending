from datetime import *
import calendar
import json

# Open de json file en return het gehele bestand
def open_recorddata():
    with open('record_dataPL.json') as file:
        recorddata = json.load(file)
        return recorddata

# Returned een lijst uit de json file, exlusief de eerste record. (Eerste record is leeg)
def get_record_list():
    recorddata = open_recorddata()
    record_list = recorddata['records']
    return record_list[1:]

# Returned een lijst met data binnen het ingestelde tijdsframe (default 14 dagen in het verleden, vanaf vandaag)
def get_timeframe_data():
    today = date.today()
    startdate = today - timedelta(days=21)
    record_list = get_record_list()
    timeframe_data = []

    for record in record_list:
        record_date = datetime.strptime(record['Date'], '%Y-%m-%d').date()
        if startdate <= record_date <= today:
            timeframe_data.append(record)
    return timeframe_data

# Returned de dag naam van een gegeven record als een string in het Engels ('Monday', 'Tuesday' etc..)
def get_day_name(record):
    record_date = datetime.strptime(record['Date'], '%Y-%m-%d').date()
    record_day_name = calendar.day_name[record_date.weekday()]
    return record_day_name

# Haal alle records op van een bepaalde datum
def get_date_data(date):
    timeframe_data = get_timeframe_data()
    date_data = []

    for record in timeframe_data:
        if record['Date'] == date:
            date_data.append(record)
    return date_data

# Return alle records van een gegeven dag (Parameter is een string bijvoorbeeld: 'Friday')
def get_day_data(day):
    timeframe_data = get_timeframe_data()
    day_data = []

    for record in timeframe_data:
        if get_day_name(record) == day:
            day_data.append(record)
    return day_data

# Return het aantal blikjes dat verkocht is op een gegeven datum (Parameter is een string bijvoorbeeld: '2020-01-17')
def amount_sold_on(date):
    sold_list = []
    date_data = get_date_data(date)

    for record in date_data:
        sold_list.append(record['Sold'])
    amount_sold_on_date = (max(sold_list) - min(sold_list))
    return amount_sold_on_date

# Return een dictionary met aantal blikjes verkocht per datum (Parameter is een string bijv: 'Friday')
def get_selling_data(day):
    day_data = get_day_data(day)
    selling_data = {}

    for record in day_data:
        date = record['Date']
        selling_data[date] = amount_sold_on(date)
    return selling_data

# Reken het verschil uit tussen twee getallen
def difference(n1, n2):
    if n1 <= n2:
        return n2 - n1
    else:
        return n1 - n2

# Doe een voorspelling voor de gegeven dag
def sell_prediction(day):
    selling_data = get_selling_data(day)
    selling_data_list = []

    for record in selling_data:
        selling_data_list.append(selling_data[record])
    if len(selling_data_list) > 3:
        selling_data_list = selling_data_list[1:]

    first_day = selling_data_list[0]
    second_day = selling_data_list[1]
    third_day = selling_data_list[2]

    if first_day == second_day == third_day:
        prediction = third_day
    if first_day < second_day < third_day:
        if difference(difference(first_day, second_day), difference(second_day, third_day)) == 0:
            prediction = third_day + difference(second_day, third_day)
        else:
            prediction = third_day + difference(difference(first_day, second_day), difference(second_day, third_day))
    if first_day > second_day > third_day:
        if difference(difference(first_day, second_day), difference(second_day, third_day)) == 0:
            prediction = third_day - difference(second_day, third_day)
            if prediction < 0:
                prediction = 0
        else:
            prediction = third_day - difference(difference(first_day, second_day), difference(second_day, third_day))
            if prediction < 0:
                prediction = 0
    if first_day > second_day < third_day or first_day < second_day > third_day:
        prediction = (first_day + second_day + third_day) // len(selling_data_list)
    if first_day == second_day:
        if second_day > third_day:
            prediction = third_day - difference(second_day, third_day)
            if prediction < 0:
                prediction = 0
        if second_day < third_day:
            prediction = third_day + difference(second_day, third_day)
    if second_day == third_day:
        if first_day > third_day:
            prediction = third_day - difference(first_day, third_day)
        if first_day < third_day:
            prediction = third_day + difference(first_day, third_day)

    return 'On {} approximately {} cans will be sold'.format(day, prediction)

def get_week_prediction():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    predictions = []
    for day in days:
        predictions.append(sell_prediction(day))
    return predictions