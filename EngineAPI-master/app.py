from flask import Flask, send_from_directory, jsonify, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("/index.html", code=302)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=False)

if __name__ == '__main__':
    app.run()
