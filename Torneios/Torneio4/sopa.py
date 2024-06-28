'''

Dada uma lista de palavras diferentes todas com o
mesmo tamanho N, defina uma função que calcula
quantas sopas de letras de tamanho N x N podem
ser construidas com essas palavras, sendo que
uma sopa de letras só é válida se todas as 
suas linhas e colunas forem palavras diferentes
retiradas da lista dada.

Por exemplo se as palavras forem

['age','ago','beg','cab','cad','dog']

é possível construir as seguintes sopas de letras

cab
age
dog

cad
ago
beg



    input: palavras = ['age','ago','beg','cab','cad','dog']
    output: 2

    input: palavras = ['is','so','no','in','on','si']
    output: 4
'''

from itertools import permutations


def valid(lista, palavras):
    
    size = len(lista[0])
        
    for num in range(size):
        curr_wrd = ""
        for palavra in lista:
            curr_wrd += palavra[num]
        if curr_wrd not in palavras or curr_wrd in lista:
            return False
     
    return True

def sopa(palavras):
    
    tamanho = len(palavras[0])
        
    count = 0

    for x in permutations(palavras,tamanho):

        lista = []
        
        for pal in x:
            lista.append(pal)
        
        if valid(lista, palavras):
            count+=1
            
            
    
    return count
    
#50%