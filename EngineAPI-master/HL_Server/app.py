from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
import json
import json_open
import voorspelling_HL

app = Flask(__name__)

maxcans = 6
maintenancemax = 200

predictions = voorspelling_HL.get_week_prediction()

def amountpercent(amount, max):
    percent = (100 / max) * amount
    if percent > 100:
        percent = str(100)
    else:
        percent = str(percent)
    return percent[:5] + '%'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/heidelberglaan')
def heidelberglaan():
    HLcansAmount = json_open.get_data("HL")[0]
    HLsold = json_open.get_data("HL")[1]
    HLmaintenance = json_open.get_data("HL")[2]
    print(HLcansAmount, HLsold, HLmaintenance)
    return render_template('heidelberglaan.html',
                           HLcansAmount=HLcansAmount,
                           amountpercentcans=amountpercent(HLcansAmount, maxcans),
                           maxcans=maxcans, maintenancemax=maintenancemax,
                           amountpercentmaintenance=amountpercent(HLmaintenance, maintenancemax),
                           HLsold=HLsold,
                           HLmaintenance=HLmaintenance,
                           predictions=predictions)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

def run_site():
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

run_site()

