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
@app.route('/padualaan')
def padualaan():
    PLcansAmount = json_open.get_data("PL")[0]
    PLsold = json_open.get_data("PL")[0]
    return render_template('padualaan.html', PLcansAmount=PLcansAmount, amountpercentcans=amountpercent(PLcansAmount, maxcans),  maxcans=maxcans, maintenancemax=maintenancemax, amountpercentmaintenance=amountpercent(PLsold, maintenancemax), PLsold=PLsold)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

def run_site():
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

run_site()

