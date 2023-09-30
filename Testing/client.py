import requests

# Define the URL of the Flask server
url = 'http://127.0.0.1:5000/upload'

# List of file paths to images you want to upload
files = [
    ('files[]', open('test_image.jpg', 'rb')),
    ('files[]', open('image.jpg', 'rb')),
    # Add more files as needed
]

# Send a POST request to upload the images
response = requests.post(url, files=files)

# Check if the request was successful
if response.status_code == 200:
    print("Images uploaded successfully!")
else:
    print(f"Error uploading images. Status code: {response.status_code}")
