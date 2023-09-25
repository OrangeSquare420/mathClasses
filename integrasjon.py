def f(x):
    return 10*x**3-x**2+3*x-6

def integral(funksjon, a, b):
    
    step = float(0.0001) # Nøyaktigheten
    sum = float(0) # Variabel for å lagre sum
    
    teller = 0 # Teller opp hvor lang programmet er kommet
    
    while teller < b:
        
        sum += funksjon(a+teller)
        teller += step
    
    returnValue = sum / 10000
    
    if returnValue <= 0:
        returnValue = returnValue * -1
    return returnValue # Dele på antall punkter


print(integral(f, 0, 2))