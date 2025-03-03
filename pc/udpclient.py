"""
    Copyright (C) 2017 - 2021  Zhengyu Peng, https://zpeng.me

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    ----------

    `                      `
    -:.                  -#:
    -//:.              -###:
    -////:.          -#####:
    -/:.://:.      -###++##:
    ..   `://:-  -###+. :##:
           `:/+####+.   :##:
    .::::::::/+###.     :##:
    .////-----+##:    `:###:
     `-//:.   :##:  `:###/.
       `-//:. :##:`:###/.
         `-//:+######/.
           `-/+####/.
             `+##+.
              :##:
              :##:
              :##:
              :##:
              :##:
               .+:

"""

import socket
from PySide6.QtCore import QObject, Signal

class UDPClient(QObject):
    STOP = 0
    CONNECTED = 1

    status = Signal(int, str)  # Signal to emit status updates
    message = Signal(str, str)  # Signal to emit received messages

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = None
        self.running = False

    def start(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setblocking(False)
            self.running = True
            self.status.emit(self.CONNECTED, f"{self.host}:{self.port}")
        except Exception as e:
            self.status.emit(self.STOP, str(e))

    def send(self, message):
        if self.sock:
            try:
                self.sock.sendto(message.encode(), (self.host, self.port))
                self.message.emit("UDP Client", f"Sent: {message}")
            except Exception as e:
                self.message.emit("UDP Client", f"Error: {str(e)}")
                
    def listen_for_messages(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)  # Buffer size is 1024 bytes
                if data:
                    self.message.emit("UDP Server", f"Received: {data.decode()}")
            except BlockingIOError:
                # No data available, continue listening
                pass
            except Exception as e:
                self.message.emit("UDP Client", f"Error: {str(e)}")
                self.running = False

    def close(self):
        self.running = False
        if self.sock:
            self.sock.close()
            self.sock = None
        self.status.emit(self.STOP, "Disconnected")