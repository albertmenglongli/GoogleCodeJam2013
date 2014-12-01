__author__ = 'LML'
import numpy as np

def getResult(input):
    N,arr=input
    NN=N*N
    flg="Yes"
    for j in range(0,NN):
        for i in range(1,NN+1):
            if i in arr[j]:
                continue
            else:
                flg="No"
                return flg

    for j in range(0,NN):
        lst=zip(*arr)[j]
        for i in range(1,NN+1):
            if i in lst:
                continue
            else:
                flg="No"
                return flg
    arr=np.array(arr)
    for m in range(0,N):
        for n in range(0,N):
            lst= arr[m*N:m*N+N,n*N:n*N+N]
            for i in range(1,NN+1):
                if i in lst:
                    continue
                else:
                    flg="No"
                    return flg

    return flg







if __name__=="__main__":
    f=open("A-large.in","r")
    Cnt=int(f.readline())
    inputs=[]
    for i in range(0,Cnt):
        N=int(f.readline().rstrip())
        arrs=[]
        for j in range(0,N*N):
            strLine=f.readline().rstrip()
            numbersStr=strLine.split(" ")
            numbers=[int(number) for number in numbersStr]
            arrs.append(numbers)
        inputs.append((N,arrs))
    f.close()

    outF=open("Output","w")
    for i in range(Cnt):
        outF.write("Case #"+str(i+1)+": ")
        strResult=getResult(inputs[i])
        outF.write(strResult)
        if not i==Cnt-1:
            outF.write("\n")
    outF.flush()
    outF.close()