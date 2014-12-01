__author__ = 'LML'

dicSucessive={2:"double",3:"triple",4:"quadruple",5:"quintuple",6:"sextuple",7:"septuple",8:"octuple",9:"nonuple",10:"decuple"}
dicDigStr={'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}


def getResult(scontent,sformat):
    eachForN=sformat.split("-")
    eachForN=[int(i) for i in eachForN]
    groups= separateContentByEachForN(scontent,eachForN)
    result=[]
    for group in groups:
        result+=handle(group)
    return " ".join(result)

def handle(group):
    idx=0
    num=0
    result=[]
    while idx<len(group):
        num+=1
        if idx<len(group)-1 and group[idx+1]==group[idx]:
            idx+=1
            continue
        else:
            if num==1:
                result.append(dicDigStr[group[idx]])
            elif num>10:
                for j in range(num):
                    result.append(dicDigStr[group[idx]])
            else:
                result.append(dicSucessive[num])
                result.append(dicDigStr[group[idx]])
            num=0

            idx+=1
    return  result


def separateContentByEachForN(scontent,eachForN):
    idx=-1
    groups=[]
    for i in eachForN:
        group=[]
        for j in range(i):
            idx+=1
            group.append(scontent[idx])
        groups.append(group)
    return groups

if __name__=="__main__":
    f=open("A-large.in","r")
    N=int(f.readline())
    inputs=[]
    for i in range(0,N):

        strLine=f.readline().rstrip()
        scontent,sformat=strLine.split(" ")
        inputs.append((scontent,sformat))

    f.close()

    outF=open("Output","w")
    for i in range(N):
        outF.write("Case #"+str(i+1)+": ")
        strResult=getResult(inputs[i][0],inputs[i][1])
        outF.write(strResult)
        if not i==N-1:
            outF.write("\n")
    outF.flush()
    outF.close()

