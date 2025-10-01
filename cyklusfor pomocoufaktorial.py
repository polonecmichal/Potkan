#napiste program ktory vypocita fakttorial cisla zadaneho uzivatelom
import math
a = int(input("Zadaj cislo, starký: "))
výstup = 1
for i in range(1, a + 1):
    výstup = výstup * i #výstup *=i
print("výstup:")
