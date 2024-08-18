import email
from email import policy
from email.parser import BytesParser

def parse_email_headers(file_path):
    with open(file_path, 'rb') as file:
        msg = BytesParser(policy=policy.default).parse(file)
    headers = dict(msg.items())
    return headers

# Especifica el path del archivo de correo
email_file_path = "C:\\Users\\Juan\\Downloads\\sample_email3.eml"

# Analiza las cabeceras del correo
headers = parse_email_headers(email_file_path)

# Muestra las cabeceras
for key, value in headers.items():
    print(f"{key}: {value}")
