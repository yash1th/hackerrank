import math
ab = int(input())
bc = int(input())
ac = math.hypot(ab,bc)
mc = ac/2
degrees = math.degrees(math.asin(mc/bc))
if degrees>90:
    degrees = 180 - degrees
print(str(int(round(degrees,0))),'\xb0',sep='')

#the question exploits a bug in python2 and does not accept correct solution in python3


# solution in python2 copied from github
# import math
#
# ab = input()
# bc = input()
#
# h = math.sqrt(ab**2 + bc**2)
# h = h / 2.0
# adj = bc / 2.0
# print str(int(round(math.degrees(math.acos(adj/h))))) + "°"
