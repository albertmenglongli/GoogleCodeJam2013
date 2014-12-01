__author__ = 'LML'
def getResult(pairs):
    def getAllNames():
        names=[]
        for pair in pairs:
            first,second=pair
            if first not in names:
                names.append(first)
            if second not in names:
                names.append(second)
        return names

    def getOpps(name):
        results=[]
        for pair in pairs:
            first,second=pair
            if first==name:
                results.append(second)
            if second==name:
                results.append(first)
        return results

    names= getAllNames()
    dicOpps={}

    def place(k,X):
        name=names[k]
        opps=dicOpps[name]
        setA=set()
        for opp in opps:
            setA.add(opp)
        setB=set()
        for i in range(0,k):
            setB.add(names[i])
        setAnd= setA&setB

        for i in setAnd:
            idx= names.index(i)
            if X[k]==X[idx]:
                return False

        return True

    for name in names:
        dicOpps.update({name:getOpps(name)})

    numOfNames=len(names)
    X=[0]*numOfNames
    X[0]=0
    k=0
    flgResult=False
    while k>=0:
        X[k]+=1
        while X[k]<=2 and not place(k,X):
            X[k]+=1
        if X[k]>2:
            break
        if X[k]<=2:
            if k==numOfNames-1:
                flgResult=True
                print X
                break
            else:
                k+=1
                X[k]=0
        else:
            k-=1

    if flgResult:
        return "Yes"
    else :
        return "No"




if __name__=="__main__":
    f=open("A-small-2-attempt1.in","r")
    N=int(f.readline())
    inputs=[]
    for i in range(0,N):
        NN=int(f.readline())
        pairs=[]
        for i in range(0,NN):
            tmpPair=f.readline()
            tmpPair=tmpPair.strip()
            tmpPair=tmpPair.split(" ")
            pair=(tmpPair[0],tmpPair[1])
            pairs.append(pair)
        inputs.append(pairs)

    f.close()

    outF=open("Output","w")
    for i in range(N):
        outF.write("Case #"+str(i+1)+": ")
        pairs=inputs[i]
        result=getResult(pairs)
        outF.write(result)
        if not i==N-1:
            outF.write("\n")
    outF.flush()
    outF.close()