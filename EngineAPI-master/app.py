from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
import json
# from machinefuncties import *

app = Flask(__name__)

maxcans = 6
maintenancemax = 100

HLcansAmount = 3
PLcansAmount = 4

HLsold = 80

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
    return render_template('padualaan.html', PLcansAmount=PLcansAmount)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
