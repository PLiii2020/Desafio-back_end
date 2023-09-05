#ler a matriz txt
def ler(a):
    with open(a, "r") as arquivo:

        
        matriz =arquivo.readlines()
        matriz=[x.strip('\n') for x in matriz] 
        print(matriz)
        print(" ".join(str(a) for a in matriz))
        matriz=" ".join(str(a) for a in matriz)
        matriz=matriz.split()
     
    linha =int(matriz[0])
    matriz.pop(0)
   
    coluna =int(matriz[0])
    matriz.pop(0)
    m=[]
    cont=0
    for l in range(linha):
        a=[]
        for c in range(coluna):
            elemento=int(matriz[cont])
            cont=cont+1
            a.append(elemento)
        m.append(a)
    print("Matriz inicial:")       
    polir_matriz(linha,coluna,m)
    print("Matriz apos a retirada de iguais:")
    iguais(linha,coluna,m)

  



#Deixar a matriz organizada
def polir_matriz(linha,coluna,m):
    for l in range(linha):
        for c in range(coluna):
          print(f'[{m[l][c]:^5}]',end='')
        print()  

#igualar valores iguais a zero deixando apenas o valor original    
def iguais(linha,coluna,m):
    
   for i in range(0,3):
      for j in range(0,3):
       
     
        x=0
        for a in range(0,linha):
            for b in range(0,coluna):
         
                if   m[i][j]==m[a][b] :
                    x=x+1
                    
                    if x>1:
                        m[a][b]=0
   polir_matriz(linha,coluna,m)
    
#no arquivo mat.txt houve a necessidade da primeira linha identificar a linha e a coluna da matriz a ser escrita
ler("mat.txt")