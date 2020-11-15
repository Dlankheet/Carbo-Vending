import json

def open_recorddata(location):
    if location == "PL":
        with open('record_dataPL.json') as f:
            recorddata = json.load(f)
            return recorddata

    else:
        with open('record_dataHL.json') as f:
            recorddata = json.load(f)
            return recorddata

def get_data(location):
    recorddata = open_recorddata(location)
    records = len(recorddata['records']) - 1
    amount_cans = recorddata['records'][records]['Amount']
    amount_sold = recorddata['records'][records]['Sold']
    amount_maintenance = recorddata['records'][records]['Maintenance']
    #tijd = recorddata['records'][records]['Tijd']
    # print(recorddata)
    # print("Aantalblikjes = {} om {}".format(amount_cans, tijd))
    # print("Aantal verkocht = {}".format(amount_sold))
    return(amount_cans, amount_sold, amount_maintenance)

#print(get_data())
