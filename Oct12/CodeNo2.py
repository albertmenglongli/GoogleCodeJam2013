__author__ = 'LML'

def getDistance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def getPointsFromArea(x1,y1,x2,y2):
    points=[]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            points.append((i,j))
    return points

def getPointsFromAreas(areas):
    points=[]
    for area in areas:
        points+=getPointsFromArea(area[0],area[1],area[2],area[3])
    return points

def getPointsFromResults(points):
    if len(points)==1:
        return points[0]
    elif len(points)>1:
        from operator import itemgetter
        points=sorted(points, key=itemgetter(0,1))
        return points[0]





def getResult(input):
    N,arr=input

    allPoints=getPointsFromAreas(arr)

    totalD=float("inf")
    results=[]
    for p in allPoints:
        tmpD=0
        for otherP in allPoints:
            tmpD+=getDistance(p,otherP)
        if tmpD<totalD:
            totalD=tmpD
            results=[]
            results.append(p)
        elif tmpD==totalD:
            results.append(p)
        else:
            continue

    point=getPointsFromResults(results)

    return point[0],point[1],totalD



if __name__=="__main__":
    f=open("B-large.in","r")
    Cnt=int(f.readline())
    inputs=[]
    for i in range(0,Cnt):
        N=int(f.readline().rstrip())
        arrs=[]
        for j in range(0,N):
            strLine=f.readline().rstrip()
            numbersStr=strLine.split(" ")
            numbers=[int(number) for number in numbersStr]
            arrs.append(numbers)
        inputs.append((N,arrs))
    f.close()


    outF=open("Output","w")
    for i in range(Cnt):
        outF.write("Case #"+str(i+1)+": ")
        tupleResult=getResult(inputs[i])
        listResult=list(tupleResult)
        listResult=[str(i) for i in listResult]
        strResult=" ".join(listResult)
        outF.write(strResult)
        if not i==Cnt-1:
            outF.write("\n")
    outF.flush()
    outF.close()
