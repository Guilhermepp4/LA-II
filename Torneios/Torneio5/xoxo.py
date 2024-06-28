'''

Considere um jogo onde temos uma sequência de 'o's e 'x's,
onde um 'o' representa um espaço vazio e um 'x' uma peça.
As jogadas possíveis são mover uma peça para o lado (esquerdo
ou direito), caso a posição ao lado esteja vazia, ou
"comer" uma peça ao lado caso a posição seguinte esteja vazia.
Para ganhar o jogo, o objectivo é ficar apenas com uma peça. 
Por exemplo, se começarmos com

xoxo

podemos ganhar o jogo, movendo o primeiro 'x' para a direita, 
resultando no seguinte estado,

oxxo

e depois usar o primeiro 'x' para comer o segundo, resultando em

ooox

Obviamente, existem várias outras sequências de jogadas que permitem
ganhar o jogo.

Implemente uma função que, dada uma linha com a descrição da
configuração inicial do jogo, determine o número mínimo de jogadas
necessárias para ganhar o jogo (2 no caso do exemplo acima).

Sugere-se que comece por implementar uma função que dado um
estado do jogo calcule todos os possíveis resultados de fazer
uma jogada.





input: linha = "xoxo"
outpu: 2

input: linha = "xxoxox"
output: 3


'''

def complete(linha):
    count_x = 0
    
    for pos in linha:
        if pos == "x":
            count_x += 1
    
    return count_x == 1
    
def extensions(linha, jogadas):
    ext = []

    
    for i in range(len(linha)):
        
        linha_atual = linha.copy()
        if i+2 < len(linha):
            if linha_atual[i] == "x" and linha_atual[i+1] == "x" and linha_atual[i+2] == "o":
                linha_atual[i] = "o"
                linha_atual[i+1] = "o"
                linha_atual[i+2] = "x"
                if linha_atual not in jogadas:
                    
                    ext.append(linha_atual)
                    linha_atual = linha.copy()
        
        if i-2 >= 0:
            if linha_atual[i] == "x" and linha_atual[i-1] == "x" and linha_atual[i-2] == "o":
                    linha_atual[i] = "o"
                    linha_atual[i-1] = "o"
                    linha_atual[i-2] = "x"
                    if linha_atual not in jogadas:
                        ext.append(linha_atual)
                        linha_atual = linha.copy()
            
        if i+1 < len(linha):
            if linha_atual[i] == "x" and linha_atual[i+1] == "o":
                linha_atual[i] = "o"
                linha_atual[i+1] = "x"
                if linha_atual not in jogadas:
                    ext.append(linha_atual)
                    linha_atual = linha.copy()
        
        if i-1 >= 0:
            if linha_atual[i] == "x" and linha_atual[i-1] == "o":
                linha_atual[i] = "o"
                linha_atual[i-1] = "x"
                if linha_atual not in jogadas:
                    ext.append(linha_atual)
                    linha_atual = linha.copy()

    return ext
    
def aux(linha, count, resp, jogadas):
    if complete(linha):
        resp.append(count)
    for ext in extensions(linha, jogadas):
        jogadas.append(ext)
        aux(ext, count+1 , resp, jogadas)
    
    return resp

def xoxo(linha):
    linha = list(linha)
    return min(aux(linha, 0, [], [linha]))
   
#80%