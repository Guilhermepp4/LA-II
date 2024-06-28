"""

Implemente uma função que dado um mapa rectangular em que para cada posição
é indicada a respectiva altura, calcule o maior caminho que é possível
fazer nesse mapa. Assuma que apenas é possível andar para a direita ou
para baixo e apenas se a diferença de alturas for exactamente 1.

Sugere-se que começe por definir uma função que calcula qual o maior caminho
que acaba numa determinada posição.

input: mapa = [[7,5,2,3,1],
               [3,4,1,4,4],
               [1,5,6,7,8],
               [3,4,5,8,9],
               [3,2,2,7,6]]    
output: 8

input: mapa = [[1,2,4],
              [3,1,5],
              [1,5,2]]
                    
output: 3
"""

def aux(mapa, nemo,x, y, borderx, bordery):
    
    if x+1 >= borderx and y+1 >= bordery:
        return 0
    
    if (x,y) in nemo:
        return nemo[(x,y)]
        
    b = 0
    d = 0
    
    if y+1 < bordery:
        if abs(mapa[x][y+1] - mapa[x][y]) == 1:
            b = 1 + aux(mapa, nemo, x, y+1, borderx, bordery)
    if x+1 < borderx:
        if abs(mapa[x+1][y] - mapa[x][y]) == 1:
            d = 1 + aux(mapa, nemo, x+1, y, borderx, bordery)
        
    nemo[(x,y)] = max(b,d)
    return nemo[(x,y)] 

def caminho(mapa):
    
    
    borderx = len(mapa)
    bordery = len(mapa[0])
    resp = []
    nemo = {}
    
    for i in range(borderx):
        for j in range(bordery):
            resp.append(aux(mapa, nemo, i, j, borderx, bordery))
    print(nemo)
    return max(resp) +1

#80%