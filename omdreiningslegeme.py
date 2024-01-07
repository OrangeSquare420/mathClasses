# Funksjon som skal integreres
def f(x):
    e = 2.7182
    potens = x**2
    return e**potens

dx = 0.0001 # Skrittstørrelse
x_start = 1 # Integral start
x_stopp = 2 # Integral stopp

sum = 0 # Summen av alle integrerte verdier

while x_start < x_stopp:
    funksjonsverdi = f(x_start) # Finne funksjonsverdi
    areal = funksjonsverdi*funksjonsverdi*dx*3.14 #Finne areal av funksjonsverdi
    
    sum += areal # Legge til verdien i summevariabelen
    
    print(sum*dx)
    
    x_start += dx # Legge til nytt skritt / steg
    
print("Volum:", sum)