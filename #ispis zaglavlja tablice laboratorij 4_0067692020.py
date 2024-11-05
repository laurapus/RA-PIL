#ispis zaglavlja tablice (brojevi od 1 do 10)
print("  ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n"+"-"*45)
#ispis redova tablice množenja
for i in range(1, 11):
    print(f"{i:2}|", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="") #ispis rezultata množenja
    print() # novired nakon svakog reda tablice
