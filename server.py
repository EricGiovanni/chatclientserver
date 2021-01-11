import socket
import threading
import sys

class Server():
    ''' Constructor del servidor '''
    def __init__(self, host = 'localhost', port = 3000):
        #
        self.clients = []
        # Variable para almacenar el socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Iniciando servidor en el host y puerto que nos dieron en el constructor
        self.sock.bind((str(host), int(port)))
        # Esperamos un maximo de 10 conexiones
        self.sock.listen(10)
        # Quitamos bloqueo de sockets
        self.sock.setblocking(False)
        '''
        Iniciamos hilos para aceptar conexiones y procesar mensajes
        '''
        accept = threading.Thread(target = self.accept_connection)
        process = threading.Thread(target = self.process_connection)
        # Iniciamos hilo para aceptar conexiones
        accept.daemon = True
        accept.start()
        # Iniciamos hilo para procesar mensajes
        process.daemon = True
        process.start()
        # Hilo principal para recibir mensaje que nos permita salir del servidor
        while True:
            msg = input('->')
            if msg != 'exit':
                pass
            else:
                self.sock.close()
                sys.exit()

    '''
    Metodo para enviar mensajes a todos los usuarios
    conectados
    '''
    def msg_to_all(self, msg, client):
        for c in self.clients:
            try:
                if c != client:
                    c.send(msg)
            except:
                self.clients.remove(c)
    
    '''
    Metodo que acepta conexiones de nuevos usuarios
    '''
    def accept_connection(self):
        print('Aceptando conexiones...')
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clients.append(conn)
            except:
                pass

    '''
    Metodo para verificar si recibimos mensajes y enviarlos
    a todos los usuarios conectados
    '''
    def process_connection(self):
        print('Recibiendo mensajes')
        while True:
            if len(self.clients) > 0:
                for c in self.clients:
                    try:
                        data = c.recv(2048)
                        if data:
                            self.msg_to_all(data, c)
                    except:
                        pass

if __name__ == '__main__':
    server = Server()
