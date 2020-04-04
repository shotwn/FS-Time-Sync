import socket
import threading
import sys


class SingleInstance:
    def __init__(self, port):
        self.triggers = []

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(('localhost', port))
            self.socket.listen(5)
        except OSError:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('localhost', port))
            self.socket.sendall(b'SingleInstance')
            print("An instance of the program already working.")
            sys.exit(0)

        self.listen_thread = threading.Thread(None, self.socket_listener, "Single Instance Thread", daemon=True)
        self.listen_thread.start()

    def socket_listener(self):
        while True:
            connection, client_address = self.socket.accept()

            data = connection.recv(1024)
            if data == b'SingleInstance':
                self._trigger()

    def _trigger(self):
        for trigger in self.triggers:
            trigger()

    def add_trigger(self, callable):
        self.triggers.append(callable)
