"""

Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partido num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.


            input = probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
                    passos = 2
            
            output = 0.25

            input = probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
                    passos = 6
            
            output = 0.08

"""

def aux(p, x, y, probs, cache):
    if p == 0:
        if (x,y) == (0,0):
            return 1
        else:
            return 0
    if (p,x,y) in cache:
        return cache[(p,x,y)]
    a = probs['U'] * aux(p-1, x+1, y, probs, cache)
    b = probs['D'] * aux(p-1, x-1, y, probs, cache)
    c = probs['L'] * aux(p-1, x, y-1, probs, cache)
    d = probs['R'] * aux(p-1, x, y+1, probs, cache)
    cache[(p,x,y)] = a+b+c+d
    return cache[(p,x,y)]

def probabilidade(passos,probs):
    return round(aux(passos, 0, 0, probs, {}),2) if passos % 2 == 0 else 0.0

#100%