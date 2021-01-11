import socket
import threading
import sys

''' Clase del cliente '''
class Client():
    ''' Constructor '''
    def __init__(self, host = 'localhost', port = 3000):
        # Variable para almacenar el socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Nos conectamos al servidor
        self.sock.connect(str(host), int(port))
        '''
        Iniciamos hilo para esperar mensajes y si recibimos uno,
        guardarlo en una variable
        '''
        msg_recv = threading.Thread(target = self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('->')
            if msg != 'exit':
                self.send_msg(msg)
            else:
                self.sock.close()
                sys.exit(-1)

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(2048)
                if data:
                    print(data.decode('utf-8'))
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(data.encode('utf-8'))


if __init__ == '__main__':
    c = Client()


