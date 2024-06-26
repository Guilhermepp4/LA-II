"""

    Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
    Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
    tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
    que lhe permitirá ter a máxima receita.
    
    Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
    e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
    disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
    que poderá obter se vender todos os produtos que escolher transportar, e a lista
    de produtos que deverá levar para obter essa receita (incluindo repetições, 
    caso se justifique), ordenada alfabeticamente.
    
    Cada produto consiste num triplo com o nome, o valor, e o peso.
    
    Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
    aos produtos que aparecem primeiro na lista de entrada.
    
    
    input:produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    capacidade = 14
    
    output: lucro = 190
            lista = ["biblia","biblia","microondas"]))
    
    [("Verde",4,12),("Azul",2,2),("Cinzento",2,1),("Laranja",1,1),("Amarelo",10,4)]
    (36,["Amarelo","Amarelo","Amarelo","Cinzento","Cinzento","Cinzento"]))


"""

def vendedor(capacidade, produtos):
    if capacidade == 0 or not produtos:
        return 0, []

    produtos.sort(key=lambda t: t[1] - t[2], reverse=True)
    lucro = 0
    lista = []

    for produto in produtos:
        while capacidade >= produto[2]:  # Enquanto houver capacidade para adicionar este produto
            capacidade -= produto[2]
            lucro += produto[1]
            lista.append(produto[0])

    return lucro, lista

#50%