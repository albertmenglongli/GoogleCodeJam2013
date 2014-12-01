__author__ = 'LML'
import sys
from math import *
def IsApproximatelyEqual(x, y, epsilon=1e-6):
  """Returns True iff y is within relative or absolute 'epsilon' of x.

  By default, 'epsilon' is 1e-6.
  """
  # Check absolute precision.
  if -epsilon <= x - y <= epsilon:
    return True

  # Is x or y too close to zero?
  if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
    return False

  # Check relative precision.
  return (-epsilon <= (x - y) / x <= epsilon
       or -epsilon <= (x - y) / y <= epsilon)
def getResult(V,D):
    g=9.8
    sinTcosT=D*g/(2*V*V)
    sinDoubleT=sinTcosT*2
    from math import asin,pi
    if IsApproximatelyEqual(sinDoubleT,1.0):
        sinDoubleT=1.0
    doubleT=asin(sinDoubleT)
    T=doubleT/2.0*180/pi
    return T


#V,D=238.0, 5780.0
#g=9.8
#sinTcosT=D*g/(2*V*V)
#sinDoubleT=sinTcosT*2
#print sinDoubleT
#print IsApproximatelyEqual(sinDoubleT,1.0)
#
#sys.exit(0)



f=open("B-small-attempt1.in","r")
N=int(f.readline())
inputs=[]
for i in range(0,N):
    line=f.readline().strip()
    pair=line.split(" ")
    inputs.append((float(pair[0]),float(pair[1])))


f.close()



outF=open("Output","w")
for i in range(N):
    outF.write("Case #"+str(i+1)+": ")
    pair=inputs[i]
    result=getResult(pair[0],pair[1])
    print result
    outF.write(str(result))
    if not i==N-1:
        outF.write("\n")
outF.flush()
outF.close()
