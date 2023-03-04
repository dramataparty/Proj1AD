"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo:
Números de aluno:
"""

# zona para fazer importação

import sock_utils
import sys, socket as s

# definição da classe server_connection 



class server_connection:
    conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    def __init__(self, address, port):
        
        if len(sys.argv) > 1:
            self.address = address
            self.port = port   
        else:
            self.address = '127.0.0.1'
            self.port = 9999
                
    pass # Remover esta linha e fazer implementação da função
    

    def connect(self):
        conn_sock.connect((self.address, self.port))
        while True:
            msg = str(input('comando >'));
            if msg == 'EXIT':
                break
    pass # Remover esta linha e fazer implementação da função

    def send_receive(self, data):
        conn_sock.sendall(msg.encode('utf-8'))
        resposta = conn_sock.recv(1024)
        print("resposta: " + resposta.decode())
    pass # Remover esta linha e fazer implementação da função

    def close(self):
        conn_sock.close()    
    pass # Remover esta linha e fazer implementação da função



