from PIL import Image
from ultralytics import YOLO
import io

model = YOLO('best (1).pt')
input_image_paths = ['./test_image.jpg']

def decode_image(byte_array):
    input_images=[]
    for i in byte_array:
        decoded_byte_string = base64.b64decode(i)
        byte_stream = io.BytesIO(decoded_byte_string)
        image = Image.open(byte_stream)
        input_images.append(image)
    return input_images


def get_output(byte_array):
    input_images = decode_image(byte_array)
    byte_stream = io.BytesIO()
    results_list = model.predict(input_images)
    output = []
    for i, results in enumerate(results_list):
        im_array = results.plot()
        im = Image.fromarray(im_array)
        im.save(byte_stream, format='PNG') #for byte stream
        byte_string = base64.b64encode(byte_stream.getvalue()).decode('utf-8')
        output.append(byte_string)
        print(byte_string)
        #im.show()
        im.save(f'results_{i}.jpg')
    return output
