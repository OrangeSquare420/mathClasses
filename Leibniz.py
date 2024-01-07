def verdiAvPi(i):
    utregning = float(0.0)
    for iterasjon in range(i):
        utregning += float(( ( -1 ) ** iterasjon ) / ( 2 * iterasjon + 1))
        #print(utregning)
        
    return float(4 * utregning)

print(verdiAvPi(10000000))