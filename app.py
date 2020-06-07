# 'g1.png
from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
from SD import SD
from pick import pick
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def root():
  return send_from_directory('', 'index.html')

@app.route('/qwe', methods=['POST'])
def upload():
  print(request)
  file = request.files['file']
  if file:
    filename = secure_filename(file.filename)
    file.save(filename)
  time.sleep(2)
  name = SD(filename)
  newBal = pick(name)
  return jsonify({
    "type": "ok",
    "image": newBal
  })

@app.route('/get')
def get():
  return send_file(request.args.get("img"), mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 
