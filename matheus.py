lista5 = []
lista4 = []
lista3 = []
lista2 = []

for dez1 in range(50):
    for dez2 in range(dez1+1,50):
        lista2.append([dez1 + 1, dez2 + 1])
        for dez3 in range(dez2+1,50):
            lista3.append([dez1 + 1, dez2 + 1, dez3 + 1])
            for dez4 in range(dez3+1,50):
                lista4.append([dez1 + 1, dez2 + 1, dez3 + 1, dez4 + 1])
                for dez5 in range(dez4+1,50):
                    lista5.append([dez1+1,dez2+1,dez3+1,dez4+1,dez5+1])

print(len(lista5))
print(len(lista4))
print(len(lista3))
print(len(lista2))
