import math 


def f(x, tverrsnitt):
    value = (tverrsnitt**2)-(x-tverrsnitt)**2
    
    if value > 0:
        return math.sqrt(value)
    else:
        return 0

def antallFyrstikkerITverrsnitt(tverrsnitt):
    dx=2
    sum=0
    while dx < tverrsnitt:
        val = math.floor(f(dx,tverrsnitt)/2)
        sum += val
        dx += 2
    return sum



meterTrestokk = int(input("Antall meter trestokk:"))
tverrsnitt = int(input("Tverrsnitt trestokk mm:"))

lengdeForhold = meterTrestokk*100/48

print("Antall fyrstikker i trestokken:", math.floor((antallFyrstikkerITverrsnitt(tverrsnitt)*lengdeForhold)))

