import sys, socket as s
import sock_utils
class server_connection:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        
    pass # Remover esta linha e fazer implementação da função

    def connect(self):
    pass # Remover esta linha e fazer implementação da função

    def send_receive(self, data):
    pass # Remover esta linha e fazer implementação da função

    def close(self):
    pass # Remover esta linha e fazer implementação da função



if len(sys.argv) > 1:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    HOST = '127.0.0.1'
    PORT = 9999
while True:
    msg = str(input('comando >'));
    if msg == 'EXIT':
        break
    
    

    conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    conn_sock.connect((HOST, PORT))
    conn_sock.sendall(msg.encode('utf-8'))
    resposta = conn_sock.recv(1024)
    print("resposta: " + resposta.decode())


    
conn_sock.close()