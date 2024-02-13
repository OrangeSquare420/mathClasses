from pylab import *
from scipy.optimize import curve_fit 

# Leser inn dataene 
tid = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23] 
vannstand = [94, 43, 26, 61, 113, 138, 111, 59, 35, 64, 117, 146]

# Definerer funksjonen h som en generell funksjon. Perioden er gitt av oppgåveteksten. 
def h(t, A, phi, d): 
    return A*sin(0.524*t + phi) + d 

# Bestemmer konstantene ved hjelp av curve_fit
[A, phi, d] = curve_fit(h, tid, vannstand)[0] 
print("A =", round(A, 2)) 
print("phi =", round(phi, 2)) 
print("d =", round(d, 2)) 

# Plotter dataene sammen med grafen til h 
plot(tid, vannstand, "o") 
xlabel("Tid (timer)") 
ylabel("Vannstand (cm)") 
t = linspace(0, 24, 1000) 
plot(t, h(t, A, phi, d), "r") 
show()