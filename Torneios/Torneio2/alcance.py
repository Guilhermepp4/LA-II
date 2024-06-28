"""
Uma cidade é representada por um mapa rectangular que é uma lista de strings. 
Cada caracter representa um bairro e em cada bairro apenas existe uma estrada 
de sentido único (representada pelos caracteres '>', '<', '^', ou 'v'), 
que dá acesso a um dos quatro bairros vizinhos, ou uma rotunda (caracter 'O') 
que dá acesso aos quatro bairros vizinhos. A cidade de facto é uma esfera, 
pelo que os bairros nos limites do mapa têm vizinhos nos bairros do lado oposto. 
Implemente uma função que dado um destes mapas e as coordenadas de um bairro,
determine a quantos bairros é possível chegar de carro a partir desse bairro.

    input: mapa = [">>v<<", , o = (0,0)
                   "^^O>>"]
    output: 8

    
    input: mapa = [">>v<<", , o = (0,0)
                   "^<<>^"]
    output: 6

"""

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

def make_graph(adj,mapa,lins,cols):

    for l in range(lins):
        for c in range(cols):
            
            if (l,c) not in adj:
                adj[(l,c)] = [] 
            
            if mapa[l][c] == ">":
                if c == cols-1:
                    adj[(l,c)].append((l,0))
                else:
                    adj[(l,c)].append((l,c+1))
              
            
            if mapa[l][c] == "<":
                if c == 0:
                    adj[(l,c)].append((l,cols-1))
                else:
                    adj[(l,c)].append((l, c-1))
            
            if mapa[l][c] == "^":
                if l == 0:
                    adj[(l,c)].append((lins-1,c))
                else:
                    adj[(l,c)].append((l-1,c))
            
            if mapa[l][c] == "v":
                if l == lins-1:
                    adj[(l,c)].append((0,c))
                else:
                    adj[(l,c)].append((l+1,c))   
            
            if mapa[l][c] == "O":
                if c == cols-1:
                    adj[(l,c)].append((l,0))
                else:
                    adj[(l,c)].append((l,c+1))
    
                if c == 0:
                    adj[(l,c)].append((l,cols-1))
                else:
                    adj[(l,c)].append((l,c-1))
                    
                if l == 0:
                    adj[(l,c)].append((lins-1,c))
                else:
                    adj[(l,c)].append((l-1,c))
                    
                if l == lins-1:
                    adj[(l,c)].append((0,c))
                else:
                    adj[(l,c)].append((l+1,c))     
                
    return adj

def alcance(mapa, o):  
     
    adj = {}
    lins = len(mapa)
    cols = len(mapa[0])
    
    adj=make_graph(adj,mapa,lins,cols)
    
    resp = bfs(adj,o)
    
    return len(resp)

#40%