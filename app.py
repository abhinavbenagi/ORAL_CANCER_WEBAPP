from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import os
from database import *
from classfication import *

app = Flask(__name__)
db = database() #initiate database connection. Refer to database.py

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request['username']
        password = request['password']
        if db.signup_data(username, password):
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failed'})

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request['username']
        password = request['password']
        if db.check_login(username, password):
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failed'})

@app.route('/upload/<string:username>', methods=['POST'])
def upload(username):
    if request.method == 'POST':
        try:
            uploaded_files = request.files.getlist("files[]")
            user = username
            logging.info("Data received!")
        
            #Processing the data
            obj = classification()
            obj.caller_function(uploaded_files)

            for image_name in obj.outputfilenames:
                file_path = os.path.join(obj.output_dir, image_name)

                if os.path.exists(file_path):
                    yield send_file(file_path, mimetype='image/jpeg')
                else:
                    yield f"Image {image_name} not found", 404

            obj.destruct()
            return jsonify({'status': 'success'})
            
        except:
            return jsonify({'status': 'failed'})



if __name__ == '__main__':
    app.run(debug=True)