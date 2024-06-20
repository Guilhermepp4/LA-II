'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

[("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])


'''

def tabela_class(lista_final , jogos):
    for jogo in jogos: 
        if jogo[0] not in lista_final:
            lista_final[jogo[0]] = 0
        if jogo[2] not in lista_final:
            lista_final[jogo[2]] = 0
    return

def saldo_golos(lista_golos, jogos):
    for jogo in jogos:
        lista_golos[jogo[0]] += jogo[1] - jogo[3]
        lista_golos[jogo[2]] += jogo[3] - jogo[1]
    return

def tabela(jogos):
    
    lista_golos = {}
    lista_final = {}
    
    tabela_class(lista_final, jogos)
    
    lista_golos = lista_final.copy()
    
    saldo_golos(lista_golos, jogos)
    
    for jogo in jogos:
        if jogo[1] > jogo[3]:
            lista_final[jogo[0]] +=3
        elif jogo[1] < jogo[3]: 
            lista_final[jogo[2]] +=3
        else:   
            lista_final[jogo[0]] +=1
            lista_final[jogo[2]] +=1
    
    lista_final = list(lista_final.items())
    
    lista_final.sort(key=lambda item: item[0])
    lista_final.sort(key=lambda item: lista_golos.get(item[0]), reverse=True)
    lista_final.sort(key=lambda item: (item[1]), reverse=True)
    
    return(lista_final)

#100%