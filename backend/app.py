from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import os
import uuid
from database import *
from classfication import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}})
app.config["UPLOADS_DEFAULT_DEST"] = "uploads/original"
app.config["UPLOADED_IMAGES_DEST"] = "uploads/original"
app.config["PROCESSED_IMAGES_DEST"] = "uploads/generated"
app.config["UPLOADED_IMAGES_URL"] = "/uploads/original/"


db = database()  # initiate database connection. Refer to database.py


@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.signup_data(username, password):
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.check_login(username, password):
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})


@app.route("/upload", methods=["POST"])
def upload_files():
    if "images" in request.files:
        file_list = request.files.getlist("images")
        user_name = request.form.get("user_name")

        user_images = []
        model_images = []

        for file in file_list:
            filename = file.filename
            image_id = str(uuid.uuid4())
            file_path = os.path.join(
                app.config["UPLOADED_IMAGES_DEST"], image_id + ".jpg"
            )
            file.save(file_path)
            user_images.append([image_id, file_path])
            logging.info(f"Image {filename} saved to {file_path}")

        data = classification()
        model_images = data.caller_function(user_images)

        logging.info(user_images)
        logging.info(model_images)

        if db.upload_image(user_name, user_images, model_images):
            return jsonify(
                {
                    "status": "success",
                    "user_images": user_images,
                    "model_images": model_images,
                    "user_name": user_name,
                }
            )
        else:
            return jsonify({"status": "failed"})


@app.route("/uploads/<filename>")
def uploaded_original_file(filename):
    return send_from_directory(app.config["UPLOADS_DEFAULT_DEST"], filename)


@app.route("/generated/<filename>")
def uploaded_generated_file(filename):
    return send_from_directory(app.config["PROCESSED_IMAGES_DEST"], filename)


if __name__ == "__main__":
    app.run(debug=True)
