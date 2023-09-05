lista=[6,90,3,9,100]
quant=0
maior=lista[0]
n=0
for b in range(0,3):
    maior=lista[0]
    for a in range(0,len(lista)):
        if maior < lista[a]:
            maior=lista[a]
            n=a
    lista.pop(n)

print("O terceiro maior valor dessa lista é",maior)