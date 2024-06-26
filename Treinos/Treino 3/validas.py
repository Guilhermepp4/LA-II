"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.
            
        input: listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]], 10
        output: [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]]
         
            
            
        input: listas = [[1,1,1,1,1],[2],[3,3,3,3,3,3,3],[4],[5,5,5,5,5]], 5
        output: [[1,1,1,1,1],[5,5,5,5,5]]
          
"""


def validas(soma, listas):

    soma_atual = 0
    lista_final = []
    j = 0
    t=0
    k=0
    if soma == 0 or listas == []:
        return []

    for lista in listas:
        soma_atual = 0
        for i in range(len(lista)):
            if lista[i] + soma_atual <= soma:
                soma_atual += lista[i]
                
        if soma_atual != soma:
            j+=1
            soma_atual = 0
            t=0
            for t in range(t+j,len(lista)):
                if lista[t] + soma_atual <= soma:
                    soma_atual += lista[t]
               
            if soma_atual != soma:
                k=0
                j+=1
                soma_atual = 0
                for k in range(k+j,len(lista)):
                    if lista[k] + soma_atual <= soma:
                        soma_atual += lista[k]
                        
            if soma_atual == soma and lista[0:len(lista)] not in lista_final:
                lista_final.append(lista[0:len(lista)])
        if soma_atual == soma and lista[0:len(lista)] not in lista_final:
            lista_final.append(lista[0:len(lista)])

    return lista_final

    #80%


def aux(soma, lista, comprimento_lista, indice, somasubseq):
    if comprimento_lista == 0:
        return 0

    for indice in range(len(lista)):
        somasubseq += lista[indice]
        if somasubseq > soma:
            return 0
        if somasubseq == soma:
            return soma

    return aux(soma, lista, comprimento_lista - 1, indice + 1, somasubseq)

def validas(soma, listas):
    resp = []
    for lista in listas:
        if aux(soma, lista, len(lista), 0, 0) == soma:
            resp.append(lista)

    return resp
    
    #90%



def validas(soma, listas):
    
    lista_final = []
    if soma == 0 or listas == []:
        return lista_final

    for lista in listas:
        soma_atual = 0
        for i in range(len(lista)):
            if soma_atual + lista[i] > soma:
                break
            soma_atual += lista[i]
        if soma_atual == soma and lista not in lista_final:
            lista_final.append(lista)
        else:
            j = 1
            while j < len(lista):
                soma_atual = 0
                for i in range(j, len(lista)):
                    if soma_atual + lista[i] > soma:
                        break
                    soma_atual += lista[i]
                if soma_atual == soma and lista[j:len(lista)] not in lista_final:
                    lista_final.append(lista[j:len(lista)])
                j += 1

    return lista_final
    #90%


def validas(soma, listas):
    
    lista_final = []
    if soma == 0 or listas == []:
        return lista_final

    for lista in listas:
        soma_atual = 0
        for i in range(len(lista)):
            if soma_atual + lista[i] > soma:
                break
            soma_atual += lista[i]
        if soma_atual == soma and lista not in lista_final:
            lista_final.append(lista)
        else:
            j = 1
            while j < len(lista):
                soma_atual = 0
                for i in range(j, len(lista)):
                    if soma_atual + lista[i] > soma:
                        break
                    soma_atual += lista[i]
                if soma_atual == soma and lista[j:len(lista)] not in lista_final:
                    lista_final.append(lista[j:len(lista)])
                j += 1

    return lista_final

    #80%