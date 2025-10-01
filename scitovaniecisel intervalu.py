#spocitaj parne cisla z intervalu <a,b>
a=int(input("Zadaj zaciatok intervalu a: "))
b=int(input("Zadaj koniec intervalu b: "))
s=0
for i in range(a,b+1):
    if i%2==0:
        s=s+i
print("Suma parnych cisel v intervale <a,b> je: ",s)
