"""

Implemente uma função que dado um mapa quadrado repreentado com uma lista de
strings, devolva as coordenadas onde se encontra o tesouro mais central. Um
tesouro é marcado com um 'X'. Caso haja mais do que um tesouro à mesma
distância do centro devolva o que tiver a menor coordenada horizontal e, caso
esta seja idêntica, o que tiver a menor coordenada vertical.

    input: mapa = ["   ",
                   " X ",
                   "  X"]
    output: (1,1)
    
    input: mapa = ["  X",
                   "   ",
                   "  X"]
    output: (2,0)
"""

def tesouro(mapa):
    
    def distancia(cor,tamanho):
        if tamanho%2==0:
            meio = [[tamanho//2, tamanho//2],[tamanho//2,(tamanho//2)-1],[(tamanho//2)-1,tamanho//2],[(tamanho//2)-1,(tamanho//2)-1]]
        else:
            meio = [tamanho//2, tamanho//2]
        dist = 0
        lista=[0,0]
        
  
        lista[0] = cor[0]
        lista[1] = cor[1]
            
        while(lista[0],lista[1]) in meio:
              
            if lista[0] > meio:
                lista[0] -= 1
                dist += 1
            elif lista[0] < meio:
                lista[0] += 1
                dist += 1
                
            if lista[1] > meio:
                lista[1] -=1
                dist += 1
            elif lista[1] < meio:
                lista[1] += 1
                dist += 1
        
        
        return dist
    
    tamanho = len(mapa)
    lista_cor = []
    
    dis = {}
    for x in range(tamanho):
        for y in range(tamanho):
            if mapa[x][y] == "X":
                lista_cor.append((x,y))
    
    
    for cor in lista_cor:
        dis[cor] = distancia(cor,tamanho)
            
                
    dis = list(dis.items())
    print(dis)
    dis.sort(key=lambda item: item[0][1])
    dis.sort(key=lambda item: item[0][0])
    dis.sort(key=lambda item: item[1])

    return dis[0][0]

#70%