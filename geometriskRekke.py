def s(i, a1, k):
    teller = (k**i-1)
    nevner = (k-1)
    return a1 * (teller/nevner)

# Tar inn et langt tall
# Returnerer to verdier
# Verdi 1 => Grunnverdi, lavere enn 10
# Verdi 2 => 10-er eksponenten til tallet
def standardForm(tall):
    eksponent = 0
    while tall > 10:
        tall = tall / 10
        print(tall)
        eksponent += 1
        
    return [round(tall, 2), eksponent]

k = 4
a1 = 1

verdi = standardForm(round(s(100, a1, k)))

print(f'S100 = {verdi[0]} x 10^{verdi[1]}')