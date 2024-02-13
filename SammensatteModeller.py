from pylab import *
from scipy.optimize import curve_fit

# Leser inn dataene
tid = [0.25, 0.50, 1, 2, 3, 5, 8, 12, 24]
koffein = [6.99, 9.64, 10.52, 10.20, 9.80, 8.18, 6.25, 3.48, 0.63]

# Definerer funksjonen f
def f(t, a, b, c):
    return a*(e**(-b*t) - e**(-c*t))

# Bestemmer a, b og c
[a, b, c] = curve_fit(f, tid, koffein)[0]
print("a =", round(a, 3))
print("b =", round(b, 5))
print("c =", round(c, 3))

# Plotter dataene sammen med grafen til f
plot(tid, koffein, "o")
xlabel("Tid (timer)")
ylabel("Konsentrasjon av koffein (mg/L)")
t = linspace(0, 24, 1000)
plot(t, f(t, a, b, c), "r")
show()