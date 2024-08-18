from stegano import lsb

# Especifica el path de la imagen
image_path = "C:\\Users\\Juan\\Downloads\\monalisa_steg.png"

# Extrae el mensaje oculto usando LSB
hidden_message = lsb.reveal(image_path)

if hidden_message:
    print("Mensaje oculto encontrado:")
    print(hidden_message)
else:
    print("No se encontró ningún mensaje oculto en la imagen.")
