#!/usr/bin/env python3
from exif import Image as ExifImage
#from PIL import Image as PillowImage
#from PIL import ExifTags
import os
#lista imagenes en lista images
images = os.listdir('imagenes')
# List Your Images
#images = ["SAM_2894.JPG", "SAM_2904.JPG", "SAM_2905.JPG"]
# EXIF Tags para comprobacion
EXIF_TAGS = [
    "artist",
    "datetime_original",
    "copyright",
]
# editar metadatos en el exif
print("EXIF\n======")
for img in images:
    # raiz de imagenes
    image_path = "imagenes/{}".format(img)

    # abre imagen y lee datos exif
    with open(image_path, "rb") as input_file:
        exif_img = ExifImage(input_file)
    
    # mete datos artista (ejemplo)
    exif_img.artist = "marco"

    # inserta datos de fecha y copyright
    exif_img.datetime_original = "2018:01:29 22:50:55"
    exif_img.copyright = "Copyright 2018"
    #path para guardar imagenes
    output_filepath = img

    # guarda imagenes en el disco duro
    with open(output_filepath, "wb") as ofile:
        ofile.write(exif_img.get_file())

    # check para ver datos ya modificados
    print(img)
    #abre archivos con exif
    with open(output_filepath, "rb") as confirmation:
        exif_img = ExifImage(confirmation)
    
    for tag in EXIF_TAGS:
        # extrae valores exif para visualizar
        value = exif_img.get(tag)
        # imprime tags extraidos para muestreo
        print("{}: {}".format(tag, value))
    print("\n")