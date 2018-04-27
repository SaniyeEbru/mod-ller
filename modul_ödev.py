def isletmeKar():
    gelirler=int(input("gelirleri gir:"))
    giderler=int(input("giderleri gir:"))
    kar=gelirler-giderler
    return kar



def adamBasiCiro():
    ciro=int(input("toplam ciro:"))
    calisan=int(input("toplam çalışan sayısı:"))
    ciroH=ciro/calisan
    return ciroH



def aktif():
    kasaHesabı=20000
    alınanCek=10000
    bankalar=5000
    alıcakSenet=28000
    ticariMal=65000
    binalar=150000
    tasıtlar=25000
    demirbaslar=8000
    global aktifler
    aktifler=kasaHesabı+alınanCek+bankalar+alıcakSenet+ticariMal+binalar+tasıtlar+demirbaslar
    return aktifler
def pasif():
    bankaKredi=42000
    satıcılar=60000
    bankaKrediH=35000
    borcSenet=115000
    sermaye=59000
    global pasifler
    pasifler=bankaKredi+satıcılar+bankaKrediH+borcSenet+sermaye
    return pasifler




class oran():
    def __init__(self,begeni,yorum,paylasım,icerik,takipci):
        self.begeni=begeni
        self.yorum=yorum
        self.paylasım=paylasım
        self.icerik=icerik
        self.takipci=takipci
        print("etkileşim oranı=",[((begeni+yorum+paylasım)/icerik)/takipci]*100)








