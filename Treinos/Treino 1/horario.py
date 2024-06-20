"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.


    input: ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
           alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
            
    output: [(1000, 7), (5000, 4)])
    

    input: ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1)}
           alunos = {5000: {"la2","pi"}, 2000: {"pi","la2"}}
    
    output: [(2000, 3), (5000, 3)])

"""

def horario(ucs,alunos):
    
    final = []
    
    for aluno in alunos:
        
        dias = []
        horarioFim = {"segunda":[] ,"terca":[] , "quarta":[] ,"quinta":[] ,"sexta":[]}
        inicio = {"segunda":[] ,"terca":[] , "quarta":[] ,"quinta":[] ,"sexta":[]}
        horas = 0
        run = True
        
        for i in alunos[aluno]:
            
            if i not in ucs:
                horas = -1
                break;
                
            if ucs[i][0] in dias:
                dia = ucs[i][0]
                for y in range(5):
                    if ucs[i][1] + ucs[i][2] in horarioFim[dia] or (ucs[i][1] + ucs[i][2] < horarioFim[dia][y] and ucs[i][1] + ucs[i][2] > inicio[dia][y]):
                        horas = 0
                        run = False
                        break;
                    
                
                else:
                    horas += ucs[i][2]
                    horarioFim[ucs[i][0]].append(ucs[i][1])
                    
            if ucs[i][0] not in dias:
                
                dias.append(ucs[i][0])

                horas += ucs[i][2]
                horarioFim[ucs[i][0]].append(ucs[i][1]+ucs[i][2])
                inicio[ucs[i][0]].append(ucs[i][1])
                
 
        if run and horas != -1:
            fim = (aluno, horas)
            final.append(fim)
            fim = []

            
    final.sort(key = lambda t : t[0])
    final.sort(key = lambda t : t[1], reverse = True)
    
    return final

#100%