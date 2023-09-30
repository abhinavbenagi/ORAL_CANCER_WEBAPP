import os
from PIL import Image
from ultralytics import YOLO
import io
import base64
import logging

logging.basicConfig(filename='test_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class classification():
    def __init__(self):
        self.model = YOLO('best (1).pt')
        self.output_dir = "uploads/"
        os.makedirs(self.output_dir, exist_ok=True)
        self.image_byte_strings=[] #contains byte strings of input images
        self.output = [] #contains byte strings of model output
        self.outputfilenames =[] #path where the model has saved the images
        self.filenames =[] #filenames of input images
        self.input_path=[] #complete path where input images are saved
        logging.info("Classification class initialization successful")

    def byte_string_to_image(self,byte_string):
        '''
        Converts byte string to image
        '''
        decoded_byte_string = base64.b64decode(byte_string)
        byte_stream = io.BytesIO(decoded_byte_string)
        image = Image.open(byte_stream)
        logging.info("Byte string to image conversion successful")
        return image

    def convert_images_to_byte_strings(self,image_paths):
        '''
        Converts images to byte strings
        '''
        for path in image_paths:
            with open(path, 'rb') as img_file:
                img = Image.open(img_file)
                byte_array = io.BytesIO()
                img.save(byte_array, format='jpeg')
                byte_array = byte_array.getvalue()
                byte_string = base64.b64encode(byte_array).decode('utf-8')
                self.image_byte_strings.append(byte_string)


    def save_image_to_disk(self,image,filename):
        '''
        saves image to disk
        '''
        image.save(os.path.join(self.output_dir, filename))
        logging.info(f"Image saved to disk :- {self.output_dir}/{filename}")

    def delete_image_from_disk(self,filenames):
        '''
        deletes image from disk
        '''
        for filename in filenames:
            os.remove(os.path.join(self.output_dir, filename))
            logging.info(f"Image deleted from disk :- {self.output_dir}/{filename}")


    
    def caller_function(self,uploaded_files):
        logging.info("caller function initiated")

        # for i, byte_string in enumerate(byte_strings):
        #     image = self.byte_string_to_image(byte_string)
        #     filename = f"image_{i}.png"
        #     self.save_image_to_disk(image, filename)
        #     image_path = os.path.join(self.output_dir, filename)
        #     self.input_path.append(image_path)
        #     self.filenames.append(filename)

        for file in uploaded_files:
            file.save(f"uploads/{file.filename}")
            self.input_path.append(f"uploads/{file.filename}")
            self.filenames.append(file.filename)

        self.convert_images_to_byte_strings(self.input_path)
        logging.info("Finished converting to actual images.")

        results_list = self.model.predict(self.input_path)
        logging.info("Finished model prediction")

        for i, results in enumerate(results_list):
            byte_stream = io.BytesIO()
            im_array = results.plot()
            im = Image.fromarray(im_array)
            im.save(f'uploads/results_{i}.jpg')
            im.save(byte_stream, format='PNG') #for byte stream
            byte_string = base64.b64encode(byte_stream.getvalue()).decode('utf-8')
            self.output.append(byte_string)
            self.outputfilenames.append(f'results_{i}.jpg')
            byte_stream.close()
        logging.info("Finished converting to byte strings")

    def destruct(self):
        self.delete_image_from_disk(self.filenames)
        self.delete_image_from_disk(self.outputfilenames)
        self.output = []
        self.outputfilenames =[]
        self.image_byte_strings=[]
        self.filenames =[]
        self.input_path=[]

