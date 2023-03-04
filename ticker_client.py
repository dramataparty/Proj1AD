#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 1 - ticker_client.py
Grupo:52
Números de aluno: 56931, 56922
"""
# imports

import sock_utils as su
import sys, socket as s

# Programa principal

def send_receive(self, data):
    while True:
        msg = str(input('comando >'));
        #validar o comando fornecido
        
        local_commands = []
        serv_commands = []

        if msg == 'EXIT':
            break

        elif msg in local_commands:
            #processar
        
        elif msg in serv_commands:
            conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            conn_sock.connect((HOST, PORT))
            
            conn_sock.sendall(msg.encode('utf-8'))
            resposta = conn_sock.recv(1024)
            print("resposta: " + resposta.decode())
            conn_sock.close()

        #caso faltem argumentos
            print("MISSING-ARGUMENTS")

        else:
            print("UNKNOWN-COMMAND")

        

        #parâmetros linha de comandos
