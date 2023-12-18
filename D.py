#Endre størrelsen/oppløsningen på bildet (resize), slik at enten bredden har minimum 1080 piksler. Les mer om kravene Instagram stiller til oppløsning på bilder her: https://help.instagram.com/1631821640426723 
from PIL import Image
import pilgram

def resize_image(input_path, output_path, new_size=(1080, 1080)):
    with Image.open(input_path) as img:
        resized_img = img.resize(new_size)

        resized_img.save('sample-resize.jpg')

resize_image('sample.jpg', 'sample-resize.jpg')





