import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        print(f"Escaneando puerto {port}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Tiempo de espera para la conexión
        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

if __name__ == "__main__":
    # Configuración del host y los puertos a escanear
    host = 'localhost'
    ports = range(1, 5)  # Escanea puertos

    print(f"Escaneando puertos en {host}...")
    open_ports = scan_ports(host, ports)

    if open_ports:
        print("Puertos abiertos:")
        for port in open_ports:
            print(f"Puerto {port}")
    else:
        print("No se encontraron puertos abiertos.")
