'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.



[["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
            (maior(vizinhos), 6)

'''

def dfs(adj,o):
    return dfs_aux(adj,o,set(),{})

def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return vis

def maior(vizinhos):
    
    def make_grafo(vizinhos, grafo):
        for fronteiras in vizinhos:
            lista_aux = []
            for pais in fronteiras:
                if pais not in grafo:
                    grafo[pais] = []
                
                lista_aux.append(pais)
                if pais not in paises:
                    paises.append(pais)
            for pais in fronteiras:
                for i in range(len(lista_aux)):
                    if lista_aux[i] != pais:
                        grafo[pais].append(lista_aux[i])
                
    grafo={}   
    paises=[]
    maior = 0
    make_grafo(vizinhos, grafo)
    
    for pais in paises:
        resp = (len(dfs(grafo,pais)))
        if resp > maior:
            maior = resp
    
    return maior

#100%