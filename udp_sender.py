import socket

esp32_ip = "192.168.4.1"  # Replace with your ESP32's IP address
udp_port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Implement controls here, whether as a GUI or console based!
message = "walk180".encode()  # Message to send
sock.sendto(message, (esp32_ip, udp_port))
print(f"Sent: {message.decode()} to {esp32_ip}:{udp_port}")

sock.close()

