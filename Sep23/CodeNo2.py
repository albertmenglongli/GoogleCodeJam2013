__author__ = 'LML'

def problem1(pos):
    lstOf01=[]
    while not pos==1:
        lstOf01.append(pos%2)
        pos/=2
    lstOf01.reverse()
    p=q=1
    for i in lstOf01:
        if i==0:
            p=p
            q+=p
        else:
            q=q
            p+=q
    return p,q



def problem2(fir,sec):
    lstOf01=[]
    def getMaxPQ(f,s):
        if f==s:
            return 1
        ma=max(f,s)
        if ma==s:
            p0=f
            q0=s-f
        else:
            q0=s
            p0=f-s
        return max(p0,q0)

    def getPathBack(f,s):
        if f==s:
            return
        if f>s:
            lstOf01.append(1)
        else:
            lstOf01.append(0)
        ma=max(f,s)
        if ma==s:
            p=f
            q=s-f
        else:
            q=s
            p=f-s
        getPathBack(p,q)

    getPathBack(fir,sec)
    lstOf01.reverse()
    cntsAboveThisLevel=pow(2,len(lstOf01))-1

    cntsInThisLevelBefore=0

    for i in range(0,len(lstOf01)):
        if lstOf01[i]==0:
            continue
        else:
            cntsInThisLevelBefore+=int(pow(2,len(lstOf01)-i-1))
    return int(cntsAboveThisLevel+cntsInThisLevelBefore+1)




if __name__=='__main__':
    from math import *
#    print problem1(17)
#    print problem2(5,4)
#    print problem1(44926)
#    print problem2(191,219)
#    for i in range(1,15):
#        print problem1(i)
#    print problem2(10,3)



    f=open("B-small-attempt0.in","r")
    N=int(f.readline())
    inputs=[]
    for i in range(0,N):
        strLine=f.readline().rstrip()
        strContent=strLine.split(" ")
        typeID=int(strContent[0])
        if typeID==1:
            para=int(strContent[1])
            inputs.append((1,para))
        elif typeID==2:
            paras=(int(strContent[1]),int(strContent[2]))
            inputs.append((2,paras))
    f.close()

    outF=open("Output","w")
    for i in range(N):
        outF.write("Case #"+str(i+1)+": ")
        if inputs[i][0]==1:
            result=problem1(inputs[i][1])
            result=[str(i) for i in result]
            result=list(result)
            strResult=" ".join(result)
        elif inputs[i][0]==2:
            result=problem2(inputs[i][1][0],inputs[i][1][1])
            strResult=str(int(result))
        outF.write(strResult)
        if not i==N-1:
            outF.write("\n")
    outF.flush()
    outF.close()