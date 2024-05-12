from math import sqrt

'''Sx = float(input( "Sx: " ))
Sy = float(input( "Sy: " ))
Sz = float(input( "Sz: " ))
r = float(input( "r: " ))

Px = float(input( "Px: " ))
Py = float(input( "Py: " ))
Pz = float(input( "Pz: " ))
'''

S = (4,5,2)

r = 2

P = (5.45, 4.78, 0.64)

vector = [0,0,0]
absVector = [0,0,0]
length = 0

# Tar inn sentrumspunktet og referansepunktet og lager en sirkel på formen: 
# (x-px)**2+(y-py)**2+(z-pz)**2=r**2
# Returnerer radiusen til ny sirkel og sammenlikner
def sirkel(sx,sy,sz,px,py,pz):
    radiusSquared = round((sx-px)**2+(sy-py)**2+(sz-pz)**2)
    return sqrt(radiusSquared)

index = 0
for axis in vector:
    vector[index] = (S[index]-P[index])
    absVector[index] = abs(S[index]-P[index])
    print(index, axis)
    index += 1

for axis in absVector:
    length += axis * axis
length = sqrt(round(length))

print(absVector, length)

# Sirkelen sin radius dersom punktet P ble brukt som referanse
'''sirkelCalc = sirkel(Sx,Sy,Sz,Px,Py,Pz)



print("Kalkulert sirkelradius:", sirkelCalc)

if( sirkelCalc > r ):
   print( "P ligger utenfor kuleflaten" )
elif( sirkelCalc < r ):
   print( "P ligger inni kuleflaten" )
else:
   print( "P ligger på kuleflaten" )'''