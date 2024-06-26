'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''
def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return pai

def translate_route(d, pai, inst):

    if pai == (d[0] - 1,d[1]):
        inst.append("S")
    
    if pai == (d[0] + 1,d[1]):
        inst.append("N")
    
    if pai == (d[0],d[1] - 1):
        inst.append("E")
    
    if pai == (d[0],d[1] + 1):
        inst.append("O")

    return inst

def make_graph(map_graph, mapa, lins, cols):
    
    for l in range(lins):
        for c in range(cols):

            if (l,c) not in map_graph:
                map_graph[(l,c)] = {}

            if l > 0:
                if (l-1,c) not in map_graph:
                    map_graph[(l-1,c)] = {}

                if  mapa[l][c] == ' ' and  mapa[l-1][c] == ' ':
                    map_graph[(l,c)].update({(l-1,c) : 1})
                    map_graph[(l-1,c)].update({(l,c) : 1})

            if c > 0:
                if (l,c - 1) not in map_graph:
                    map_graph[(l,c - 1)] = {}

                if  mapa[l][c] == ' ' and  mapa[l][c - 1] == ' ':
                    map_graph[(l,c)].update({(l,c - 1) : 1})
                    map_graph[(l,c - 1)].update({(l,c) : 1})
    return map_graph

def caminho(mapa):

    map_graph = {}
    lins = len(mapa)
    cols = len(mapa[0])
    inst=[]

    d = (lins - 1 ,cols - 1)

    make_graph(map_graph, mapa, lins, cols)

    pai = (dijkstra(map_graph, (0,0)))

    while d != (0,0):
        translate_route(d, pai[d], inst)
        d = pai[d]

    inst.reverse()
    inst = "".join(inst)

    return inst

#100%