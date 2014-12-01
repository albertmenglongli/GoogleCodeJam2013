__author__ = 'LML'

def getResult(lst):
    lstOdd=[x for x in lst if not x%2==0]
    lstEven=[x for x in lst if x%2==0]
    lstOddIdx=[]
    lstEvenIdx=[]
    for i in range(len(lst)):
        if lst[i]%2==0:
            lstEvenIdx.append(i)
        else:
            lstOddIdx.append(i)

    lstEven.sort(reverse=True)
    lstOdd.sort()
    result=[]

    for i in range(len(lst)):
        if i in lstEvenIdx:
            result.append(lstEven[lstEvenIdx.index(i)])
        else:
            result.append(lstOdd[lstOddIdx.index(i)])
    return result

if __name__=="__main__":

    f=open("C-large.in","r")
    N=int(f.readline())
    inputs=[]
    for i in range(0,N):
        nn=int(f.readline())
        strContent=f.readline().rstrip()
        lstStr=strContent.split(" ")
        lstNum=[int(i) for i in lstStr]
        inputs.append(lstNum)

    f.close()

    outF=open("Output","w")
    for i in range(N):
        outF.write("Case #"+str(i+1)+": ")
        result=getResult(inputs[i])
        result=[str(i) for i in result]
        strResult=" ".join(result)
        outF.write(strResult)
        if not i==N-1:
            outF.write("\n")
    outF.flush()
    outF.close()
