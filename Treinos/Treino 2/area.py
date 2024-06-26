'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return vis

def area(p,mapa):

    adj = {}
    lado = len(mapa)
    x = p[0]
    y = p[1]

    for lin in range(lado):
        for col in range(lado):
            
            if (lin,col) not in adj and mapa[lin][col] != "*":
                adj[(lin,col)] = []

            if mapa[lin][col] != "*":
                if col - 1 >= 0 and mapa[lin][col - 1] != "*" :
                    adj[(lin,col)].append((lin, col - 1))

                if lin - 1 >= 0 and mapa[lin - 1][col] != "*":
                    adj[(lin,col)].append((lin - 1, col))

                if col + 1 < lado and mapa[lin][col + 1] != "*":
                    adj[(lin,col)].append((lin, col + 1))

                if lin + 1 < lado and mapa[lin + 1][col] != "*":
                    adj[(lin,col)].append((lin + 1, col))

    resp = len(bfs(adj, p))
    return resp

#80%