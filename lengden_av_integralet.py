from scipy.integrate import quad
import numpy as np

# Definerer funksjonen, sqrt(1+f'(x))^2
def f(x):
    return np.sqrt(1 + (4*x)**2)

dx = 0.0001 # Skrittstørrelse
x_start = 0 # Integral start
x_stopp = 10 # Integral stopp

sum = 0 # Summen av alle integrerte verdier

while x_start < x_stopp:
    funksjonsverdi = f(x_start) # Finne funksjonsverdi
    lengde_stykke = funksjonsverdi*dx #Finne areal av funksjonsverdi
    
    sum += lengde_stykke # Legge til verdien i summevariabelen
    
    x_start += dx # Legge til nytt skritt / steg
    
print("Volum:", sum)