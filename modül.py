from modul_ödev import isletmeKar
k=isletmeKar()
print(k)



from modul_ödev import adamBasiCiro
c=adamBasiCiro()
print(c)


from modul_ödev import aktif
from modul_ödev import pasif
a=aktif()
print(a)
p=pasif()
print(p)
if (a==p):
    print("bilanço doğru.")
else:
    print("bilanco yanlıs.")


from modul_ödev import oran
ybs1=oran(365000,65000,870,500,1125000)
print(ybs1)
if(ybs1>0.20):
    print("başarılı")
else:
    print("basarısız")
ybs2=oran(450000,25000,380,100,1450000)
print(ybs2)
if(ybs2>0.20):
    print("başarılı")
else:
    print("basarısız")
ybs3=oran(582000,52000,1200,650,2000000)
print(ybs3)
if(ybs3>0.20):
    print("başarılı")
else:
    print("basarısız")
