import os
from PIL import Image
from io import BytesIO, StringIO
import base64


class CustomImage:
    def __init__(self, source_image, image_name):
        # self.image = Image.open(path)
        self.image_name = image_name

        self.image = Image.open(BytesIO(source_image))
        self.width, self.height = self.image.size


    def reduce_image(self, size=0.5, new_quality=75):
        iname, iext = os.path.splitext(self.image_name)
        new_width = round(self.width * size)
        new_height = round(self.height * size)
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

        saveExtension = {".jpeg": "JPEG", ".jpg": "JPEG", ".png": "PNG", ".gif": "GIF"}
        
        with BytesIO() as output:
            self.image.save(output, saveExtension[iext], quality=new_quality)
            contents = { "img": base64.b64encode(output.getvalue()), "image_filename": "Reduced_" + self.image_name }
        
        return contents
