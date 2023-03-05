#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 1 - ticker_server.py
Grupo:
Números de aluno:
"""

# Zona para fazer importação
import sock_utils as su
import sys, socket as s
###############################################################################

class resource:
    def __init__(self, resource_id):
        su.create_tcp_server_socket(self.address, self.port);
        self.resource_id=resource_id
        pass # Remover esta linha e fazer implementação da função

        def subscribe(self, client_id, time_limit):
            self.client_id=client_id
            
        pass # Remover esta linha e fazer implementação da função

        def unsubscribe (self, client_id):
        pass # Remover esta linha e fazer implementação da função

        def status(self, client_id):
        pass # Remover esta linha e fazer implementação da função

        def __repr__(self):
            output = ""
            # R <resource_id> <list of subscribers>

            return output


        ###############################################################################

class resource_pool:
    subs = {}
    cmds = {'SUBSCR': subscribe,
            'CANCEL':unsubscribe,
            'STATUS':status ,
            'INFOS': infos ,
            'STATIS': statis }
    
    def __init__(self, N, K, M):
        self.N = N
        self.K = K
        self.M = M
    pass # Remover esta linha e fazer implementação da função

    def clear_expired_subs(self):
        subs = {}
    pass # Remover esta linha e fazer implementação da função

    def subscribe(self, resource_id, client_id, time_limit):
        if :
             subs.update({resource_id:client_id})
            return 'OK'
        elif:
            return 'NOK'
        else:
            return 'UNKNOWN RESOURCE'
            
       
    pass # Remover esta linha e fazer implementação da função

    def unsubscribe (self, resource_id, client_id):
       if :
             subs.pop({resource_id:client_id})
            return 'OK'
        elif:
            return 'NOK'
        else:
            return 'UNKNOWN RESOURCE'
    pass # Remover esta linha e fazer implementação da função

    def status(self, resource_id, client_id):
         if :
             subs.pop({resource_id:client_id})
            return 'SUBSCRIBED'
        elif:
            return 'UNSUBSCRIBED'
        else:
            return 'UNKNOWN RESOURCE'
    pass # Remover esta linha e fazer implementação da função

    def infos(self, option, client_id):
        if option=="M":
            return #lista de elementos subscritos
        elif option=="K":
            return #<número de ações que cli-ente ainda pode subscre-ver>
    pass # Remover esta linha e fazer implementação da função

    def statis(self, option, resource_id):
        if option=="L":
            if resource_id not in subs:
                return 'UNKNOWN RESOURCE'
        elif option=="ALL":
            return #numero coisas
    pass # Remover esta linha e fazer implementação da função

    def __repr__(self):
    output = ""
    
    
    def process(line):
        cmd, *args = line.split()
    return cmds[cmd](*args)

process(msg)


    # Acrescentar no output uma linha por cada recurso
    return output


###############################################################################

# código do programa principal
