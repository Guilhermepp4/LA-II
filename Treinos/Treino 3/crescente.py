"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.


input: lista = [15,27,14,38,26,55,46,65,85]
output: 6


input: lista = [5,2,7,4,3,8]
output: 3

lista = [6, 2, 5, 1, 7, 4, 8, 3]


"""

def crescente(lista):
    comprimento = len(lista)
    numero = 0
    nemo = [1] * comprimento  

    for t in range(comprimento):
        numero = lista[t]
        for i in range(1,comprimento - t):
            if numero <= lista[t+i]: 
                numero = lista[t+i]
                nemo[t] += 1

    print(nemo)
    return max(nemo)

#100%

def crescente(lista):
    
    size = []
    comprimento = len(lista)
    maior = 1
    size = [1 for x in range(comprimento)]
    print(size)
    if comprimento == 0:
       return 0
    
    
    for i in range(comprimento - 2, -1, -1):
        for j in range(i + 1, comprimento):    
            if lista[i] <= lista[j]:
                if maior < size[i] + size[j]:
                    maior = size[i] + size[j]
                
        size[i] = maior
        maior = 1
        print(size)

    
    return max(size)

#80%