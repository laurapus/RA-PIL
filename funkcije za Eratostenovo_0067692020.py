#definiranej funkcije za Eratostenovo sito
def erastotenovo_sito(limit):
    brojevi=[True]*(limit+1) # Inicijalizacije čiste za označavanje prostih brojeva
    brojevi[0]= brojevi[1]=False # 0 i 1 nisu prosti brojevi
    # glavni algoritam za sito
    for i in range(2, int(limit**0.5)+1):
        if brojevi[i]:
            for j in range(i*i, limit + 1,i):
                brojevi[j]= False # Označivanje višekratnika kao neprostih brojeva
# Ispis prostih brojeva
prosti_brojevi=[i for i, is_prime in enumerate(brojevi)if is_prime]
def new_func(prosti_brojevi):
    return prosti_brojevi

return new_func(prosti_brojevi)
# Definiramo limit za prvih 100 prostih brojeva
limit=542 #542 je dovoljan limit da bismo dobili 100 prostih brojeva
parnih_100_prostih= erastotenovo_sito(limit)[:100]
#ispis prvih 100 prostih brojeva
print(prvih_100_prostih)
