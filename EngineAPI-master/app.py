from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
import json
# from machinefuncties import *

app = Flask(__name__)

maxcans = 6

HLcansAmount = 4
PLcansAmount = 4


def amountpercent(amount, maxcans):
    percent = str((100 / maxcans) * amount)
    return percent[:5] + '%'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/heidelberglaan')
def heidelberglaan():
    return render_template('heidelberglaan.html', HLcansAmount=HLcansAmount, amountpercent=amountpercent(HLcansAmount, maxcans))

@app.route('/padualaan')
def padualaan():
    return render_template('padualaan.html', PLcansAmount=PLcansAmount)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
