"""

Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

            input: mapa = [".3......",
                           "........",
                           "...5#...",
                           "...##...",
                           ".....9..",
                           "..2.....",
                           "..2.....",
                           "..2....."]
                    
            output: 12

"""
def aux(mapa, x, y, xfinal, yfinal, cache):
    if x == xfinal and y == yfinal:
        if mapa[x][y] not in [".","#"]:
            return int(mapa[x][y])
        else:
            return 0

    if (x,y) in cache:
        return cache[(x,y)]

    b = 0
    d = 0

    if x + 1 <= xfinal and mapa[x+1][y] != "#":
        if mapa[x][y] == ".":
            d = 0 + aux(mapa, x+1, y, xfinal, yfinal, cache)
        else:
            d = int(mapa[x][y]) + aux(mapa, x+1, y, xfinal, yfinal, cache)
    if y + 1 <= yfinal and mapa[x][y+1] != "#":
        if mapa[x][y] == ".":
            b = 0 + aux(mapa, x, y+1, xfinal, yfinal, cache)
        else:
            b = int(mapa[x][y]) + aux(mapa, x, y+1, xfinal, yfinal, cache)
    
    cache[(x,y)] = max(b,d)
    return cache[(x,y)]

def saque(mapa):
    return aux(mapa, 0, 0, len(mapa) - 1, len(mapa[0]) - 1, {})

#80%