def f(x):
    return -1 * (x-2) * (x-3) * (x-5)


def sum(funk, a, b):
    # Klarerer variabel for sum
    S = 0
    
    # Klarerer variabel for index / steg
    i = 0
    
    # Antall rektangler / steg / n / tallet i toppen
    n = 10000

    # Finner delta x / størrelsen på hvert steg / bunnlinjen i rektangel
    d = (b-a)/n

    # Kjører gjennom løkken frem til indeks er nådd antall rektangler
    while i < n:
        # Finner bestemt x-verdi bbasert på indeks og stegstørrelse
        x_i = a + d*i

        # Finner summen av tidligere sum og legger til 
        # funksjonsverdien multiplisert med steg-størrelse
        S = S + funk(x_i) * d

        # Legger til en indeks
        i += 1

    return S

values = [sum(f,0,2), sum(f,2,3), sum(f,3,5)]



print(sum(f,0,5))