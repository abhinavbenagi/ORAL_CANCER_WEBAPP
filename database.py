from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(filename='test_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

username = os.getenv('USERDATA')
password = os.getenv('DATAPASSKEY')
uri = f"mongodb+srv://{username}:{password}@oralcancer.l78fama.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
class database():
    def __init__(self):
        try:
            logging.info("Initiating database connection")
            client.admin.command('ping')
            db = client['PatientData']
            self.login = db['Login_Credentials']
            self.images = db['Scan_Image']
            self.output = db['Output_Image']
            logging.info("Database connection successful")
        except Exception as e:
            logging.error("Database connection failed")
            return
    
    def check_login(self, username, password):
        try:
            logging.info("Checking login credentials")
            user = self.login.find_one({'username': username})
            if user['password'] == password:
                logging.info("Login credentials verified")
                return True
            else:
                logging.info("Login credentials verification failed")
                return False
        except Exception as e:
            logging.error("Login credentials verification failed")
            return False
    
    def signup_data(self, username, password):
        try:
            user = self.login.find_one({'username': username})
            if user:
                logging.info("User Already Exists! Choose another username!")
                return False
            logging.info("Inserting sign up data")
            self.login.insert_one({'username': username, 'password': password})
            logging.info("Sign up data inserted")
            return True
        except Exception as e:
            logging.error("Sign up data insertion failed")
            return False

    def upload_image(self, username, inp_image, out_image):
        try:
            logging.info("Uploading image to database")
            self.images.insert_one({'username': username, 'input_image': image, "output_image": out_image})
            logging.info("Database update successful")
            return True
        except Exception as e:
            logging.error("Image upload failed")
            return False