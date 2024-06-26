'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.

'''

def complete(tamanho, c):
    return len(c) == tamanho

def extensions(c, conhecidos):
    if not c:
        return conhecidos
    l = []
    for conhecido in filter(lambda x: x > c[-1], conhecidos):
        flag = True
        for x in c:
            if conhecido not in conhecidos[x]:
                flag = False
                break
        if flag:
            l.append(conhecido)
    
    return l

def valid():
    return True

def aux(c, conhecidos, tamanho):
    if complete(tamanho, c):
        return valid()
    for x in extensions(c, conhecidos):
        c.append(x)
        if aux(c, conhecidos, tamanho):
            return True
        c.pop()
    
    return False


def amigos(conhecidos):
    if not conhecidos:
        return 0
    adj = {}
    for (x,y) in conhecidos:
        if x not in adj:
            adj[x] = set()
        adj[x].add(y)
        if y not in adj:
            adj[y] = set()
        adj[y].add(x)
        
    c = []
    for i in range(len(adj), 0, -1): 
        if aux(c, adj, i):
            return i
        
#100%