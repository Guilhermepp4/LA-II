'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

                    [["Porto",20,"Lisboa"],
                    ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
                    ["Braga",3,"Famalicao",3,"Porto"],
                    ["Viana",4,"Povoa",3,"Porto"],
                    ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]]
                    
                    ("Caminha","Lisboa"),30

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

def viagem(rotas,o,d):
    
    if o == d:
        return 0
    
    adj = {}

    for rota in rotas:
        i=0
        while (i < (len(rota)-2)):

            if rota[i] not in adj:
                adj[rota[i]] = {}
            
            if rota[i+2] not in adj:
                adj[rota[i+2]] = {}

            adj[rota[i]].update({rota[i+2]: rota[i+1]})
            adj[rota[i+2]].update({rota[i]: rota[i+1]})

            i+=2

    pai = dijkstra(adj, o)
    soma = 0

    while d != o:
        soma += adj[d][pai[d]]
        d = pai[d]
    
    return soma

#100%