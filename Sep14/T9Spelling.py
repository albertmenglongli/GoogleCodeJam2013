__author__ = 'LML'
T9Layout=dict({2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno"\
,7:"pqrs",8:"tuv",9:"wxyz",0:" "})
T9Mapping=dict()
for k in T9Layout.keys():
    v=T9Layout[k]
    for i in range(len(v)):
        T9Mapping.update({v[i]:str(k)*(i+1)})
def getCode(test):
    if len(test)==0:
        return ""
    result=""
    for i in range(len(test)):
        curNum=T9Mapping[test[i]][0]
        if len(result)>0 and curNum==result[-1]:
            result+=" "
        result+=T9Mapping[test[i]]
    return result

f=open("C-small-practice.in","r")
N=int(f.readline())
lines=f.readlines()
lines=[line.rstrip() for line in lines]

#lines=["hi","yes","foo  bar","hello world"]
#N=len(lines)

results=[]
for line in lines:
    results.append( getCode(line))


outF=open("Output","w")
for i in range(N):
    outF.write("Case #"+str(i+1)+": ")
    outF.write(results[i])
    if not i==N-1:
        outF.write("\n")
outF.flush()
outF.close()