"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""
def hacker(log):

    pin_copy = ""
    pin_cracker = ""
    mail_card = {}
    resp=[]

    for tuplo in log:
        if tuplo[1] not in mail_card:
            mail_card[tuplo[1]] = tuplo[0]
        elif tuplo[1] in mail_card:
            pin_copy = mail_card[tuplo[1]]
            pin_cracker = ""
            for i in range(16):
                if tuplo[0][i] != "*":
                    pin_cracker += tuplo[0][i]
                else:
                    pin_cracker += pin_copy[i]
            mail_card[tuplo[1]] = pin_cracker
            
    for mail in mail_card:
        resp.append((mail_card[mail],mail))

    resp.sort(key=lambda x: x[1])
    resp.sort(key=lambda x: x[0].count("*"))

    return resp

#100%