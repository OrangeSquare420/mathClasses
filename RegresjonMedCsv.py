from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

# Den store fordelen med å gjennomføre regresjon i Python er at vi kan hente data rett frå datafiler 
# og slepp å skrive dei inn i reknearket i GeoGebra. 
# Under ser vi på korleis vi kan lese data frå ei såkalla .csv (Comma-Separated-Values)- fil. 


#Hentar inn data frå fila Tidevann.csv
df = pd.read_csv("Tidevann.csv", sep=";", decimal='.')

time=df['tid'].tolist()
vannstand=df['vannstand'].tolist()

# Definerer funksjonen h 
def h(t, A, phi, d): 
    return A*sin(0.524*t + phi) + d 

# Bestemmer konstantene 
[A, phi, d] = curve_fit(h, time, vannstand)[0] 
print("A =", round(A, 2)) 
print("phi =", round(phi, 2)) 
print("d =", round(d, 2)) 

# Plotter dataene sammen med grafen til h 
plot(time, vannstand, "o") 
xlabel("Tid (timer)") 
ylabel("Vannstand (cm)") 
t = linspace(0, 24, 1000) 
plot(t, h(t, A, phi, d), "r") 
show()