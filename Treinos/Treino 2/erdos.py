'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
                       "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
    2
                       
['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek']

'''

def bfs(adj):
    erdos = {"Paul Erdos": 0}
    queue = ["Paul Erdos"]
    while queue:
        v = queue.pop(0)
        for d in adj:
            if v in adj[d]:
                for autor in adj[d]:
                    if autor not in erdos:
                        erdos[autor] = erdos[v] + 1
                        queue.append(autor)
    return erdos

def erdos(artigos,n):
    
    erdos = bfs(artigos)
    
    lista_erdos = []
    resp = []

    for autor in erdos:
        if erdos[autor] <= n:
            lista_erdos.append((autor, erdos[autor]))

    lista_erdos.sort(key = lambda t: t[0])
    lista_erdos.sort(key = lambda t: t[1])

    for par in lista_erdos:
        resp.append(par[0])

    return resp

#100%