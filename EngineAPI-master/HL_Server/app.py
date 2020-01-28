from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
import json
import json_open

app = Flask(__name__)

maxcans = 6
maintenancemax = 100

def amountpercent(amount, max):
    percent = str((100 / max) * amount)
    return percent[:5] + '%'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/heidelberglaan')
def heidelberglaan():
    HLcansAmount = json_open.get_data("HL")[0]
    HLsold = json_open.get_data("HL")[1]
    return render_template('heidelberglaan.html', HLcansAmount=HLcansAmount, amountpercentcans=amountpercent(HLcansAmount, maxcans),  maxcans=maxcans, maintenancemax=maintenancemax, amountpercentmaintenance=amountpercent(HLsold, maintenancemax), HLsold=HLsold)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

def run_site():
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

run_site()

