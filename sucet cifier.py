#scitaj cifry zadaneho cisla
number = int(input("Zadaj cislo:"))
ScitoCif = 0
while number !=0:
    cifra = number % 10
    ScitoCif += cifra 
    number //= 10 #odstranenie poslednej cifry
print("Sucet cifier je: ", ScitoCif)
