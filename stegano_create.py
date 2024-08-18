from stegano import lsb

# Especifica el path de la imagen original y la imagen de salida
original_image_path = "C:\\Users\\Juan\\Downloads\\monalisa.png"
output_image_path = "C:\\Users\\Juan\\Downloads\\monalisa_steg.png"

# Especifica el mensaje que deseas ocultar
secret_message = "Hello world"

# Oculta el mensaje en la imagen usando LSB
lsb.hide(original_image_path, message=secret_message).save(output_image_path)

print(f"Mensaje oculto guardado en {output_image_path}")