# llista = list(input("Introdueix una llista de paraules: ").split())
# llista_ordenada = sorted(llista)

# valor_ant = None
# resultat = []

# for i in llista_ordenada:
#     if i != valor_ant:
#         resultat.append(i)
#     valor_ant = i
# print(resultat)



llista = list(input("Introdueix una llista de paraules: ").split())
resultat = list(set(llista))
print(resultat)