import time
start=time.time()
l1=[2,3,2]
l2=[3,2,2]

for i in range (len(l1)):
    maiorl1=l1[0]
    maiorl2=l2[0]
    nl1=0
    nl2=0
    for a in range(len(l2)):
        if maiorl1 < l1[a]:
            maiorl1=l1[a]
            nl1=a
        if maiorl2<l2[a]:
            maiorl2=l2[a]
            nl2=a
    
    if maiorl1 == maiorl2:
        a=True
        l1.pop(nl1)
        l2.pop(nl2)
    else:
        a=False
        break

if a :
    end=time.time()
    print("é uma permutação",(end-start))
else :
    end=time.time()
    print("Não é uma permutação",(end-start))
               