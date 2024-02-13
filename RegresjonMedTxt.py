from pylab import *
from scipy.optimize import curve_fit

# Leser inn dataene og trekker ut verdiene for perioden 2015−2020
co2_alle = loadtxt("co2_mm_mlo.txt", delimiter = ",", usecols = (2, 3))
aar_alle = co2_alle[:, 0]
co2_alle = co2_alle[:, 1]
intervall = (aar_alle >= 2015) & (aar_alle < 2021)
aar = aar_alle[intervall]
co2 = co2_alle[intervall]

# Definerer funksjonen f
def f(t, a, b, c, d):
    return a*t + b + c*sin(2*pi*t + d)

# Bestemmer verdiene av parametrene og skriver ut verdiene
[a, b, c, d] = curve_fit(f, aar-2015, co2)[0]
print("a =", round(a, 2))
print("b =", round(b, 2))
print("c =", round(c, 2))
print("d =", round(d, 2))

# Lager plott av dataene med tilpasset kurve
plot(aar, co2, ".")
ylim(395, 420)
xlabel("År")
ylabel("CO2-konsentrasjon (ppm)")
t = linspace(0, 6, 1000)
plot(t + 2015, f(t, a, b, c, d), "r")
show()