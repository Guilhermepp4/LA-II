'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

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
    return dist

def travessia(mapa):
    
    lins = len(mapa)
    cols = len(mapa[0])
    h = 0

    adj = {}

    for l in range(lins):
        for c in range(cols):

            if (l,c) not in adj:
                adj[(l,c)] = {}

            if l > 0 and abs(int(mapa[l][c]) - int(mapa[l-1][c])) <=2:
                
                if (l - 1,c) not in adj:
                    adj[(l - 1,c)] = {}

                adj[(l,c)].update({(l - 1,c) : abs(int(mapa[l][c]) - int(mapa[l-1][c])) + 1})
                adj[(l - 1,c)].update({(l,c) : abs(int(mapa[l][c]) - int(mapa[l-1][c])) + 1})


            if c > 0 and abs(int(mapa[l][c]) - int(mapa[l][c - 1])) <=2:
                
                if (l,c - 1) not in adj:
                    adj[(l,c - 1)] = {}

                adj[(l,c)].update({(l,c - 1) : abs(int(mapa[l][c]) - int(mapa[l][c - 1])) + 1})
                adj[(l,c - 1)].update({(l,c) : abs(int(mapa[l][c]) - int(mapa[l][c - 1])) + 1})

    start_positions = []
    finish_line = []

    for c in range(cols):
        start_positions.append((0,c))

    for c in range(cols):
        finish_line.append((lins - 1,c))

    min = lins * cols * 2

    

    for d in start_positions:
        if d in adj:
            dist = dijkstra(adj,d)

            for f in finish_line:
                if f in dist:
                    if dist[f] < min:
                        min = dist[f]
                        h = d[1]

    return (h,min)


#100%