'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.

input: "o tempo perguntou ao tempo quanto tempo o tempo tem"
output: ['tempo','o','ao','perguntou','quanto','tem']

input: "ola"
output: ['ola']
'''

def frequencia(texto):
    palavras = {}
    finaleira = []
    
    for text in texto.split():
        if text not in palavras:
            palavras[text] = 1
        else:
            palavras[text] += 1
    final = sorted(palavras.items(), key = lambda t: t[0])

    final.sort(key = lambda t: t[1], reverse = True)
    
    for i in final:
        finaleira.append(i[0])
        
    return finaleira

#100%