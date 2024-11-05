# tražimo unos koiko brojeva ćemo provjeriti jesu li parni ili neparni
n=int(input("unesi količinu brojeva za koju želiš ispitati parnost"))
# varijable za brojanje parnih i neparnih brojeva
parni_broj=0
neparni_broj=0
#petlja za unos i provjeru svakog broja
for i in range(n):
    broj=int(input(f"unesite broj {i+1}:"))
    #provjera parnosti broja
    if broj%2==0:
        print(f"broj {broj} je paran.")
        parni_broj+=1
    else:
        print(f"broj {broj} je neparan.")
        neparni_broj+=1
#ispis konačnog broja parnih i neparnih brojeva
print("\nukupno parnih brojeva:",parni_broj)
print("ukupno neparnih brojeva:",neparni_broj)    