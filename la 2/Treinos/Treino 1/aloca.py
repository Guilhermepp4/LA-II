"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

prefs = {10885:[1,5],40000:[5],10000:[1,2]}

"""

def aloca(prefs):

    lista_nalocados = []
    alunos = sorted(prefs)
    lista_projetos = []

    for aluno in alunos:
        for projeto in prefs[aluno]:

            if projeto not in lista_projetos:
                lista_projetos.append(projeto)
                break
        else:
            lista_nalocados.append(aluno)

    return lista_nalocados

#100%
    