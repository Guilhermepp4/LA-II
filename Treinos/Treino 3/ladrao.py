"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

input: 10 , objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
output: 46

"""

def ladrao(capacidade,objectos):
    objectos.sort(key = lambda x: x[1]/x[2], reverse = True)
    
    print(objectos)
    cap = 0
    lista_obj = []
    
    for objeto in objectos:
        cap += objeto[2]
        
        if cap <= capacidade:
            lista_obj.append(objeto)
            
    soma = 0
    for objeto in lista_obj:
        soma += objeto[1]
    return soma

#80%