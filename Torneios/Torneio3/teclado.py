"""

Os teclados de computador costumam ter um teclado numérico no lado direito
com a seguinte configuração:

123
456
789
*0#

Implemente uma função que calcula quantas sequências de n digitos é
possível escrever neste teclado assumindo que depois de teclar um digito
só é possível teclar o mesmo digito ou um digito vizinho (na vertical ou
na horizontal). Por exemplo, para n = 2 é possível escrever as seguintes
sequências:

00, 08, 11, 12, 14, 21, 22, 23, 25, 32, 33, 36, 41, 44, 45, 47, … ,96, 98, 99

Sugere-se que comece por implementar uma função que calcule quantas
sequências de n digitos começando num determinado digito é possível escrever.


input: teclado(2)
output: 36


input: teclado(3)
output: 138

"""

def aux(n, nemo, i):
    if n == 0:
        return 1
    
    if (n, i) in nemo:
        return nemo[(n,i)]
        
    m = c = d = b = e = 0
    
    if i == 0:
        c = aux(n-1, nemo, 8) 
        m = aux(n-1, nemo, 0)
    else: 
        if i not in [1, 2 ,3]:
            c = aux(n-1, nemo, i - 3)  
        if i not in [7, 0 ,9]:
            if i != 8:
                b = aux(n-1, nemo, i + 3)
            else:
                b= aux(n-1, nemo, 0)
        if i not in [3, 6 ,9, 0]:
            d = aux(n-1, nemo, i + 1)
        if i not in [1, 4, 7, 0]:
            e = aux(n-1, nemo, i - 1)
        m = aux(n-1, nemo, i)
    
    nemo[(n,i)] = m + c+ d+ e + b
    return nemo[(n,i)]
def teclado(n):
    
    resp = 0
    nemo = {}
    
    for i in range(10):
        print(i)
        resp += aux(n-1, nemo, i)

    return resp 

#100%