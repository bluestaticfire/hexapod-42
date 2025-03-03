import socket

def udp_server(ip: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"UDP Server listening on {ip}:{port}")

    try:
        while True:
            # Receive data from the client
            data, addr = sock.recvfrom(1024)  
            print(f"Received message from {addr}: {data.decode()}")
            # Send a response back to the client
            response = f"ACK: {data.decode()}"
            sock.sendto(response.encode(), addr)
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_server("0.0.0.0", 12345)  
    