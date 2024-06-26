"""
Nos emails do gmail os pontos são irrelevantes. Por exemplo manuel.maria@gmail.com
e manuelmaria@gmail.com são o mesmo email. Dada uma lista de emails do gmail, 
devolva a lista de emails únicos nela contidos, ordenados do mais frequente para 
o menos frequente, mostrando para cada um deles apenas a versão mais frequente. 
Em caso de empate em qualquer dos critérios use a ordem lexicográfica para desempatar.

    input: teste = ["alcinocunha@gmail.com","manuel@gmail.com","alcino.cunha@gmail.com","maria.francisca@gmail.com","mariafrancisca@gmail.com","alcino.cunha@gmail.com","alcino.cunha@gmail.com"]
    output: ['alcino.cunha@gmail.com', 'maria.francisca@gmail.com', 'manuel@gmail.com'])

    input: teste = ["maria@gmail.com","manuel@gmail.com","manuel@gmail.com","maria@gmail.com"]
    output: ["manuel@gmail.com","maria@gmail.com"]
    
"""

def emails(lista):
    
    def default(email):
 
        email_D = ""
        for i in range(len(email)):
            if email[i] != ".":
                email_D += email[i] 

        print(email_D)
        return email_D
    
    contas = {}
    lista_r = []
    
    
    for email in lista:
        email_D = default(email)
        email_c = ""
        for i in range(len(email)-4):
            email_c += email[i]
            
        if email_D not in contas:
            if "." in email_c:
                contas[email_D] = [email,0,1,1] ## com ponto
                contas[email_D][0] = email
            else:
                contas[email_D] = [email,1,0,1] ##sem ponto
                contas[email_D][0] = email
        else:
            if "." in email_c:
                contas[email_D][2] += 1
                contas[email_D][3] += 1
                
            else:
                contas[email_D][1] += 1
                contas[email_D][3] += 1
            contas[email_D][0] = email
    
    for conta in contas:
        lista_r.append(contas[conta][0])
    
    lista_r.sort()
    lista_r.sort(key=lambda item : contas[default(item)][3],reverse=True)
    
    return lista_r

#80%