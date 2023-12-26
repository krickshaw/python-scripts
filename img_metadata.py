import exifread

def obtener_metadatos(archivo):
    # Abre el archivo en modo binario
    with open(archivo, 'rb') as f:
        # Lee los metadatos usando exifread
        tags = exifread.process_file(f)

        # Imprime los metadatos
        for tag, valor in tags.items():
            print(f'{tag}: {valor}')

if __name__ == "__main__":
    # Archivo de imagen
    imagen = '/home/kali/Desktop/Python/Panasonic1.jpg'
    
    obtener_metadatos(imagen)
