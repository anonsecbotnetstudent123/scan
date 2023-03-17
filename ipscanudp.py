import socket
import random

def portscanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)
    sock.sendto(b'\x00\x01\x00\x00\x00\x01\x00\x00stats items\r\n', (ip, port))
    try:
        response, address = sock.recvfrom(1024)
        if response:
            with open("success.txt", "a") as f:
                f.write(f"{ip}:{port}\n")
    except:
        pass
    sock.close()

while True:
    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    port = 11211
    portscanner(ip, port)