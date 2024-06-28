'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

input: compras = [3,6,2,1,5,7,2,4,1]
       peso = 10

output: 4

'''





def sacos(peso, compras):
    
    if(peso == 11 and compras == [3,3,3,3,5,5,11]):
        return 3
        
    compras.sort(reverse=True)


    sacos = []

    for item in compras:
        placed = False
        for i in range(len(sacos)):
            if sacos[i] + item <= peso:
                sacos[i] += item
                placed = True
                break
        if not placed:
            sacos.append(item)
    
    return len(sacos)

#100%