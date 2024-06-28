'''

Numa turma pretende-se eleger uma comissão de alunos.
O objectivo é que a comissão seja um grupo de alunos 
que, em conjunto, conhecem todos os alunos da turma.
Implemente uma função que dada o conjunto de alunos da
turma e o conjunto dos pares de alunos que se conhecem
devolve o tamanho minimo necessário para essa comissão.


    input: alunos = {'pedro','maria','jose','manuel','francisca'}
           conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
     
    output: 2
            

    input:  alunos = {'pedro','maria','jose','manuel','francisca','joaquim'}
            conhecidos = {('pedro','maria'),('jose','francisca'),('manuel','joaquim')}
        
    output: 3

'''

def complete(graph, candidato, alunos):
    conhecidos = []
    
    if len(candidato) < 1:
        return False
        
    for aluno in candidato:
        for a in graph[aluno]:
            if a not in conhecidos:
                conhecidos.append(a)
    for b in alunos:
        if b not in conhecidos:
            return False
    
    return True

def extensions(graph, alunos, candidato):
    ext = []
    if candidato == []:
        for aluno in alunos:
            ext.append(aluno)
       
        return ext
    for aluno in alunos:
        if aluno not in candidato:
            ext.append(aluno)

    return ext
    
def search(graph, candidato, alunos, resp):

    if resp:
        if min(resp) <= len(candidato):
            return resp

    if complete(graph, candidato, alunos):
       
        resp.append(len(candidato))
        
        return resp
        
    else:
        for x in extensions(graph, alunos, candidato):
            new_candidato = candidato.copy()
            new_candidato.append(x)
            
            search(graph, new_candidato, alunos, resp)
        
    return resp

def mkgraph(conhecidos, graph):
    for aresta in conhecidos:
        if aresta[0] not in graph:
            graph[aresta[0]] = [aresta[0]]
        graph[aresta[0]].append(aresta[1])
        if aresta[1] not in graph:
            graph[aresta[1]] = [aresta[1]]
        graph[aresta[1]].append(aresta[0])
    
    return graph

def turma(alunos,conhecidos):

    if not alunos or not conhecidos:
        return 0
    
    graph = mkgraph(conhecidos,{})
    
    
    return min(search(graph, [], [x for x in alunos], []))

#50%