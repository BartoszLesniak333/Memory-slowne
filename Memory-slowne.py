import sys
import os
import time

latwy=('test', 'proba')   #probna lista
sredni=('ojciec','wynik')   #probna lista
trudny=('walic','nie wiem')   #probna lista
sprawdzanie=[]

def zwalnianie():
    sprawdzanie.clear()

def latwy_ilosc():
    n=len(latwy)
    wynik=0
    x=0
    while x<n:
        slowo=str(input("Podaj słowo: \n"))
        m=len(sprawdzanie) 
        for i in range(0, m):           #sprawdzanie czy slowo sie nie powtorzylo
            if(slowo==sprawdzanie[i]):
                print("Powtorzone slowo")
                kontyuowanie(wynik)
        
        if slowo in latwy:              #dodawanie punktow za dobre slowo
            wynik+=1
        else:                           #konczenie programu 
            print("Zle slowo")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x+=1
    kontyuowanie(wynik)
def sredni_ilosc():
    n=len(sredni)
    wynik=0
    x=0
    while x<n:
        slowo=str(input("Podaj słowo: \n"))
        m=len(sprawdzanie) 
        for i in range(0, m):           #sprawdzanie czy slowo sie nie powtorzylo
            if(slowo==sprawdzanie[i]):
                print("Powtorzone slowo")
                kontyuowanie(wynik)
        
        if slowo in sredni:              #dodawanie punktow za dobre slowo
            wynik+=1
        else:                           #konczenie programu 
            print("Zle slowo")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x+=1
    kontyuowanie(wynik)
def trudny_ilosc():
    n=len(trudny)
    print("Zapamiętaj słowa masz na to 5 min.")
    for i in range(0,n):
        print(trudny[i])
    time.sleep(300)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik=0
    x=0
    while x<n:
        slowo=str(input("Podaj słowo: \n"))
        m=len(sprawdzanie) 
        for i in range(0, m):           #sprawdzanie czy slowo sie nie powtorzylo
            if(slowo==sprawdzanie[i]):
                print("Powtorzone slowo")
                kontyuowanie(wynik)
        
        if slowo in trudny:              #dodawanie punktow za dobre slowo
            wynik+=1
        else:                           #konczenie programu 
            print("Zle slowo")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x+=1
    kontyuowanie(wynik)

def koniec():
    print("Dziekujemy za granie!")
    sys.exit(0)

def kontyuowanie(wynik):          #koncowa funkcja ma pokazywac wynik
    zwalnianie()
    print("Ostateczny wynik:",wynik,"pkt")
    koniec=str(input("Czy chcesz wyjsc z programu? y/n \n"))
    if(koniec=='y'):
        sys.exit(0)
    if(koniec=='n'):
        os.system("cls")
        main()

def ilosc():         #tryb do ilosci
    print("Wybór poziomu trudności. \n1.Latwy \n2.Sredni \n3.Trudny")
    wybor=int(input("Wybierz poziom trudnosci:"))
    if(wybor==1):
        os.system("cls")
        latwy_ilosc()
    if(wybor==2):
        os.system("cls")
        sredni_ilosc()
    if(wybor==3):
        os.system("cls")
        trudny_ilosc()
    

def na_czas():          #tryb gry na czas
    print("Na czas")

def main():             #glowna funkcja
    print("Menu \n1. Ilosc\n2. Na czas\n3. Wyjscie")
    wybor=int(input("Wybierz tryb: "))      #zapytanie o wybor
    if(wybor==1):
        os.system("cls")
        ilosc()
    if(wybor==2):
        os.system("cls")
        na_czas()
    if(wybor==3):
        koniec()

main()          #wywolanie funckji glownej