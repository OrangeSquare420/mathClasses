# Definerer funksjonen a med n som parameter
def a(n):
    # Fysisk umulig å skjære en pizza et negativt antall ganger. 
    if n > 0:
        # Returnerer kursiv formel
        return (0.5*n**2) + (0.5*n) + 1
    else:
        # Returnerer null dersom hvis-løkke er usann
        return 0

# Tar inn en n-verdi fra bruker
indeks = int(input("Hvilket ledd i Lazy caterers sequence: "))

#Blank linje
print("\n")

# Printer ut funksjonen med indeks som parameter
print(a(indeks))