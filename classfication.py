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
        self.output_dir = "uploads/generated/"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs("uploads/original/", exist_ok=True)
        self.outputfilenames =[] #path where the model has saved the images
        self.input_path=[] #complete path where input images are saved
        logging.info("Classification class initialization successful")

    
    def caller_function(self,user_images):
        logging.info("caller function initiated")
        result_id=[]
        for i in user_images:
            result_id.append(i[0])
            self.input_path.append(i[1])

        results_list = self.model.predict(self.input_path)
        logging.info("Finished model prediction")

        for i, results in enumerate(results_list):
            im_array = results.plot()
            im = Image.fromarray(im_array)
            im.save(f'uploads/generated/{result_id[i]}.jpg')
            self.outputfilenames.append([
                result_id[i], f'uploads/generated/{result_id[i]}.jpg'
            ])
            
        logging.info("Finished Model Process")
        return self.outputfilenames

