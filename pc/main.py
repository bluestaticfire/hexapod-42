import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread
from udpclient import UDPClient

class MainApp:
    def __init__(self):
        # Create the UDP client
        self.udp_client = UDPClient("192.168.4.1", 1234) 

        self.udp_thread = QThread()
        self.udp_client.moveToThread(self.udp_thread)

        # Connect signals
        self.udp_client.status.connect(self.on_status_update)
        self.udp_client.message.connect(self.on_message_received)

        # Start the thread and the UDP client
        self.udp_thread.started.connect(self.udp_client.start)
        self.udp_thread.start()

        # Send a test message
        self.udp_client.send("Hello, Server!")

    def on_status_update(self, status, message):
        print(f"Status: {status}, Message: {message}")

    def on_message_received(self, source, message):
        print(f"Received from {source}: {message}")

    def close(self):
        # Clean up
        self.udp_client.close()
        self.udp_thread.quit()
        self.udp_thread.wait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()

    # Simulate running the application
    sys.exit(app.exec())