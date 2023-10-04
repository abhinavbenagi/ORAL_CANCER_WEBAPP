# ORAL CANCER WEBAPP

### Local Environment Setup

---

To set up the project on your local environment, follow the following setup procedure:

- run the following command to install the requirements
  
  ```
  $ pip install -r requirements.txt
  ```
- Create a ``` .env ``` file and store the username and password of the monogDB Atlas server as ```USERDATA``` and ```DATAPASSKEY```.
- run the flask server

  ```
  $ python app.py
  ``` 

### API Documentation
---

The endpoints accessible are as follows:

- ```/signup``` : POST method to register a user. Takes username and password as the request body.
- ```/login``` : POST method to login a registered user. Takes username and password as the request body.
- ```/upload``` : POST method to upload the scan images of the user. Takes username as body parameter and multiple files containing the images.
  Returns the status of the request, original image paths and processed image paths on server along with unique image id of each image that has been stored on the server as a JSON object.
- ```/upload/<file_id>``` : GET method to retrieve the particular original scan image with the unique file id from the server.
-  ```/generated/<file_id>``` : GET method to retrieve the particular processed scan image with the unique file id from the server.
