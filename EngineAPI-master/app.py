from flask import Flask, send_from_directory, jsonify, redirect, request, render_template
# from machinefuncties import *

app = Flask(__name__)

posts = [
    {
        'author': 'Jordan Peterson',
        'title': '12 Rules for life',
        'content': 'eye opening book',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'George Orwell',
        'title': '1984',
        'content': 'very scary book',
        'date_posted': 'April 28, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/heidelberglaan')
def heidelberglaan():
    return render_template('heidelberglaan.html')

@app.route('/padualaan')
def padualaan():
    return render_template('padualaan.html')

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
