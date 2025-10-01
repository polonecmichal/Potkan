import math
a =int(input("zadaj mi stranu a:"))
b =int(input("zadaj mi stranu b:"))
c =int(input("zadaj mi stranu c:"))
if a+b>c and a+c>b and b+c>a:
    print("tento trojuholnik moze existovat")   
if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2):
    print("je pravouhly")
o = (a+b+c)
po = o/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print("obvod je:",o)
print("obsah je:",s)
print("polovica obvodu je:",po)
Va = (a*(s*2/a))/2
Vb = (b*(s*2/b))/2
Vc = (c*(s*2/c))/2
print("vyska na stranu a je:",Va)
print("vyska na stranu b je:",Vb)     
print("vyska na stranu c je:",Vc)
pvpis = (s*2/a)
print("dlzka priesecnika vpisanej kruznice na je:",pvpis)
popis = (s*2/po)
print("dlzka priesecnika opisanej kruznice je:",popis)
#pocitam uhly#
alfa = round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
beta = round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
gama = round(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))),2)



a =int(input("zadaj mi stranu a:"))
b =int(input("zadaj mi stranu b:"))
c =int(input("zadaj mi stranu c:"))

if a > b and a > c :
 if b > c:
        print(a,b,c)

elif b > a and b > c:
    if a > c: print(b,a,c)


elif c > a and c> b:
    if a > b:     print (c,a,b)
    
else: print(c,b,a)
