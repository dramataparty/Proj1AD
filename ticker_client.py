#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 1 - ticker_client.py
Grupo:52
Números de aluno: 56931,
"""
# Zona para fazer imports

import sock_utils as su
import sys, socket as s
# Programa principal

def send_receive(self, data):
    while True:
        msg = str(input('comando >'));
        s.sendall(msg.encode('utf-8'))
        resposta = s.recv(1024)
        print("resposta: " + resposta.decode())
        if msg == 'EXIT':
            break
    