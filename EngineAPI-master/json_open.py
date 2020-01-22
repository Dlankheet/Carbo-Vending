import json

def open_recorddata():
    with open('record_data.json') as f:
        recorddata = json.load(f)
        return recorddata

def get_data():
    recorddata = open_recorddata()
    records = len(recorddata['records']) - 1
    amount_cans = recorddata['records'][records]['Amount']
    amount_sold = recorddata['records'][records]['Sold']
    tijd = recorddata['records'][records]['Tijd']
    print(recorddata)
    print("Aantalblikjes = {} om {}".format(amount_cans, tijd))
    print("Aantal verkocht = {}".format(amount_sold))
    return(amount_cans, amount_sold)

