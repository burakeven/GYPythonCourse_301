#FONKSIYON YAZIMI
#def ile fonksiyon yazimi yapilir.

def kare_al(x):
    print(x**2)
    
kare_al(4)    
#-----------------------------------------------
def kare_al(x):
    print("Girilen sayinin karesi: " + str(x**2))
kare_al(4)      


def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(5)

#ON TANIMLI ARGUMANLAR
def carpim(x,y):
    print(x*y)
    
#ARGUMANLARIN SIRALAMASI
def carpim(x,y=1):
    print(x*y)
    
carpim(y=2, x=3)
    
#NE ZAMAN FONKSIYON YAZILIR?
#isi,nem,sarj

def direk_hesap(isi,nem,sarj):
    print((isi*nem)/sarj)
    
direk_hesap(5, 6, 28)

#CIKTIYI GIRDI OLARAK KULLANMAK
def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj


cikti = direk_hesap(2, 5, 25)
cikti
print(cikti)

x=10
y=20

def carpma_yap(x,y):
    return x*y

carpim(2,3)

#LOCAL VE GLOBAL DEGISKENLER
x = []
def eleman_ekle(y):
    x.append(y)
    print(str(y)+ " ifadesi eklendi.")
#fonksiyon içerisinde x olmadigi icin global degisken olan x'e ulasabiliriz ve 
#yapacagimiz islemleri halledebiliriz.
    
eleman_ekle(5)
eleman_ekle("burak")

x

#KARAR & KONTROL YAPILARI
#True-False

sinir = 5000
sinir == 4000 #sinir 4000 mi? 4000 olmadigi icin false doner.

#if

sinir=20000
gelir=20000

if gelir<sinir:
    print("Geliriniz sinir noktasina ulasamadi.")
else:
    print("Geliriniz sinir noktanizdan yuksek.")

#else
if gelir>sinir:
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk")
    
#elif
sinir =50000
gelir1=60000
gelir2=50000
gelir3=35000

if gelir3>sinir:
    print("Tebrikler.")
elif gelir3<sinir:
    print("Uyari aldiniz.")
else:
    print("Gelir sinira esit degildir.")
    
#MINI UYGULAMA
sinir=50000
magaza_adi=input("Magaza Adi Nedir?")
gelir=int(input("Gelirinizi giriniz"))
#Kullanicidan gelen bilgiler her zaman string olarak gelir ve operasyonel bir
#islem yapmamiz gerektiginde bunu cevirmemiz gerekmektedir.
if gelir>sinir:
    print("Tebrikler: " + magaza_adi + " Promosyon kazandiniz." + " geliriniz yuksek.")
elif gelir==sinir:
    print("Geliriniz sinira esit.")
else:
    print("Uyari aldiniz, cabalayin. " + str(gelir))

#DONGULER - FOR

ogrenci = ["burak","mehmet","berk","tugce"]

for i in ogrenci:
    print(i)

maaslar= [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i*0.15)
    
#FONKSIYON VE DONGU BERABER KULLANIMI

def kare_al(x):
    print(x*2)
    
kare_al(2)

maaslar2= [1000,2000,3000,4000,5000]

for i in maaslar2:
    print(i)
    
#maas zammi %20
1000*.20+1000

def yeni_maas(x):
    print(x*0.20+x)

yeni_maas(2500)

for i in maaslar2:
    yeni_maas(i)
    
#mini uygulama
#if, for ve fonksiyon beraber

maaslar2= [1000,2000,3000,4000,5000]
def deger1(x):
    print(x*0.30+x)
def deger2(x):
    print(x*0.20+x)

for i in maaslar2:
    if i>=3000:
        deger2(i)
    elif i<3000:
        deger1(i)

4000*0.20+4000

#break & continue
maaslar3= [8000,5000,2000,1000,3000,7000,1000]
dir(maaslar3)

maaslar3.sort()
maaslar3

for i in maaslar3: #3000'e geldiginde döngüyü bozdu.
    if i==3000:
        print("Kesildi.")
        break
    print(i)
    
for i in maaslar3: #3000'i atlamış olduk.
    if i==3000:
        continue
    print(i)
    
sayi=1
while sayi<10:
    print(sayi)
    sayi+=1

