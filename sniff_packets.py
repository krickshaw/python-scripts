from scapy.all import sniff
from scapy.all import get_if_list

# Callback para procesar los paquetes capturados
def packet_callback(packet):
    print(f"Paquete capturado: {packet.summary()}")

def start_sniffer(interface):
    print(f"Capturando paquetes en la interfaz {interface}...")
    # Captura paquetes en la interfaz especificada
    sniff(iface=interface, prn=packet_callback, count=10)

# Lista las interfaces disponibles
def list_interfaces():
    interfaces = get_if_list()
    print("Interfaces disponibles:")
    for iface in interfaces:
        print(iface)
        #start_sniffer(iface)

if __name__ == "__main__":
    # Especifica la interfaz de red a escuchar (por ejemplo, 'eth0', 'wlan0', etc.)
    interface = 'Wi-Fi' 

    start_sniffer(interface)

    list_interfaces()
