def aloca(prefs):
    ListaAluno = sorted(prefs)
    ListaAlocados = {}
    Lista_Nao_Alocados = {}
    
    for aluno in ListaAluno:
        for projeto in prefs[aluno]:
            if projeto not in ListaAlocados:
                ListaAlocados.append(projeto)
            
    return  
