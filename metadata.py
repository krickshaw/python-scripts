from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        exif[tag_name] = value
    return exif

image_path = "C:\\Users\\Juan\\Downloads\\Photo1.jpg"
exif_data = get_exif_data(image_path)
for key, value in exif_data.items():
    print(f"{key}: {value}")
