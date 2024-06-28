'''

Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.


    input: sets = [{1,2,3},{2,4},{3,4},{4,5}]
    output: 2


    input: sets = [{1},{2},{3,4},{5,6,7,8},{1,3,5,7},{2,4,6,8},{9}]
    output: 3

'''

from itertools import combinations

def uniao(sets):
    union_all = set().union(*sets)
    
    for r in range(1, len(sets) + 1):
        for set1 in combinations(sets, r):
            print(set1)
            union_subset = set().union(*set1)
            if union_subset == union_all:
                return r
    return len(sets)
            
#100%