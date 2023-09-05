
l1=[10,9,8]
l2=[7,6,5]
res=l1+l2

maior=res[0]
nmaior=0
nmenor=0
for i in range(len(l1)):
    menor=res[0]
    maior=res[0]
    for a in range(len(res)):
        if maior<res[a]:
            maior=res[a]
            nmaior=a
        if menor>res[a]:
            menor=res[a]
            nmenor=a  
    l1[i]=res[nmenor]
    res.pop(nmenor)
    l2[i]=res[nmaior]
    res.pop(nmaior)

print("l1=",l1)
print("l2=",l2)    