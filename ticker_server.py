class resource:
    def __init__(self, resource_id):
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


        

class resource_pool:
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
    pass # Remover esta linha e fazer implementação da função

    def subscribe(self, resource_id, client_id, time_limit):
    pass # Remover esta linha e fazer implementação da função

    def unsubscribe (self, resource_id, client_id):
    pass # Remover esta linha e fazer implementação da função

    def status(self, resource_id, client_id):
    pass # Remover esta linha e fazer implementação da função

    def infos(self, option, client_id):
    pass # Remover esta linha e fazer implementação da função

    def statis(self, option, resource_id):
    pass # Remover esta linha e fazer implementação da função

    def __repr__(self):
    output = ""
    
    
    def process(line):
        cmd, *args = line.split()
    return cmds[cmd](*args)

process(msg)


    # Acrescentar no output uma linha por cada recurso
    return output
