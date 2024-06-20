'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.


        input: (["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"])
        output: ([('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])

        input: (["ab","bc","bd","cd"])
        output: [('a',1),('c',2),('d',2),('b',3)]
'''

def cruzamentos(ruas):
    palavras = {}
    
    for rua in ruas:
        
        if rua[0] not in palavras:
            palavras[rua[0]] = 0
        palavras[rua[0]] += 1
        
        if rua[-1] not in palavras:
            palavras[rua[-1]] = 0
        palavras[rua[-1]] += 1
        
        if rua[-1] == rua[0]:
            palavras[rua[0]] -= 1
    
    
    palavras_ordenadas = sorted(palavras.items(), key=lambda t: t[0])
    palavras_ordenadas.sort(key=lambda t: t[1])
    
    return palavras_ordenadas

#100%