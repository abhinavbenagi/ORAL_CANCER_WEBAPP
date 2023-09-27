#

from PIL import Image
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('best (1).pt')

# Create a list of paths to the input images
#input_image_paths = ['17 (3) - Copy.jpg','17 (2).jpg']
input_image_paths = ['image1.jpg','image2.jgp']

# Predict for all input images in a single batch
results_list = model.predict(input_image_paths)
# Process the results list for each image
for i, results in enumerate(results_list):
    im_array = results.plot()
    im = Image.fromarray(im_array)
    im.show()
    im.save(f'results_{i}.jpg')  # Save each image with a unique filename
