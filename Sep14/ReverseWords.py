__author__ = 'LML'
f=open("B-large-practice.in","r")
N=int(f.readline())
lines=f.readlines()
lines=[line.rstrip() for line in lines]


def ReverseWords(line):
    newLine=[]
    line=line.split(" ")
    for i in range(len(line)-1,-1,-1):
        newLine.append(line[i])
    return " ".join(newLine)



results=[]
for line in lines:
    results.append(ReverseWords(line))

outF=open("Output","w")
for i in range(N):
    outF.write("Case #"+str(i+1)+": ")
    outF.write(results[i])
    if not i==N-1:
        outF.write("\n")
outF.flush()
outF.close()