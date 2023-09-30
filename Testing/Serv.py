from flask import Flask, request, send_file

app = Flask(__name__)

# Create a directory for uploads
import os
os.makedirs('uploads', exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("files[]")
    for file in uploaded_files:
        file.save(f"uploads/{file.filename}")
    return "Files uploaded successfully!"


if __name__ == '__main__':
    app.run(debug=True)
