from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
import json
import json_open

app = Flask(__name__)

maxcans = 6
maintenancemax = 100

HLcansAmount = json_openhl.get_data()[0]
PLcansAmount = json_openpl.get_data()[0]

HLsold = json_openhl.get_data()[1]
PLsold = json_openpl.get_data()[0]


def amountpercent(amount, max):
    percent = str((100 / max) * amount)
    return percent[:5] + '%'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/heidelberglaan')
def heidelberglaan():
    return render_template('heidelberglaan.html', HLcansAmount=HLcansAmount, amountpercentcans=amountpercent(HLcansAmount, maxcans),  maxcans=maxcans, maintenancemax=maintenancemax, amountpercentmaintenance=amountpercent(HLsold, maintenancemax), HLsold=HLsold)

@app.route('/padualaan')
def padualaan():
    return render_template('padualaan.html', PLcansAmount=PLcansAmount, amountpercentcans=amountpercent(PLcansAmount, maxcans),  maxcans=maxcans, maintenancemax=maintenancemax, amountpercentmaintenance=amountpercent(PLsold, maintenancemax), PLsold=PLsold)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

def run_site():
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

run_site()

