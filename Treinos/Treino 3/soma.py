"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.


    input = lista = [-2,1,-3,4,-1,2,1,-5,4]
    output = 6

            
            
    input = lista = [1,2,3,4,-11,1,2,3,4,5]
    output = 15


"""


def maxsoma(lista):
    comprimento = len(lista)
    max_val = max_atu = lista[0]

    for i in range(comprimento):
        soma_atual = lista[i]
        for j in range(i+1,comprimento):
            soma_atual += lista[j]
            max_atu = max(max_atu, soma_atual)
        max_val = max(max_val, max_atu)

    return max_val
    
def maxsoma(lista):
    max_atual = max_total = lista[0]  # Inicialize ambas as variáveis com o primeiro elemento da lista
    
    for num in lista[1:]:  # Começando do segundo elemento da lista
    
        max_atual = max(num, max_atual + num)  # Escolha entre o número atual e a soma atual + o número atual
        max_total = max(max_total, max_atual)  # Atualize a maior soma total
    
    return max_total
    
#100%
    