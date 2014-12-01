__author__ = 'LML'
import sys

def generateLe():
    lstL=map(chr,range(97,123))
    lstU=map(chr,range(65,65+26))
    Lexicographically={}
    for i in range(len(lstL)):
        Lexicographically.update({lstL[i]:i+27})
    for i in range(len(lstU)):
        Lexicographically.update({lstU[i]:i+1})
    Lexicographically.update({' ':0})
    return Lexicographically
comTable=generateLe()

def myCompare(str1,str2):
    global comTable
    minLen=min(len(str1),len(str2))
    i=-1
    while i <minLen:
        i+=1
        if comTable[str1[i]]<comTable[str2[i]]:
            return -1
        elif comTable[str1[i]]>comTable[str2[i]]:
            return 1
        else:
            continue

    return 1

def mySort(names):
    print names
    cnt=0
    for i in range(1,len(names)):
        if myCompare(names[i-1],names[i])>0:
            cnt+=1
            tmp=names[i]
            j=i
            while myCompare(names[j-1],tmp)>0 and j>0:
                names[j]=names[j-1]
                j-=1
            names[j]=tmp
    print names
    return cnt


fileName="C-small-2-attempt0.in"
f=open(fileName,"r")
N=int(f.readline())
inputs=[]
for i in range(0,N):
    NN=int(f.readline())
    names=[]
    for j in range(NN):
        line=f.readline().strip()
        names.append(line)
    inputs.append(names)
f.close()




outF=open("Output","w")
for i in range(N):
    outF.write("Case #"+str(i+1)+": ")
    names=inputs[i]
    result=mySort(names)
    print result
    outF.write(str(result))
    if not i==N-1:
        outF.write("\n")
outF.flush()
outF.close()





