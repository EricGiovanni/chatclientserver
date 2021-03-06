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
        self.sock.connect((str(host), int(port)))
        '''
        Iniciamos hilo para esperar mensajes y si recibimos uno,
        guardarlo en una variable y mostrarlo al cliente
        '''
        msg_recv = threading.Thread(target = self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()
        '''
        Hilo principal que espera el mensaje que quieres enviar
        y luego los manda a todos los usuarios
        '''
        while True:
            msg = input('->')
            if msg != 'exit':
                self.send_msg(msg)
            else:
                self.sock.close()
                sys.exit()

    '''
    Metodo que espera mensajes del servidor 
    y los imprime
    '''
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(2048)
                if data:
                    print(data.decode('utf-8'))
            except:
                pass
    '''
    Metodo que manda mensajes al servidor
    '''
    def send_msg(self, msg):
        self.sock.send(msg.encode('utf-8'))


if __name__ == '__main__':
    client = Client()


