"""
Numa aldeia todas as pessoas tem um nome próprio e dois apelidos diferentes. 
Implemente uma função que dado o conjunto de pessoas que vivem na aldeia e o 
nome de uma delas, determine qual o nome do parente mais afastado.
Se houver mais do que um parente igualmente mais afastado, deve ser devolvido o que 
tiver o nome mais pequeno em ordem lexicográfica.
Duas pessoas são parentes diretos se partilharem algum apelido. Se partilharem
os dois apelidos são parentes de primeiro grau. Se partilharem apenas um apelido
são parentes de segundo grau.


    input: aldeia = ["Ana Silva Costa","Alberto Costa Pereira","Eva Silva Costa","Rui Pereira Barros"], p = "Ana Silva Costa"
    output: "Rui Pereira Barros"

    input: aldeia = ["Ana Silva Costa","Alberto Costa Pereira","Eva Silva Costa","Rui Moreira Barros"], p = "Ana Silva Costa"
    output: "Alberto Costa Pereira"

"""

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

def diretos(adj, pessoas):
    
    for i in range(len(pessoas)-1):
        a,b,c = pessoas[i].split()
        
        for pessoa in pessoas:
            
            nomes = pessoa.split()
            
            if pessoa not in adj:
                adj[pessoa]={}
                
            if pessoas[i] not in adj:
                adj[pessoas[i]]= {}
            
            if b in nomes and c in nomes and a not in nomes:
                adj[pessoas[i]].update({pessoa:0})
                adj[pessoa].update({pessoas[i]:0})
            
    return adj

def indiretos(adj,pessoas):
    
    for i in range(len(pessoas)-1):
        a,b,c = pessoas[i].split()
        
        for pessoa in pessoas:
            
            nomes = pessoa.split()
            
            if pessoa not in adj:
                adj[pessoa]={}
                
            if pessoas[i] not in adj:
                adj[pessoas[i]]= {}
            
            if (b in nomes or c in nomes) and not (b in nomes and c in nomes):
                adj[pessoas[i]].update({pessoa:2})
                adj[pessoa].update({pessoas[i]:2})
    
    return adj

def parente(pessoas,p):
    
    if len(pessoas) == 1:
        return p
    
    adj={}
    lista_nomes = []
    
    adj=diretos(adj,pessoas)
    adj=indiretos(adj,pessoas)
    
    dist = dijkstra(adj,p)
    print (dist)
    
    for nome in dist:
        lista_nomes.append(nome)
    
    lista_nomes.sort()
    lista_nomes.sort(key = lambda t : dist[t], reverse = True)
    
    return lista_nomes[0]

#100%