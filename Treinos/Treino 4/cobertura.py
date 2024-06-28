'''

Implemente uma função que calcula o número mínimo de nós de um grafo 
não orientado que cobrem todas as arestas, ou seja, o tamanho do menor 
conjunto de nós que contém pelo menos um extremo de cada aresta. 
A função recebe a lista de todas as arestas do grafo, sendo cada aresta um 
par de nós.

'''

def cobertura(arestas):

    cobertura_nos = set()
    
   
    arestas_restantes = arestas[:]
    
    while arestas_restantes:

        incidencia = {}
        for u, v in arestas_restantes:
            if u in incidencia:
                incidencia[u] += 1
            else:
                incidencia[u] = 1
            if v in incidencia:
                incidencia[v] += 1
            else:
                incidencia[v] = 1

  
        max_n = max(incidencia, key=incidencia.get)

 
        cobertura_nos.add(max_n)

       
        arestas_restantes = [(u, v) for u, v in arestas_restantes if u != max_n and v != max_n]
    
    return len(cobertura_nos)

#100%