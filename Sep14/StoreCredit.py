__author__ = 'LML'
f=open("A-large-practice.in","r")
N=int(f.readline())
inputs=[]
for i in range(0,N):
    C=int(f.readline())
    I=int(f.readline())
    Ps=f.readline()
    Ps.rstrip()
    Ps=Ps.split(" ")
    Ps0=[int(p) for p in Ps ]
    Ps1=[int(p) for p in Ps ]
    Ps1.sort()
    inputs.append((C,I,Ps1,Ps0))

f.close()

def calValue(C,Ps):
    sum=0
    l=0
    u=len(Ps)-1
    while l<u:
        if Ps[l]+Ps[u]==C:
            return l,u
        while Ps[l]+Ps[u]<C:
            l+=1
        while Ps[l]+Ps[u]>C:
            u-=1
    return None

results=[]

for input in inputs:
    C,I,Ps,Ps0=input
    l,u= calValue(C,Ps)
    idx1=-1
    idx2=-1
    value1=Ps[l]
    value2=Ps[u]

    for i in range(len(Ps0)):
        if Ps0[i]==value1 and idx1<0:
            idx1=i
        if Ps0[i]==value2 and idx1!=i and idx2<0:
            idx2=i

    idx1+=1
    idx2+=1
    if idx1>idx2:
        idx1^=idx2
        idx2^=idx1
        idx1^=idx2
    result=idx1,idx2
    results.append( result)

outF=open("Output","w")
for i in range(N):
    outF.write("Case #"+str(i+1)+": ")
    outF.write(str(results[i][0])+" "+str(results[i][1]))
    if not i==N-1:
        outF.write("\n")
outF.flush()
outF.close()