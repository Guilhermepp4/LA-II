'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.


                "Todos os nomes":"9789720047572",
                "Ensaio sobre a cegueira":"9789896604011",
                "Memorial do convento":"9789720046711",
                "Os cus de Judas":"9789722036757"
                
                ["Memorial do convento","Todos os nomes"])

'''

def isbn(livros):
    invalidos = []
    for livro in livros:
        digito = 0
        posicao = 0
        numero = livros[livro]
        while (posicao <= 12):
            if posicao % 2 == 1:
                digito += int(numero[posicao]) * 3
            else:
                digito += int(numero[posicao]) * 1
            posicao += 1
        if digito % 10 != 0:
            invalidos.append(livro)
            invalidos.sort()
    return invalidos

#100%